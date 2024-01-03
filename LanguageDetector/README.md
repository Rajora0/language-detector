# Language Detector

## Overview

This Python package enables language detection for given texts utilizing a pre-trained model. It supports multiple languages and provides a confidence score for the classification.

## Installation

```
pip install language-detector
```


## Usage

```
from language_detector import LanguageDetector

# Initialize the detector
detector = LanguageDetector()

# Detect language
result = detector.detect_language("This is an example text in English.")
print(result)
```
## Example Output


```
{'label': 'en', 'score': 0.95}
```
In the example above, the detected language is English ('en') with a confidence score of 0.95.

## Dependencies

- joblib
- scikit-lear

## Model


The language detection model is based on a logistic regression classifier trained on a diverse dataset.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

