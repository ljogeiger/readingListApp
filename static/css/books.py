import requests

url = "https://www.googleapis.com/books/v1/volumes?q=Treasure%20Island"

response = requests.get(url)
response_dict = response.json()


print(response_dict["items"][1]["volumeInfo"]["authors"])


