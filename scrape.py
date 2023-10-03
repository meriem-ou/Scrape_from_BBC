import requests
from bs4 import BeautifulSoup
import json


def scrap():
    scraped_data = []
    response = requests.get('https://www.bbc.com/')
    soup = BeautifulSoup(response.text, "html.parser")
    
    for elm in soup.find_all('a', class_="media__link", rev="news|headline"):
        scraped_data.append(
                {
                    
                    "title": elm.text.replace('\n', ''),
                    "link": elm.get("href")
                }
            )
        

    print(json.dumps(scraped_data, indent=2))

scrap()    
