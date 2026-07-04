"""
earnings_analysis_service.py — Service for classifying, planning, and prompt building for the Quarterly Earnings Analysis intent.
"""
import re
from typing import Dict, List, Any

# Earnings analysis classification keywords
EARNINGS_KEYWORDS = [
    r"latest\s+(?:quarterly\s+)?results",
    r"latest\s+earnings",
    r"quarterly\s+performance",
    r"financial\s+performance",
    r"earnings\s+call",
    r"investor\s+presentation",
    r"q[1-4]\s+summary",
    r"q[1-4]\s+results",
    r"quarterly\s+highlights",
    r"revenue\s+performance",
    r"profit\s+performance"
]

class EarningsAnalysisService:
    """Detects, maps, and templates earnings-specific financial queries."""

    @staticmethod
    def is_earnings_query(query: str) -> bool:
        """
        Determines if a query targets latest quarterly earnings instead of generic company overviews.
        """
        normalized = query.lower().strip()
        
        # Check explicit keywords
        for pattern in EARNINGS_KEYWORDS:
            if re.search(pattern, normalized):
                return True
                
        # Handle implicit performance patterns
        if "perform this quarter" in normalized or "quarterly report" in normalized:
            return True
            
        return False

    @staticmethod
    def get_retrieval_priority() -> List[str]:
        """
        Returns collection searching priorities for quarterly analysis.
        Annual reports are deprioritized as they do not capture the latest quarter results.
        """
        return [
            "Quarterly Financial Statements",
            "Investor Presentations",
            "Earnings Call Transcripts",
            "SQLite Metrics",
            "Latest News",
            "Annual Reports"  # Lowest priority for recent quarterly analysis
        ]

    @staticmethod
    def get_analyst_prompt(query: str, context_summary: str) -> str:
        """
        Generates a highly structured Morgan Stanley style prompt for Gemini.
        """
        return f"""You are an Equity Research Analyst at a major investment bank (e.g., J.P. Morgan, Goldman Sachs).
Your task is to summarize the latest quarterly results and business performance for the requested company based on the provided evidence.

Target Query: "{query}"

=== ANALYTICAL FOCUS ===
- Financial Highlights: Extract Revenue, YoY/QoQ Growth, Net Profit, Margins, and EPS.
- Business Highlights: Summarize major contract/deal wins, Cloud/AI initiatives, and product segments.
- Segment & Geography Performance: Extract performance across divisions and regions where available.
- Management Commentary: Capture executive statements regarding tailwinds, caution, and demand indicators.
- Challenges & Outlook: Extract guidance, discretionary spending risks, and macroeconomic headwinds.

=== RETRIEVED CONTEXT ===
{context_summary}

=== CONSTRAINTS ===
- Do NOT output generic definitions or historical overviews (e.g. "TCS is an IT company..."). Start immediately with current performance.
- Focus ONLY on the latest quarterly results.
- Never invent or estimate numbers. If a metrics is missing or unavailable, explicitly state that it is not disclosed in the retrieved sources, and continue reasoning using available qualitative data.
- Write in a professional, concise, and structured Research Note format.

=== RESPONSE FORMAT ===
Please output your research note using the following exact headings:

### Executive Summary
[Concise summary of the quarter's overall health and market position]

### Financial Highlights
- **Revenue:** [Value and YoY/QoQ Growth]
- **Net Profit:** [Value and growth rate]
- **Operating/EBIT Margin:** [Margin % and expansion/contraction basis points]
- **EPS:** [Earnings per share values]

### Business & Operational Highlights
- [Deal wins, technological updates, or core segment initiatives]

### Segment Performance
- [Breakdown of business units or geographical regions performance]

### Management Commentary
- [Primary commentary and strategic highlights from executive leadership]

### Growth Drivers & Outlook
- [Future guidance, pipeline strength, or growth catalysts]

### Challenges & Risks
- [Headwinds, margins pressure, or caution zones reported]

### Limitations & Evidence
- **Available Sources:** [List of documents/databases used]
- **Unavailable Details:** [List of missing metrics or disclosures]

### Conclusion & Confidence
- **Analytical Outlook:** [Neutral, cautious, or positive strategic review]
- **Confidence Level:** [High/Medium/Low based on source completeness]
"""
