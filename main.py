import re
from bs4 import BeautifulSoup
import requests
import os

# Read the URLs from the file
with open("all_vietanhsongngu_links.txt", "r", encoding='utf-8') as file:
    urls = file.read().splitlines()

# Loop through each URL and process it
for url in urls:
    # Extract the title from the URL
    title = url.split('/')[-1]  # This gets the last part of the URL
    file_name = title.replace('.htm', '')  # Remove the file extension if present

    # Perform an HTTP GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the request with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize content holders
        english_content = "English:\n"
        vietnamese_content = "\nVietnamese:\n"

        for element in soup.find_all('span', style="font-size:14px"):
            if "font-family:Calibri" not in element.get('style', ''):
                text = element.text.strip()

                # Skip unwanted lines
                if "Theo:" in text or "Content Writer:" in text:
                    continue

                # Use a regular expression pattern to identify Vietnamese characters
                if re.search(r'[À-ỹ]', text):
                    vietnamese_content += f"{text}\n"
                else:
                    english_content += f"{text}\n"

        # Ensure the directory exists
        os.makedirs('article_translation', exist_ok=True)

        # Open a file for writing both language versions in the same file
        with open(f'article_translation/{file_name}_translation.txt', 'w', encoding='utf-8') as file:
            # Write the content in the specified format
            file.write(english_content + vietnamese_content)
    else:
        print(f'Failed to retrieve the webpage for {url}')