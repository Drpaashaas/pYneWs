import requests
import json
import time
import os
from sys import platform
sleep = time.sleep


class newsApi():

    # def __init__(self):
        # self.apiKey
        # self.headers
        # self.cat
        # self.sortType
        # self.newsApiJsonData

    def apiKey(self, apikey):
    	self.apiKey = apikey

    def varValue(self):
    	self.cat = input("News articles about: ")
    	head = input("Headlines or Everything | h/e: ")
    	self.headers = self.headVal(head)
    	sort = input("Sort on d/date| p/popularity| n/nothing: ")
    	self.sortType = self.sortVal(sort)

    def createJson(self):
        self.newsApiJsonData = requests.get("https://newsapi.org/v2/" + str(self.headers) + "?q=" + str(self.cat) + self.sortType + self.apiKey)

    def headVal(self, head):
    	if head == "h" or head == "H":
    		return "top-headlines"
    	else:
    		return "everything"

    def sortVal(self, sort):
    	if sort == "d" or sort == "D":
    		return "&sortBy=publishedAt"
    	elif sort == "p" or sort == "P":
    		return "&sortBy=popularity"
    	else:
    		return "&sortBy="

    def readArticles(self):
    	if self.newsApiJsonData.status_code == 200:
    		articles = self.newsApiJsonData.json()["articles"]

    		if not articles:
    			empty()
    			if self.headers == "top-headlines":
    				print("We could not find headline articles about " + self.cat)
    			else:
    				print("We could not find news articles about " + self.cat)

    		else:
    			i = 0
    			for article in articles:
    				i += 1
    				empty()
    				empty()
    				print('\033[1m' + article['title'] + '\033[0m')
    				print(article['publishedAt'])
    				print(article['url'])
    				if i == 3:
    					empty()
    					input("press any key to continue searching...")
    					clear()
    					i = 0

    			sleep(1)
    			empty()
    			print("No more articles found.")
    			input("press any key to continue...")
    	else:
    		print("connection error: ", self.newsApiJsonData.status_code)

    	stop()

    				

def empty():
	print("")

def stop():
	empty()
	j = input("do you want to continue? y/n: ")
	if j == "y" or j == "Y":
		start()
	else:
		exit()

def clear():
	if platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def start():
	
	clear()

	empty()
	print("Welcome to pYneWs V1.1")
	empty()
	
	ji = input("Do you have your own newsApi key? y/n: ")
	
	if ji == "y" or ji == "Y":
		key = input("copy your api key here: ")
		apikey = "&apiKey=" + key
	else:
		apikey = "&apiKey=ceb21cd319bf4f9f9d18bc043df7a6c6"

	newsApiSearch = newsApi()
	newsApiSearch.apiKey(apikey)
	newsApiSearch.varValue()
	newsApiSearch.createJson()
	newsApiSearch.readArticles()

start()