import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", 
	params={"key": "5Yj35OGg7eRyZrvRn0Zg", "isbns": "9781632168146"})
print(res.json())