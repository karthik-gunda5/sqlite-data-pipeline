import requests

url = "https://fakerapi.it/api/v1/books?_quantity=5"
response = requests.get(url)

books = response.json()["data"]

for book in books:
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Published:", book["published"])
    print("-" * 30)
