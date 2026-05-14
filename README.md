# Jumia Uganda Scraper

A Scrapy spider that scrapes smartphone listings from [Jumia Uganda](https://www.jumia.ug/smartphones/), extracting product names, prices, ratings, and URLs across all paginated results.

## Data Collected

| Field | Example |
|---|---|
| `name` | Samsung Galaxy A14 6.6" 4GB RAM 128GB |
| `price` | UGX 360,000 |
| `rating` | 4.2 out of 5 |
| `url` | https://www.jumia.ug/... |

## Setup

```bash
# Clone the repo
git clone https://github.com/kenbaker-gif/jumia-scraper.git
cd jumia-scraper

# Create virtual environment
python -m venv scraping_env
source scraping_env/bin/activate

# Install dependencies
pip install scrapy shub
```

## Usage

### Run locally
```bash
# Output to JSON
scrapy crawl jumia -o products.json

# Output to CSV
scrapy crawl jumia -o products.csv
```

### Deploy to Zyte Cloud
```bash
shub login
shub deploy
shub schedule jumia
```

## Results

- **2,156 products** scraped across 50 pages
- Covers all smartphone listings on Jumia Uganda

## Tech Stack

- [Scrapy](https://scrapy.org/) — scraping framework
- [Zyte](https://www.zyte.com/) — cloud deployment and scheduling

## Use Cases

- Price monitoring and tracking
- Market research for Ugandan e-commerce
- Competitor analysis
- Dataset for ML/data science projects
