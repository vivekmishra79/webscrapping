
import requests
from bs4 import BeautifulSoup
from mysql.connector  import MySQLConnection


url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


quotes_data = []
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    quotes_data.append((text, author))


    connection = MySQLConnection(
        host="localhost",        
        user="root",             
        password="vivek",  
        database="new"   
    )
    cursor = connection.cursor()

 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        quote TEXT,
        author VARCHAR(255)
    )
    """)
 
    cursor.executemany("INSERT INTO quotes (quote, author) VALUES (%s, %s)", quotes_data)
    connection.commit()

    print(f"{cursor.rowcount} records inserted successfully!")

cursor.close()
connection.close()


    
