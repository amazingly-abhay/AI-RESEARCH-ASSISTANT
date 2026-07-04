"""
analysis_templates.py — Declares structured markdown layout templates for each of the 9 Financial Ontology Domains.
"""
from typing import Dict

# Response structures matching professional Equity Research formats
ANALYSIS_TEMPLATES: Dict[str, str] = {
    "business_risk": """=== RESPONSE STRUCTURE (Business Risk) ===
### Executive Summary
[Summary of primary strategic/operational risks and mitigation stability]

### Key Business Risks
- **[Risk 1 name]:** [Detailed explanation, evidence source, and potential operational impact]
- **[Risk 2 name]:** [Detailed explanation, evidence source, and potential operational impact]
- **[Risk 3 name]:** [Detailed explanation, evidence source, and potential operational impact]

### Management Mitigations
- [Executive strategies and operational safeguards mentioned in conference calls/MD&A]

### Financial Context
- [Revenues, Profits, and Margin trends indicating company scale, noting that these metrics represent context rather than direct risk indicators]

### Limitations & Evidence
- **Available Evidence:** [Specify if Risk Factors, Annual Reports, MD&A, or News were used]
- **Unavailable Details:** [List any missing metrics or files and their analytical impact]

### Conclusion & Confidence
- **Analytical Outlook:** [Probabilistic summary of operational resilience]
- **Confidence Level:** [High/Medium/Low based on completeness of qualitative disclosures]
""",

    "financial_risk": """=== RESPONSE STRUCTURE (Financial Risk) ===
### Executive Summary
[Summary of short-term liquidity safety and long-term solvency leverage status]

### Liquidity Risk Analysis
- **Current & Quick Ratios:** [Values and safety evaluation relative to standard thresholds]
- **Working Capital Status:** [Buffer size and operational cash flow alignment]

### Solvency & Leverage Analysis
- **Debt to Equity:** [Current leverage ratio evaluation]
- **Interest Coverage:** [EBIT safety buffer coverage calculation]
- **Solvency Risk Outlook:** [Probabilistic assessment of solvency health]

### Cash Flow Strength
- [Operating cash flow trend versus capital expenditure requirements]

### Limitations & Evidence
- **Available Metrics:** [Ratios found in SQLite database]
- **Unavailable Metrics:** [List missing solvency/liquidity metrics and their analytical impact]

### Conclusion & Confidence
- **Analytical Outlook:** [Solvency and liquidity risk assessment summary]
- **Confidence Level:** [High/Medium/Low based on ratio coverage]
""",

    "competitive_analysis": """=== RESPONSE STRUCTURE (Competitive Analysis) ===
### Executive Summary
[Summary of company's market position, competitive advantages, and industry threats]

### Market Position & Peer Group
- **Key Competitors:** [Identify peer companies]
- **Market Share & Scale:** [Scale comparison and market share dynamics]

### Competitive Advantages (Economic Moat)
- [Identify specific Moat sources: Network Effects, Switching Costs, Cost Advantage, or Brand scale]

### SWOT Assessment
- **Strengths:** [Core structural advantages]
- **Weaknesses:** [Strategic drawbacks or peer disadvantages]
- **Opportunities:** [Growth/expansion areas]
- **Threats:** [Disruption or competitive pricing pressure]

### Limitations & Evidence
- **Available Evidence:** [Sources utilized]
- **Unavailable Details:** [Details missing and impact]

### Conclusion & Confidence
- **Analytical Outlook:** [Competitive durability summary]
- **Confidence Level:** [High/Medium/Low based on peer info availability]
""",

    "valuation": """=== RESPONSE STRUCTURE (Valuation) ===
### Executive Summary
[Summary of current pricing multiples relative to growth and peer averages]

### Current Valuation Multiples
- **P/E Ratio:** [Value compared to historical average and peer average]
- **P/B Ratio:** [Value compared to book value benchmarks]
- **PEG Ratio:** [Growth-adjusted multiple evaluation]

### Peer Comparison Table
| Company | P/E | P/B | ROE | PEG |
|---|---|---|---|---|
| [Target] | [P/E] | [P/B] | [ROE] | [PEG] |
| [Peer 1] | [P/E] | [P/B] | [ROE] | [PEG] |

### Growth Justification
- [Does current earnings growth support the multiples? Explain using ROCE/ROE efficiency]

### Limitations & Evidence
- **Available Valuation Data:** [Ratios used]
- **Unavailable Multiples:** [Missing ratios and impact]

### Conclusion & Confidence
- **Valuation Stance:** [Probabilistic valuation outlook. Do NOT state a definitive BUY/SELL recommendation. Remain balanced]
- **Confidence Level:** [High/Medium/Low based on metric completeness]
""",

    "growth_analysis": """=== RESPONSE STRUCTURE (Growth Analysis) ===
### Executive Summary
[YoY and QoQ growth summary across revenue and net income lines]

### Historical Growth Trends
- **Revenue Growth Trend:** [Past 3-5 years top-line performance]
- **Profitability Growth Trend:** [Operating margins and EPS growth YoY trends]

### Growth Drivers
- [Core engines: Segment additions, price increases, volume expansions]

### Guidance & Future Outlook
- [Management guidance targets, project pipelines, and expansion timelines]

### Limitations & Evidence
- **Available Data:** [Metrics and sources]
- **Missing Growth Details:** [Unavailable parameters and impact]

### Conclusion & Confidence
- **Growth Stance:** [Growth sustainability outlook]
- **Confidence Level:** [High/Medium/Low]
""",

    "dividend_analysis": """=== RESPONSE STRUCTURE (Dividend Analysis) ===
### Executive Summary
[Overview of yield attractiveness and payout safety margins]

### Dividend Metrics
- **Dividend Yield:** [Current yield compared to peer averages]
- **Payout Ratio:** [Payout percentage relative to earnings safety limits]

### Stability & Sustainability
- **Payout History:** [Consistency and growth trend of payments]
- **Free Cash Flow Coverage:** [Is dividend covered by free cash flow?]

### Limitations & Evidence
- **Available Metrics:** [Yield, histories, payouts]
- **Missing Parameters:** [List gaps and impact]

### Conclusion & Confidence
- **Dividend Sustainability Outlook:** [Sustainability classification]
- **Confidence Level:** [High/Medium/Low]
""",

    "management_quality": """=== RESPONSE STRUCTURE (Management Quality) ===
### Executive Summary
[Summary of corporate governance and leadership execution track record]

### Execution & Capital Allocation
- [Historical capital allocation choices: acquisitions, R&D, share buybacks]

### Strategic Direction & Communication
- [Clarity of management guidance and transparency in investor communications]

### Limitations & Evidence
- **Available Information:** [CEO letters, calls, presentations]
- **Missing Disclosures:** [Unavailable documents and impact]

### Conclusion & Confidence
- **Management Review:** [Management credibility and capability assessment]
- **Confidence Level:** [High/Medium/Low]
""",

    "future_outlook": """=== RESPONSE STRUCTURE (Future Outlook) ===
### Executive Summary
[Summary of long-term strategic opportunities and expansion initiatives]

### Strategic Opportunities & Initiatives
- **Expansion Plans:** [Geographic, product, or capacity expansions]
- **Technology/AI Initiatives:** [Digital transformation or AI projects]

### Challenges & Expected Headwinds
- [Macroeconomic risks, regulatory updates, or demographic shifts]

### Limitations & Evidence
- **Available Outlook Sources:** [Transcripts, presentations, news]
- **Missing Guidance:** [Unavailable targets and impact]

### Conclusion & Confidence
- **Long-term Outlook Stance:** [Long-term performance view]
- **Confidence Level:** [High/Medium/Low]
""",

    "financial_health": """=== RESPONSE STRUCTURE (Financial Health) ===
### Executive Summary
[Comprehensive assessment of operating margins, balance sheet health, and returns]

### Profitability & Returns
- **Profit Margin Trends:** [Gross, Operating, Net margins]
- **Capital Return Efficiency:** [ROE, ROCE trends]

### Capital Structure & Solvency
- **Leverage Metrics:** [Debt-to-Equity, Interest Coverage safety metrics]
- **Liquidity Status:** [Current & Quick ratios]

### Limitations & Evidence
- **Available Health Metrics:** [Ratios and snapshot items]
- **Missing Health Details:** [Unavailable items and impact]

### Conclusion & Confidence
- **Financial Health Rating:** [Overall financial health status summary]
- **Confidence Level:** [High/Medium/Low based on data density]
"""
}


class AnalysisTemplates:
    """Provides access to structured research templates for each domain."""

    @staticmethod
    def get_template(domain_key: str) -> str:
        """Retrieves the layout template instructions for a specific financial domain."""
        return ANALYSIS_TEMPLATES.get(domain_key.lower(), "")
