"""
financial_reasoning_rules.py — Defines evidence priority layers, domain mapping rules, and language style guides for financial analysts.
"""
from typing import Dict, List, Any

# Evidence Priority order for evaluating data presence
EVIDENCE_PRIORITIES = [
    "Structured Financial Data",
    "Annual Reports",
    "Risk Factors",
    "Conference Calls",
    "Investor Presentations",
    "Recent News",
    "Financial Knowledge Base"
]

# Analyst language guidelines to ensure compliance with professional advisory standards
ANALYST_LANGUAGE_RULES = {
    "prefer": ["suggests", "indicates", "may imply", "appears", "based on available evidence", "likely"],
    "avoid": ["definitely", "guaranteed", "certainly", "must", "will definitely"]
}

# The 9 Financial Ontology Domains with their required evidence profiles
FINANCIAL_DOMAINS: Dict[str, Dict[str, Any]] = {
    "business_risk": {
        "domain_name": "Business Risk",
        "required_evidence": ["Annual Reports", "Risk Factors", "Conference Calls", "Recent News"],
        "non_critical": ["DebtToEquity", "CurrentRatio"],
        "critical_metrics": [],
        "rules": [
            "Prioritize qualitative risk factor disclosures from Annual Reports and MD&A.",
            "Use recent news to validate management's discussion of emerging risks.",
            "Structured financials are secondary and serve only as context."
        ]
    },
    "financial_risk": {
        "domain_name": "Financial Risk",
        "required_evidence": ["Structured Financial Data", "Annual Reports"],
        "non_critical": [],
        "critical_metrics": ["DebtToEquity", "CurrentRatio", "QuickRatio", "InterestCoverage"],
        "rules": [
            "Analyze leverage ratios and liquidity metrics.",
            "Assess solvency safety buffers and debt maturities.",
            "Correlate with cash flow stability."
        ]
    },
    "competitive_analysis": {
        "domain_name": "Competitive Analysis",
        "required_evidence": ["Annual Reports", "Recent News", "Industry Reports"],
        "non_critical": [],
        "critical_metrics": ["MarketShare"],
        "rules": [
            "Assess competitor metadata and industry landscape.",
            "Map strengths, weaknesses, and market positions relative to peers."
        ]
    },
    "valuation": {
        "domain_name": "Valuation",
        "required_evidence": ["Structured Financial Data", "Annual Reports"],
        "non_critical": [],
        "critical_metrics": ["PE", "PB", "PEG", "ROE", "ROCE"],
        "rules": [
            "Compare current valuation metrics with historical medians and industry peer averages.",
            "Cross-reference high P/E with high growth rates (PEG) and capital returns (ROE/ROCE).",
            "Never conclude overvalued or undervalued without sufficient evidence."
        ]
    },
    "growth_analysis": {
        "domain_name": "Growth Analysis",
        "required_evidence": ["Structured Financial Data", "Annual Reports", "Conference Calls"],
        "non_critical": [],
        "critical_metrics": ["RevenueGrowth", "ProfitGrowth", "EPSGrowth"],
        "rules": [
            "Plot historical YoY revenue and net profit growth trends.",
            "Correlate financial trajectory with management guidance and outlook."
        ]
    },
    "dividend_analysis": {
        "domain_name": "Dividend Analysis",
        "required_evidence": ["Structured Financial Data", "Annual Reports"],
        "non_critical": [],
        "critical_metrics": ["DividendYield", "PayoutRatio"],
        "rules": [
            "Check historical dividend stability and payout ratio safety margin.",
            "Assess free cash flow coverage to evaluate dividend sustainability."
        ]
    },
    "management_quality": {
        "domain_name": "Management Quality",
        "required_evidence": ["Annual Reports", "Conference Calls", "Investor Presentations"],
        "non_critical": [],
        "critical_metrics": [],
        "rules": [
            "Review CEO letters and management commentary from conference calls.",
            "Assess historical capital allocation effectiveness and execution track record."
        ]
    },
    "future_outlook": {
        "domain_name": "Future Outlook",
        "required_evidence": ["Conference Calls", "Investor Presentations", "Recent News"],
        "non_critical": [],
        "critical_metrics": [],
        "rules": [
            "Analyze guidance targets, expansion plans, and strategic initiatives.",
            "Incorporate industry trend projections and macroeconomic outlooks."
        ]
    },
    "financial_health": {
        "domain_name": "Financial Health",
        "required_evidence": ["Structured Financial Data", "Annual Reports"],
        "non_critical": [],
        "critical_metrics": ["Revenue", "Profit", "Margins", "Debt", "Cash", "ROE", "ROCE", "CurrentRatio"],
        "rules": [
            "Examine profitability margins, capital efficiency, and leverage structure.",
            "Provide an overview of liquidity and short-term debt coverage safety."
        ]
    }
}


class FinancialReasoningRules:
    """Manages lookup access for the Financial Domain Ontology rules."""

    @staticmethod
    def get_domain_profile(domain_key: str) -> Dict[str, Any] | None:
        """Retrieves required evidence parameters and guidelines for a given domain."""
        return FINANCIAL_DOMAINS.get(domain_key.lower())

    @staticmethod
    def get_priorities() -> List[str]:
        """Returns the sorted list of evidence evaluation priorities."""
        return EVIDENCE_PRIORITIES

    @staticmethod
    def get_language_rules() -> Dict[str, List[str]]:
        """Returns the analyst phrasing tone constraints."""
        return ANALYST_LANGUAGE_RULES
