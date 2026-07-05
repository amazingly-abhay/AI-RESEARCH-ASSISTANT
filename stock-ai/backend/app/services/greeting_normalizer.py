"""
greeting_normalizer.py — Normalizes and checks for small talk, greetings, or help requests.
"""
import re
from typing import Optional, Dict

class GreetingNormalizer:
    """Detects greetings, thanks, farewells, capabilities, and small talk to short-circuit queries."""

    # Normalization target buckets
    GREETINGS = {"hi", "hii", "hello", "hey", "heyy", "good morning", "good afternoon", "good evening", "greetings"}
    THANKS = {"thanks", "thank you", "thx", "appreciate it", "thankyou"}
    GOODBYES = {"bye", "byee", "goodbye", "see you", "talk to you later", "byebye"}
    CAPABILITIES = {
        "who are you", "what can you do", "how can you help", "help", 
        "capability", "how are you", "what do you do", "help me"
    }
    SMALL_TALK = {"ok", "okay", "cool", "great", "awesome", "welcome", "youre welcome", "you are welcome"}

    # Friendly predetermined responses
    RESPONSES = {
        "greeting": (
            "Hello! I'm your AI Stock Research Assistant. How can I help you today? "
            "You can ask me about companies, financial metrics, recent news, or ask to summarize quarterly results "
            "(e.g., 'Summarize TCS latest results')."
        ),
        "thanks": (
            "You're welcome! Feel free to ask about companies, earnings, annual reports, or financial news."
        ),
        "goodbye": (
            "Thanks for using the AI Financial Research Assistant. Have a great day!"
        ),
        "capability": (
            "I am an AI Financial Research Assistant. I can help you analyze stock metrics, "
            "compare financial sheets, summarize quarterly earnings (e.g., 'Latest results of Infosys'), "
            "explain conference calls, and lookup company news."
        ),
        "small_talk": (
            "Great! Let me know if you have any questions or if you would like to run a financial analysis."
        )
    }

    @classmethod
    def normalize(cls, text: str) -> str:
        """Applies lowercase, trims whitespace, strips punctuation/emojis, and collapses repeated letters."""
        # Convert to lowercase and strip spaces
        text = text.lower().strip()
        # Remove common punctuation and emoji symbols
        text = re.sub(r"[^\w\s]", "", text)
        # Collapse trailing character repetitions of length 2 or more (e.g., hii -> hi, heyy -> hey)
        text = re.sub(r"(.)\1+$", r"\1", text)
        # Collapse internal character repetitions of length 3 or more (e.g. heeyyy -> heey -> hey)
        text = re.sub(r"(.)\1{2,}", r"\1", text)
        return text.strip()

    @classmethod
    def get_short_circuit_response(cls, query: str) -> Optional[Dict[str, str]]:
        """
        Analyzes the query. If it is a greeting/small talk, returns a dict with:
        { "intent": "<intent_key>", "response": "<predefined_response>" }
        Otherwise, returns None.
        """
        normalized = cls.normalize(query)
        
        if normalized in cls.GREETINGS:
            return {"intent": "greeting", "response": cls.RESPONSES["greeting"]}
        if normalized in cls.THANKS:
            return {"intent": "thanks", "response": cls.RESPONSES["thanks"]}
        if normalized in cls.GOODBYES:
            return {"intent": "goodbye", "response": cls.RESPONSES["goodbye"]}
        if normalized in cls.CAPABILITIES:
            return {"intent": "capability", "response": cls.RESPONSES["capability"]}
        if normalized in cls.SMALL_TALK:
            return {"intent": "small_talk", "response": cls.RESPONSES["small_talk"]}
            
        return None
