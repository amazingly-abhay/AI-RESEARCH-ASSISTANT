"""
market_data_service.py — Service for real-time market stock quotes.
"""
import logging
from typing import Optional
from app.config import Settings
from app.services.ai_service import GeminiAIService
from app.services.company_detector import CompanyDetector
from app.providers.financial.base_provider import MarketDataPayload

logger = logging.getLogger(__name__)

class MarketDataService:
    def __init__(self, ai_service: GeminiAIService, settings: Settings) -> None:
        self._ai = ai_service
        self._settings = settings
        self._detector = CompanyDetector(ai_service)
        self._provider = self._init_provider()

    def _init_provider(self):
        provider_name = self._settings.financial_provider.lower() if hasattr(self._settings, "financial_provider") else "yahoo"
        if provider_name == "alphavantage":
            from app.providers.financial.alpha_vantage import AlphaVantageProvider
            return AlphaVantageProvider(ai_service=self._ai, api_key=getattr(self._settings, "alphavantage_api_key", None))
        elif provider_name == "finnhub":
            from app.providers.financial.finnhub import FinnhubProvider
            return FinnhubProvider(ai_service=self._ai, api_key=getattr(self._settings, "finnhub_api_key", None))
        elif provider_name == "polygon":
            from app.providers.financial.polygon import PolygonProvider
            return PolygonProvider(ai_service=self._ai, api_key=getattr(self._settings, "polygon_api_key", None))
        else:
            from app.providers.financial.yahoo_finance import YahooFinanceProvider
            return YahooFinanceProvider(ai_service=self._ai)

    def get_live_data(self, query: str) -> Optional[MarketDataPayload]:
        """Detects company ticker from the query and fetches real-time quote metrics."""
        ticker, name, confidence = self._detector.detect(query)
        if not ticker:
            logger.warning("MarketDataService: No company detected in query '%s'", query)
            return None
            
        logger.info("MarketDataService: Fetching live price for %s using %s", ticker, self._provider.provider_name)
        try:
            return self._provider.get_live_market_data(ticker)
        except Exception as exc:
            logger.error("MarketDataService: Failed to fetch market data for %s: %s", ticker, exc)
            return None

    @classmethod
    def format_market_data(cls, data: MarketDataPayload, ticker: str) -> str:
        """Formats the real-time quote information into a concise presentation structure."""
        change_sign = "+" if data.daily_change >= 0 else ""
        pct_sign = "+" if data.percentage_change >= 0 else ""
        market_status_str = f"\nMarket Status: {data.market_status}" if data.market_status else ""
        return (
            f"**{ticker.upper()} Market Quote**\n\n"
            f"**Current Price**: {data.currency} {data.current_price:,.2f}\n"
            f"**Daily Change**: {change_sign}{data.daily_change:,.2f} ({pct_sign}{data.percentage_change:,.2f}%)\n"
            f"**Day High**: {data.currency} {data.day_high:,.2f}\n"
            f"**Day Low**: {data.currency} {data.day_low:,.2f}\n"
            f"**Previous Close**: {data.currency} {data.previous_close:,.2f}"
            f"{market_status_str}\n"
            f"**Last Updated**: {data.last_updated}\n"
            f"**Source**: {data.source} Real-Time Market Feed"
        )
