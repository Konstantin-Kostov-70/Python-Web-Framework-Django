import csv
import requests
from bs4 import BeautifulSoup

response = requests.get("https://bilki.bg")
soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("article")

data = []
for article in articles:
    title = article.find("h2").text.strip()
    author = article.find("span", class_="author").text.strip()
    date = article.find("span", class_="date").text.strip()
    content = article.find("div", class_="content").text.strip()

    # data.append([title, author, date, content])
    data.append(article)

with open("articles.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Author", "Date", "Content"])  # Write header row
    writer.writerows(data)  # Write data rows
