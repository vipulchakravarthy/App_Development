import requests

Database_URI="postgres://anpezerezyqqnz:673ff332c1d79a7474b4cb9a542323f31de227cda1f02da75c39ea9b81b0c18f@ec2-54-197-48-79.compute-1.amazonaws.com:5432/ddl9v3a552vett"
res = requests.get("https://www.goodreads.com/book/review_counts.json", 
	params={"key": "5Yj35OGg7eRyZrvRn0Zg", "isbns": "9781632168146"})
print(res.json())
