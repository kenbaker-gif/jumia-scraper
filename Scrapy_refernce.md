# Scrapy Reference Guide
> Personal reference — built from scraping Jumia UG

---

## 1. Environment Setup

Always use a dedicated virtual environment for scraping, separate from your ML/FaceAttend env.

```bash
python -m venv ~/scraping_env
source ~/scraping_env/bin/activate
pip install scrapy shub
```

To activate later:
```bash
source ~/scraping_env/bin/activate
```

---

## 2. Start a New Project

```bash
scrapy startproject <project_name>
cd <project_name>
```

Example:
```bash
scrapy startproject jumia_scraper
cd jumia_scraper
```

This creates the following structure:
```
jumia_scraper/
    scrapy.cfg
    jumia_scraper/
        __init__.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
```

---

## 3. Generate a Spider

```bash
scrapy genspider <spider_name> <domain>
```

Example:
```bash
scrapy genspider jumia jumia.ug
```

This creates `jumia_scraper/spiders/jumia.py` with a basic template.

---

## 4. Writing the Spider

Open the generated spider and replace with your logic:

```python
import scrapy

class JumiaSpider(scrapy.Spider):
    name = "jumia"
    allowed_domains = ["jumia.ug"]
    start_urls = ["https://www.jumia.ug/smartphones/"]

    def parse(self, response):
        # Loop through each product card
        for product in response.css("article.prd"):
            yield {
                "name": product.css("h3.name::text").get(),
                "price": product.css("div.prc::text").get(),
                "rating": product.css("div.stars._s::text").get(),
                "url": "https://www.jumia.ug" + product.css("a::attr(href)").get(),
            }

        # Follow pagination automatically
        next_page = response.css("a[aria-label='Next Page']::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

### Key CSS selector patterns:
| Selector | What it does |
|---|---|
| `css("tag.class::text")` | Gets text content |
| `css("tag::attr(href)")` | Gets attribute value |
| `.get()` | Returns first match or None |
| `.getall()` | Returns list of all matches |

---

## 5. Run the Spider

Basic run (prints to terminal):
```bash
scrapy crawl jumia
```

Export to JSON:
```bash
scrapy crawl jumia -o products.json
```

Export to CSV:
```bash
scrapy crawl jumia -o products.csv
```

---

## 6. Inspect Selectors (Shell)

Use the Scrapy shell to test CSS selectors before writing the spider:

```bash
scrapy shell "https://www.jumia.ug/smartphones/"
```

Then test selectors interactively:
```python
response.css("article.prd h3.name::text").getall()
response.css("div.prc::text").getall()
```

Exit with `exit()`.

---

## 7. Deploy to Zyte (Scrapy Cloud)

### Login
```bash
shub login
# Enter your Zyte API key when prompted
```

### Link project to Zyte
In your project root, create `scrapinghub.yml`:
```yaml
projects:
  default: YOUR_ZYTE_PROJECT_ID
```

Or let shub create it:
```bash
shub deploy
```

### Deploy and run
```bash
shub deploy          # uploads spider to Zyte
shub schedule jumia  # runs the spider on Zyte cloud
```

---

## 8. Useful Settings (settings.py)

```python
# Be polite — don't hammer the server
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True

# Respect robots.txt (set False only if you have permission)
ROBOTSTXT_OBEY = True

# Concurrent requests
CONCURRENT_REQUESTS = 8

# User agent (identify yourself)
USER_AGENT = "Mozilla/5.0 (compatible; MyBot/1.0)"
```

---

## 9. Common Commands Cheatsheet

| Command | Description |
|---|---|
| `scrapy startproject name` | Create new project |
| `scrapy genspider name domain` | Generate spider |
| `scrapy crawl name` | Run spider |
| `scrapy crawl name -o out.json` | Run and export JSON |
| `scrapy crawl name -o out.csv` | Run and export CSV |
| `scrapy shell "url"` | Interactive selector testing |
| `shub login` | Login to Zyte |
| `shub deploy` | Deploy to Zyte cloud |
| `shub schedule name` | Run spider on Zyte |

---

## 10. Freelance Use Cases

- **Price monitoring** — track competitor/e-commerce prices daily
- **Lead generation** — scrape business directories for contact info
- **Market research** — aggregate product listings across multiple sites
- **Job boards** — scrape listings for clients or personal projects
- **Real estate** — property listings and price trends

> Tip: Wrap finished spiders in a FastAPI endpoint + scheduler for a higher-ticket productized service.