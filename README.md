# 🕸️ Remote Job Listings Scraper with Selenium

This is Project 2 of my technical portfolio as a **Backend Developer**, focused on **web scraping and Python automation**.

The goal is to demonstrate proficiency in scraping **JavaScript-rendered, dynamic websites** using `Selenium`, and handling data cleanly using `pandas` and `json`.


## 🎯 Objective

Automatically extract remote job listings from [RemoteOK](https://remoteok.com), collecting the following information:

- Job title
- Company
- Location
- Job link
- Tags (e.g., Python, Backend, Remote)
- Publication date (formatted as `dd-mm-yyyy / hh:mm`)


## 🧰 Tech Stack

- `Python 3`
- `Selenium` (with `webdriver-manager`)
- `pandas`
- `json`
- `datetime`


## ⚙️ Features

- Headless browser automation using Selenium
- Dynamic element extraction (JavaScript-rendered content)
- Waits for page content using `time.sleep`
- Handles missing or optional data gracefully
- Exports data to:
  - `jobs.json`
  - `jobs.csv`
- Clean and well-commented code, ready for reuse


## 📁 Project Structure
```json
job_scraper_selenium/
├── scraper.py
├── requirements.txt
├── jobs.json
├── jobs.csv
└── README.md
```


## ▶️ How to Run

1. Clone the repository:

- git clone https://github.com/Gustavix320/job_scraper_selenium.git
- cd job_scraper_selenium

2. (Optional) Create and activate a virtual environment:
- python -m venv venv
  
- Windows:
- venv\Scripts\activate
  
- macOS/Linux:
- source venv/bin/activate


3. Install dependencies:
- pip install -r requirements.txt


4. Run the scraper:
- python scraper.py


5. Output files:
- jobs.json: structured job data
- jobs.csv: tabular format (e.g., for Excel or analysis)

## 📸 Example Output (JSON)

```json
{
  "titulo": "Backend Developer @ lobstr.io Python Scraping Celery",
  "empresa": "lobstr.io",
  "local": "🌍 Worldwide",
  "link": "https://remoteok.com/remote-jobs/remote-backend-developer-lobstr-io-python-scraping-celery",
  "tags": ["Python", "Backend", "Developer"],
  "data_publicacao": "11-07-2025 / 14:43"
}
```

## 👨‍💻 Author

**Gustavo Santos**  
📍 Backend Developer | Python Web Scraper  
🔗 [LinkedIn](https://www.linkedin.com/in/gustavo-santos-502364338/)  
💻 [GitHub](https://github.com/Gustavix320)



