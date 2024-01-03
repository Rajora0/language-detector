# Language Detector Project

## Overview

This project is part of the construction of a language detector that focuses on six languages: Dutch (nl), Portuguese (pt), French (fr), Spanish (es), Italian (it), and English (en), each with a dataset of 1000 samples. The data is sourced from the Wiki2018 text from Wikipedia and is centered around languages with origins in Latin and having the highest number of speakers.

## Dataset
- Dutch (nl): 1000 samples
- Portuguese (pt): 1000 samples
- French (fr): 1000 samples
- Spanish (es): 1000 samples
- Italian (it): 1000 samples
- English (en): 1000 samples
- German (de): 1000 samples

## Model
The language detection model is designed to be simple, lightweight, and robust. The primary focus is on achieving accurate classifications, and the training method can be altered or customized using Jupyter Notebooks. The model aims to provide fast and accurate language detection as a standalone module.

## Training
To modify or customize the training method, refer to the Jupyter Notebook provided in the project.

## Installation
To use this language detection module, you can install it using the following:

```
pip install language-detector
```

## Usage 
```
from language_detector import LanguageDetector

# Initialize the detector
detector = LanguageDetector()

# Detect language
result = detector.detect_language("This is an example text.")
print(result)

```

## Support
For any issues or questions, feel free to open an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.