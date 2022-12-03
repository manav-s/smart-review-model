# -- REQUIRED LIBRARIES: --
# Pattern: for Python 3+
# pip install Pattern
#   - for python 2.7x
#   - pip install pattern

# imports
from pattern3 import sentiment

class PatternModel:
    def __init__(self):
        pass

    def predict_sentiment(self, text: str):
        """
        Predicts the sentiment of a text using Pattern.
        Example: 
        "I love this movie!" -> 1.0 (positive)
        "I hate this movie!" -> -1.0 (negative)
        Output comes in the form of a float between -1.0 and 1.0 and as (polarity, subjectivity).
        Polarity: measures the positivity or negativity of a text.
        Subjectivity: measures the personal opinion and factual information contained in a text.
        """
        return sentiment(text)