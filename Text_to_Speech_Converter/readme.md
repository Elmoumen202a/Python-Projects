# Text to Speech Converter

This Python script converts the text of an article from a given URL into an MP3 file using NLTK, newspaper3k, and gTTS.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This script leverages NLTK for natural language processing, newspaper3k for article extraction, and gTTS for text-to-speech conversion. It is designed to take a URL as input, download the corresponding article, convert its text to speech, and save the result as an MP3 file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Elmoumen202a/Python-Projects.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Python-Projects/Text_to_Speech_Converter
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python text_to_speech.py
    ```

2. Enter the URL of the article when prompted.

3. The script will download the article, convert the text to speech, and save the result as "read_article.mp3" in the same directory.

## Example

For testing purposes, you can use the following URL:

- [Top Tech Companies Hiring Python Developers](https://hackr.io/blog/top-tech-companies-hiring-python-developers)

## Testing

To run tests, use the following command:

```bash
python tests.py
