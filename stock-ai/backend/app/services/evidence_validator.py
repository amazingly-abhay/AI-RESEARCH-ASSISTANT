"""
evidence_validator.py — Validates the quality of retrieved RAG evidence to ensure analyst-grade content.
"""
import re
from typing import List, Any

# Financial keywords to check for topic relevance density
FINANCIAL_KEYWORDS = [
    "revenue", "net profit", "profit", "eps", "operating margin", "ebit margin", 
    "yoy", "qoq", "guidance", "management commentary", "financial highlights", 
    "quarter ended", "ebitda", "deal win", "outlook", "guidance"
]

class EvidenceValidator:
    """Validates retrieved vector database chunks for content size, keyword presence, and numerical density."""

    @staticmethod
    def validate_chunks(
        chunks: List[Any], 
        min_chars: int = 500, 
        min_keywords: int = 3, 
        min_metrics: int = 3
    ) -> bool:
        """
        Checks if the list of retrieved document chunks contains sufficient analytical value.
        
        Args:
            chunks: A list of DocumentChunk or NewsChunk items.
            min_chars: Minimum character length aggregate.
            min_keywords: Minimum distinct financial keywords found in the text.
            min_metrics: Minimum instances of numbers or percentage expressions.
            
        Returns:
            True if quality is acceptable, False if it is low-quality and needs retry.
            """
        if not chunks:
            return False

        # Aggregate contents
        total_content = " ".join([getattr(c, "content", "") for c in chunks]).lower().strip()
        total_len = len(total_content)

        # 1. Check size limit
        if total_len < min_chars:
            return False

        # 2. Check presence of core financial keywords
        kw_count = 0
        for kw in FINANCIAL_KEYWORDS:
            if kw in total_content:
                kw_count += 1
                
        if kw_count < min_keywords:
            return False

        # 3. Check presence of numerical metric patterns (percentages, currency, comma-separated numbers)
        metric_matches = re.findall(r"\b\d+(?:\.\d+)?%?|\b\d{1,3}(?:,\d{3})+\b", total_content)
        if len(metric_matches) < min_metrics:
            return False

        return True
