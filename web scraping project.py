import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('scraped_data.db')
c = conn.cursor()

# Create a table to store the scraped data
c.execute('CREATE TABLE IF NOT EXISTS articles (title TEXT, author TEXT, date TEXT, content TEXT)')

# Specify the URL to be scraped
url = 'https://www.example.com/articles'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the articles on the page
articles = soup.find_all('article')

# Loop through the articles and extract the information
for article in articles:
    # Extract the title, author, date, and content of the article
    title = article.find('h2').text.strip()
    author = article.find('p', class_='author').text.strip()
    date = article.find('p', class_='date').text.strip()
    content = article.find('div', class_='content').text.strip()
    
    # Insert the information into the database
    c.execute('INSERT INTO articles (title, author, date, content) VALUES (?, ?, ?, ?)', (title, author, date, content))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
