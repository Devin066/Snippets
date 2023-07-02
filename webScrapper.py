import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com'

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements on the page using their HTML tags or CSS selectors
# For example, let's find all the links on the page
links = soup.find_all('a')

# Print the href attribute of each link
for link in links:
    print(link.get('href'))
