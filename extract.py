import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Initialize WebDriver
service = Service(executable_path="chromedriver.exe")  # Path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # AliExpress URL
    url = "https://www.amazon.com/s?k=gaming&_encoding=UTF8&content-id=amzn1.sym.860dbf94-9f09-4ada-8615-32eb5ada253a&pd_rd_r=8cf6e442-63ff-4a05-bed1-90a37928de0b&pd_rd_w=Xllym&pd_rd_wg=MxVTH&pf_rd_p=860dbf94-9f09-4ada-8615-32eb5ada253a&pf_rd_r=W1AAB5YZZZG6X1GV2XHF&ref=pd_hp_d_atf_unk"
    driver.get(url)

    # Wait for the page to load (explicit wait)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.sg-col-inner"))
    )

    # Extract the HTML source
    html = driver.page_source

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Initialize a list to store the product data
    products = []

    # Extract product details
    for product in soup.find_all("div", class_="sg-col-inner"):
        try:
            # Product name
            name_element = product.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
            name = name_element.text.strip() if name_element else "N/A"

            # Product price
            price_element = product.find("span", class_="a-price-whole")
            price = price_element.text.strip() if price_element else "N/A"

            # Sold units (reviews)
            review_element = product.find("span", class_="a-size-base s-underline-text")
            review = review_element.text.strip() if review_element else "N/A"

            # Append the data to the list
            products.append({
                "Product Name": name,
                "Price": price,
                "Reviews": review
            })
        except AttributeError:
            # Skip if any element is not found
            continue

    # Convert to DataFrame
    df = pd.DataFrame(products)

    # Save to CSV file
    csv_filename = "amazon1.csv"
    df.to_csv(csv_filename, index=False, encoding="utf-8")

    print(f"Data successfully saved to {csv_filename}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")