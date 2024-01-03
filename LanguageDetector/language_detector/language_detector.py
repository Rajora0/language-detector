import joblib
from typing import Dict, Union

class LanguageDetector:
    
    def __init__(self, model_path: str = 'model.joblib') -> None:
        """
        Initialize the LanguageDetector object.

        Parameters:
            model_path (str): Path to the trained model file. Default is 'model_logistic_regression.joblib'.
        """
        self.model = joblib.load(model_path)

    def detect_language(self, text: str) -> Dict[str, Union[str, float]]:
        """
        Detect the language of the input text.

        Parameters:
            text (str): The input text to be classified.

        Returns:
            dict: A dictionary containing the label and score of the detected language.
        """
        # Check if the text contains only one word
        if len(text.split()) == 1:
            return {'label': 'unknown', 'score': 0.0}

        # Make predictions and get associated probabilities
        probabilities = self.model.predict_proba([text])[0]

        # Get the label with the highest probability
        label = self.model.classes_[probabilities.argmax()]

        # Create a dictionary with label and score
        result = {'label': label, 'score': float(probabilities.max())}

        return result
