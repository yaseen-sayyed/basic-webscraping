import requests
from bs4 import BeautifulSoup

search = input("Enter search term: ")
params = {'q': search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify())
results = soup.find("ol", {"id": "b_results"})
links = results.find_all("li", {'class': 'b_algo'})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

        children = item.find("h2")
        print("Next sibling:", children.next_sibling)
