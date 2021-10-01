import requests as rq
try:
	top_all = rq.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()
	print("Hacker News: Top 25")
	print("====================================", "\n")
	for i in range(1, 26):
		string = "https://hacker-news.firebaseio.com/v0/item/"+str(top_all[i])+".json?print=pretty"
		story = rq.get(string).json()
		print(i, ": ", story["title"], "(", story["type"], ")", sep='')
		print("----------------------")
		print(story["url"], "\n")
except:
	print("An unexpected error ocurred")
