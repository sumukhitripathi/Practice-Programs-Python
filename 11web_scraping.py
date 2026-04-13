#Web Scraping
#Extract data from user and store in database

import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://webscraper.io/test-sites/e-commerce/allinone'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('p')    #Extract all paragraph tags
else:    
    print(f'Failed to retrieve data from {url}. Status code: {response.status_code}')

#Store data in database
conn = sqlite3.connect('web_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS scraped_data (id INTEGER PRIMARY KEY, content TEXT)''')
for item in data:
    c.execute("INSERT INTO scraped_data (content) VALUES (?)", (item.text,))
conn.commit()

#Retrieve and display data from database
conn = sqlite3.connect('web_data.db')
c = conn.cursor()
c.execute("SELECT * FROM scraped_data")
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()