# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.
"""

from typing import List, Dict, Tuple, Optional
import string

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)
        
        # Simple negation list
        self.negations = {"not", "never", "no", "n't", "isnt", "wasnt", "arent"}

    def preprocess(self, text: str) -> List[str]:
        """
        Cleans text by removing punctuation and splitting into lowercase words.
        """
        # Convert to lowercase
        cleaned = text.lower()
        # Remove basic punctuation
        for char in string.punctuation:
            cleaned = cleaned.replace(char, "")
        
        tokens = cleaned.split()
        return tokens

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score". 
        Includes logic to flip the score if a negation word (like 'not') is found.
        """
        tokens = self.preprocess(text)
        score = 0
        negate_next = False

        for token in tokens:
            # Check if this token is a negation word
            if token in self.negations:
                negate_next = True
                continue

            # Determine word value
            val = 0
            if token in self.positive_words:
                val = 1
            elif token in self.negative_words:
                val = -1
            
            # Apply negation if the previous word was "not"
            if negate_next:
                val = -val
                negate_next = False
            
            score += val

        return score

    def predict_label(self, text: str) -> str:
        """
        Converts score to "positive", "negative", "neutral", or "mixed".
        """
        tokens = self.preprocess(text)
        score = self.score_text(text)
        
        # Check for mixed feelings (presence of both positive and negative words)
        has_pos = any(t in self.positive_words for t in tokens)
        has_neg = any(t in self.negative_words for t in tokens)
        
        if has_pos and has_neg:
            return "mixed"
        
        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"

    def explain(self, text: str) -> str:
        """
        Returns a human-readable explanation of why the label was chosen.
        """
        tokens = self.preprocess(text)
        score = self.score_text(text)
        pos_found = [t for t in tokens if t in self.positive_words]
        neg_found = [t for t in tokens if t in self.negative_words]

        return (
            f"Score: {score} | "
            f"Pos: {pos_found or 'None'}, "
            f"Neg: {neg_found or 'None'}"
        )