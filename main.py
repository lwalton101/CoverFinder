from your_api_client import Client

client = Client(base_url="https://api.example.com", token="YOUR_TOKEN")

response = client.books.get_book.sync(book_id=123)

print(response.title)
