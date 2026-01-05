from bs4 import BeautifulSoup
import pandas as pd

with open("../dataset.html", "r", encoding="utf-8") as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, "html.parser")

table = soup.find("table")

headers = [th.text.strip() for th in table.find_all("th")]


rows = []
for tr in table.find_all("tr")[1:]:
    rows.append([td.text.strip() for td in tr.find_all("td")])


df = pd.DataFrame(rows, columns=headers)


df.to_csv("addiction_data.csv", index=False)

print("Scraping completed successfully")
