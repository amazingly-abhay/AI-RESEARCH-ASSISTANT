"""
financial_knowledge_base.py — Stores industry heuristics, financial definitions, and analytical rules for the reasoning engine.
"""
from typing import Dict, Any

class FinancialKnowledgeBase:
    """Provides professional financial metrics, risk ratios, valuation rules, and industry heuristics."""

    @staticmethod
    def get_definitions() -> Dict[str, str]:
        return {
            "PE": "Price-to-Earnings Ratio. Measures current share price relative to per-share earnings. High P/E can imply high expected growth or overvaluation; low P/E suggests undervaluation or structural challenges.",
            "PB": "Price-to-Book Ratio. Compares a firm's market value to its book value. Often used for capital-intensive companies or financial institutions. Values < 1.0 may indicate distress or deep value.",
            "PEG": "Price/Earnings-to-Growth Ratio. Divides P/E by annual EPS growth rate. A PEG < 1.0 suggests a stock is undervalued relative to its growth trajectory.",
            "ROE": "Return on Equity. Measures net income relative to shareholders' equity. Reflects capital allocation efficiency and profitability. ROE > 15-20% is generally considered strong.",
            "CurrentRatio": "Current Assets divided by Current Liabilities. Measures short-term liquidity. A ratio between 1.5 and 3.0 indicates healthy liquidity.",
            "InterestCoverage": "EBIT divided by Interest Expense. Measures safety margin for debt servicing. Ratios below 1.5 suggest high financial distress risk.",
            "DebtToEquity": "Total Debt divided by Shareholders' Equity. Indicates financial leverage. Highly leveraged firms (>2.0) are sensitive to interest rate hikes and operational downturns."
        }

    @staticmethod
    def get_heuristics() -> Dict[str, Any]:
        return {
            "valuation_heuristics": [
                "Always compare a firm's P/E and P/B with its peer averages and historical medians.",
                "If P/E is high, check if it is justified by high Return on Equity (ROE) and high forecast PEG (< 1.5).",
                "Ensure that earnings quality is solid (net income matches operating cash flows over time)."
            ],
            "solvency_heuristics": [
                "A highly leveraged firm (D/E > 1.5) must maintain stable operating cash flows and interest coverage > 3.0.",
                "Verify if short-term debt is covered by liquid cash and receivables (Quick Ratio > 1.0)."
            ],
            "growth_heuristics": [
                "Revenue growth without profit expansion indicates margin pressure or competitive pricing erosion.",
                "Look for consistency in Year-over-Year (YoY) organic revenue increases."
            ],
            "industry_rules": {
                "Technology/Software": {
                    "critical_metrics": ["Gross Margin", "Recurring Revenue (ARR/MRR)", "R&D as % of Revenue", "Free Cash Flow Margin"],
                    "moat_indicators": ["Switching Costs", "Network Effects", "IP/Patents"]
                },
                "Banking/Finance": {
                    "critical_metrics": ["Net Interest Margin (NIM)", "Capital Adequacy Ratio (CAR)", "Non-Performing Assets (NPA)", "P/B Ratio"],
                    "moat_indicators": ["Regulatory Barriers", "Scale", "Brand Trust"]
                },
                "Consumer/Retail": {
                    "critical_metrics": ["Same-Store Sales Growth", "Inventory Turnover", "Operating Margin"],
                    "moat_indicators": ["Brand Equity", "Cost Advantage", "Distribution Scale"]
                }
            }
        }
