# Swiss Automotive Trade Association Scraper
## Overview
This repository contains two Python scripts, scrape_agvs.py and scrape_mails.py, developed to scrape data from the Swiss Automotive Trade Association (AGVS) using BeautifulSoup. These tools are designed to identify most Swiss car dealerships and obtain their website URLs. Additionally, scrape_mails.py is aimed at extracting employee details, including email addresses, from these dealership websites.

## Key Features
* **Member Identification**: scrape_agvs.py efficiently identifies members of the Swiss Automotive Trade Association, providing a comprehensive list of car dealerships in Switzerland.
* **Website URL Extraction**: Along with dealership identification, the script also scrapes the website URLs of these businesses.
* **Email Scraping**: scrape_mails.py takes this a step further by attempting to scrape employee contact information, specifically email addresses, from the identified websites.

## Use Cases
* **Market Research**: Ideal for conducting market research within the Swiss automotive sector.
* **Networking and Outreach**: Useful for professionals looking to network with or reach out to car dealerships in Switzerland.
* **Data Collection**: Beneficial for data analysts and marketers who require up-to-date information on Swiss car dealerships.

## Getting Started

### Prerequisites
1. Clone the repo
   `git clone https://github.com/ricilandolt/agvs_scraper.git`
2. Create virtual environment
  `python -m venv .venv`
3. Install dependcies
  `pip install -r requirements.txt`
