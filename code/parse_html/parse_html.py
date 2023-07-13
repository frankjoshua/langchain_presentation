import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Fetch the HTML content of the initial page
url = "https://wiki.monai.art"  # Replace with the URL of the website you want to scrape
response = requests.get(url)
html_content = response.text

# Create a Beautiful Soup object
soup = BeautifulSoup(html_content, "html.parser")

# Extract links from the initial page
links = soup.find_all("a")

# List to store the extracted content
content_list = []

# Follow each link and extract content from each page
for link in links:
    # Get the URL of the linked page
    link_url = link.get("href")
    
    # Handle relative URLs by joining with the base URL
    absolute_url = urljoin(url, link_url)
    print(absolute_url)
    
    # Fetch the HTML content of the linked page
    linked_response = requests.get(absolute_url)
    linked_html_content = linked_response.text
    
    # Create a Beautiful Soup object for the linked page
    linked_soup = BeautifulSoup(linked_html_content, "html.parser")
    
    # # Extract the desired content from the linked page
    # # Example: Extract the paragraph content
    # paragraphs = linked_soup.find_all("figure.table table tr td p")
    # content = "\n".join(paragraph.text for paragraph in paragraphs)
    # for paragraph in paragraphs:
    #     print(paragraph.text)
    
    # Add the extracted content to the content_list
    content_list.append(linked_soup.get_text())

# Write the extracted content to a document
with open("scraped_content.txt", "w") as file:
    for content in content_list:
        file.write(content + "\n")

print("Scraping completed and content saved to 'scraped_content.txt'.")
