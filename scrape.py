import requests
from bs4 import BeautifulSoup
import csv


response = requests.get('https://www.bbc.com/').text
soup = BeautifulSoup(response, "lxml")
csv_file = open('data.csv.', 'w')
writer = csv.writer(csv_file)
writer.writerow(["Url", "Title", "Source"])

new_div = soup.find("section", class_="module--news")
div_content = new_div.find("div", class_="module__content")
div_content2 = div_content.find_all("div", class_="media__content")
#print(div_content2.prettify())


for elm in div_content2 :
    url = elm.h3.a.text
    title = elm.p.text
    source = elm.findAll('a')[1].text

    print("Url : ", url.strip())
    print("Title : ", title.strip())
    print("Source : ", source.strip())

    print()
    writer.writerow([url, title, source])
    csv_file.close 
