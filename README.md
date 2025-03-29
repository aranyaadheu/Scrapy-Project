# Scrapy Project

This repository contains multiple Python scripts for web scraping using the `requests` and `BeautifulSoup` libraries. The scripts demonstrate how to scrape information from websites like IMDb and Quotes to Scrape.

## Files

### 1. **`main.ipynb`** - IMDb Top 25 Movies Scraper

This Jupyter notebook scrapes the top 25 movies from IMDb's top chart. It extracts the movie titles and their ratings.

#### How it works:
- It sends a GET request to the IMDb Top 250 page.
- It parses the HTML content using `BeautifulSoup`.
- It extracts the movie titles and ratings, then prints them out in a numbered list.

#### How to run:
1. Install the required dependencies:
    ```bash
    pip install requests beautifulsoup4
    ```
2. Run the notebook in Jupyter Notebook or Jupyter Lab to view the top 25 movies and their ratings.

---

### 2. **`quotes.ipynb`** - Quotes Scraper

This Jupyter notebook scrapes random quotes from the website **https://quotes.toscrape.com**. It extracts the text of each quote and prints them.

#### How it works:
- It sends a GET request to the Quotes to Scrape website.
- It parses the HTML content using `BeautifulSoup`.
- It finds all quotes marked with the `<span class="text">` tag and prints them out with numbering.

#### How to run:
1. Install the required dependencies:
    ```bash
    pip install requests beautifulsoup4
    ```
2. Run the notebook in Jupyter Notebook or Jupyter Lab to see the scraped quotes.

---

### 3. **`scrapy.py`** - Basic Web Scraping Example

This is a simple script that demonstrates how to scrape paragraphs (`<p>` tags) from a webpage. The script is meant to give you a basic understanding of web scraping.

#### How it works:
- It sends a GET request to a sample URL (`https://example.com`).
- It parses the HTML content and extracts all paragraphs.
- It prints the text of each paragraph on the page.

#### How to run:
1. Install the required dependencies:
    ```bash
    pip install requests beautifulsoup4
    ```
2. Run the script using Python:
    ```bash
    python scrapy.py
    ```

---

## Setup

### Prerequisites:
- Python 3.x
- Jupyter Notebook or Jupyter Lab (for `.ipynb` files)
- `requests` and `beautifulsoup4` libraries

### Installing Dependencies:
Install the necessary Python packages for web scraping:
```bash
pip install requests beautifulsoup4
