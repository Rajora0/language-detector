from setuptools import setup, find_packages

setup(
    name='language-detector',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'joblib',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'language-detector=language_detector.cli:main',
        ],
    },
    package_data={'': ['model.joblib']},  # Include the model file
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    author='Rafael Rangel',
    author_email='rafaelj492@email.com',
    description='A language detector in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rajora0/language-detector',
    python_requires='>=3.10',
)
