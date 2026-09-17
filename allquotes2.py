import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "https://quotes.toscrape.com/page/10/"
quotes_data = []
author_data = []

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.select("span.text")
    author = soup.select("small.author")

    for i in quotes:
        quotes_data.append(i.text)

    for i in author:
        author_data.append(i.text)


    next_btn = soup.select_one(".previous a")
    if next_btn == None:
        break

    url = urljoin(url, next_btn.get("href"))
    print(url)

data = {
    "AuthorName" : author_data,
    "Quotes" : quotes_data
}

df = pd.DataFrame(data)
print(df)

df.to_csv("allquotes2.csv", index=False)