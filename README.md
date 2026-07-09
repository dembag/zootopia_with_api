# Animal Web Generator

Welcome to Zootopia! This project allows you to fetch and display information 
about various animals using the API Ninjas data service. The information is 
saved to an HTML file that can be displayed in a Web Browser.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Author](#author)

## Features

- Retrieves animal information from an API
- Generates an HTML page automatically
- Uses templates for webpage generation

## Technologies

- Python 3
- HTML
- Requests

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dembag/animal-web-generator.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your API key from [API Ninjas](https://api-ninjas.com/):

```text
API_KEY=your_api_key_here
```

## Usage

Run:

```bash
python animals_web_generator.py
```

The generated webpage will be saved as `animals.html`.

## Project Structure

```
animal-web-generator/
│
├── animals_web_generator.py
├── data_fetcher.py
├── animals.html
├── .gitignore
├── README.md
└── requirements.txt
```

## Author

James Denby