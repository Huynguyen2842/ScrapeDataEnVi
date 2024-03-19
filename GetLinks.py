from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Function to scrape a single page
def scrape_page(url):
    # Open the page
    driver.get(url)

    # Wait for the dynamic content to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "penci-image-holder"))
    )

    # Scroll to ensure dynamic content loads, adjust as needed.
    for i in range(12):  # Adjust based on the actual page
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # Adjust timing as needed

    # Get the page source
    page_source = driver.page_source

    # Use BeautifulSoup to parse the loaded page source
    soup = BeautifulSoup(page_source, "html.parser")

    # Initialize a set to store unique article links
    article_links = set()

    # Find all 'a' tags with the specified class and filter by href attribute
    for a in soup.find_all("a", class_="penci-image-holder penci-lazy"):
        href = a.get("href")
        if href and not href.startswith("https://vietanhsongngu.com/course"):       
            article_links.add(href)

    return article_links

# Load the links from the text file
with open("links.txt", "r", encoding="utf-8") as file:
    urls = file.read().splitlines()

# Initialize a set to store all unique article links
all_article_links = set()

# Loop through each URL and scrape the articles
for url in urls:
    try:
        article_links = scrape_page(url)
        all_article_links.update(article_links)
        print(f"Scraped {len(article_links)} links from {url}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Close the driver after scraping all pages
driver.quit()

# Save the article links to a text file
with open("all_vietanhsongngu_links.txt", "w", encoding="utf-8") as file:
    for article_link in all_article_links:
        file.write(f"{article_link}\n")

print(f"Successfully saved {len(all_article_links)} unique links to all_vietanhsongngu_links.txt")
