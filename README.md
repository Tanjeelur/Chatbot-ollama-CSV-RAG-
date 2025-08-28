
# Chatbot-ollama-CSV-RAG

## Overview

This project combines web scraping, data processing, and AI-powered conversational search to create a Retrieval-Augmented Generation (RAG) chatbot. The system scrapes product data from Amazon, stores it in CSV format, and enables users to interact with the data using natural language queries. The chatbot leverages the Ollama language model and semantic search to provide relevant, data-driven answers.

## Features

- **Amazon Product Scraping**: Uses Selenium and BeautifulSoup to extract product names, prices, and reviews from Amazon search results.
- **Data Storage**: Saves extracted product data into CSV files for further analysis and chatbot use.
- **Conversational RAG Chatbot**: Answers user questions by retrieving relevant product data and generating responses using Ollama's LLM.
- **Semantic Search**: Employs Sentence Transformers and cosine similarity to match user queries with the most relevant product entries.
- **Extensible Web Automation**: Includes a sample script for scraping other websites (e.g., Wikipedia) using Selenium.

## Project Structure

```
.
├── amazon.csv / amazon1.csv      # Scraped product data
├── chromedriver.exe              # ChromeDriver for Selenium
├── extract.py                    # Amazon data scraping script
├── main.py                       # RAG chatbot implementation
├── webdriver.py                  # Example Selenium script
├── requirment.txt                # Python dependencies
├── pyvenv.cfg                    # Python virtual environment config
├── README.md                     # Project documentation
```

## Installation

### Prerequisites

- Python 3.8 or higher (recommended: 3.11+)
- Google Chrome browser
- Matching version of ChromeDriver (`chromedriver.exe`)
- [Ollama](https://ollama.com/) installed and running locally

### Setup Steps

1. **Clone the repository**
   ```powershell
   git clone https://github.com/Tanjeelur/Chatbot-ollama-CSV-RAG-.git
   cd Chatbot-ollama-CSV-RAG-
   ```

2. **Create and activate a virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirment.txt
   ```

4. **Download ChromeDriver**
   - Place `chromedriver.exe` in the project root.
   - Ensure the version matches your installed Chrome browser.

## Usage

### 1. Scrape Amazon Product Data

Run the scraping script to extract product information and save it to `amazon1.csv`:
```powershell
python extract.py
```

### 2. Start the Chatbot

Interact with the CSV data using the RAG chatbot:
```powershell
python main.py
```
- Type your questions about the products.
- Type `exit` to quit the chatbot.

### 3. Example Web Scraping (Optional)

Test web automation with the sample script:
```powershell
python webdriver.py
```

## How It Works

- **extract.py**: Automates a browser session to Amazon, waits for product listings to load, parses the HTML, and extracts product details into a CSV file.
- **main.py**: Loads the CSV, generates text embeddings for each product, retrieves the most relevant entries for a user query, and uses Ollama to generate a context-aware response.
- **webdriver.py**: Demonstrates basic Selenium usage for scraping other sites.

## Dependencies

All required Python packages are listed in `requirment.txt`:
- `selenium`
- `pandas`
- `beautifulsoup4`
- `ollama`
- `sentence-transformers`
- `transformers`
- `torch`
- `scikit-learn`

Install them with:
```powershell
pip install -r requirment.txt
```

## Customization

- To scrape different Amazon categories, modify the URL in `extract.py`.
- To use other CSV files, update the path in `main.py`.
- Extend the chatbot logic or scraping scripts as needed for your use case.

## License

This project is provided for educational and research purposes. Please review Amazon's terms of service before scraping their website.

## Author

Developed by Tanjeelur.
