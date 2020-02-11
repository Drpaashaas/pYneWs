import requests
import json
import time
sleep = time.sleep

print("")
print("Thanks for using my news application! pYneWs V1.0")
print("")
cat = input("What news you want to read? : ")
head = input("Headlines only or everything? h/e: ")
sort = input("Sort on date, popularity or nothing? d/p/n: ")

if head == "h" or head == "H" or head == "head" or head == "Head":
    headers = "top-headlines"
else:
    headers = "everything"

if sort == "d" or sort == "D" or sort == "date" or sort == "Date":
    sorting = "publishedAt"
if sort == "p" or sort == "P" or sort == "popularity" or sort == "Popularity":
    sorting = "popularity"
else:
    sorting = ""


newsJson = requests.get("https://newsapi.org/v2/" + headers + "?q=" + cat + "&sortBy=" + sorting + "&apiKey=ceb21cd319bf4f9f9d18bc043df7a6c6")

if newsJson.status_code == 200:

    articles = newsJson.json()["articles"]

    if not articles:
        print("")
        if headers == "top-headlines":
            print("Sorry, there is no headline information about", cat + ". Try to search on everything instead of headlines.")

    else:
        i = 0
        for article in articles:
            i = i + 1
            print("")
            print(article['title'])
            print(article['url'])
            print(article['publishedAt'])
            sleep(1)
            if i == 5:
                print("")
                input("press enter to continue..")
            if i == 10:
                print("")
                input("press enter to continue..")
            if i == 15:
                print("")
                input("press enter to continue..")
            if i == 20:
                print("")
                input("press enter to continue..")
            if i == 25:
                print("")
                input("press enter to continue..")
            if i == 30:
                print("")
                input("press enter to continue..")
            if i == 35:
                print("")
                input("press enter to continue..")

        sleep(2)
        print("")
        print("Please leave a donation at: https://something.com/donate")
        print("")
        input("press enter to leave...")

else:
    print("Sorry, something went wrong with the connection. error:", newsJson.status_code)

