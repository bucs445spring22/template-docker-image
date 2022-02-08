import requests

result = requests.get("https://opentdb.com/api.php?amount=10")
print(result.json())