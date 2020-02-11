# pYneWs V1.0
Get the latest news with this python script.


# What is pYneWs?
pYneWs is a full python application which is using an API to request all news related to your search.    
 output example:    
     
    Unpatched Citrix vulnerability now exploited, patch weeks away    
    https://arstechnica.com/information-technology/2020/01/unpatched-citrix-vulnerability-now-exploited-patch-weeks-away/    
    2020-01-13T20:31:37Z    
    
This script is powered by NewsAPI.org!
There is no specific use, so enjoy doing anything you want to use it for.

<b>Make sure if you use the application for your business that you change to API key to your own!</b>


# how to use?
pYneWs is very easy to use.

- when you execute the file pYneWs asks for what you want to search, you can simply use a word or a sentence.
- after that you are asked for what exact news you want about the subject, this can be headline or everything.
- at last the script asks how you want to sort the news, this can be on date, popularity or revelant.

# how to change the API key?
If you want to use the script to make your own or if you want to use this script for your business you have to change the API key to your own.
you can change the API key at this line:

      newsJson = requests.get("https://newsapi.org/v2/" + headers + "?q=" + cat + "&sortBy=" + sorting + "&apiKey=<b>ceb21cd319bf4f9f9d18bc043df7a6c6<b>")
You can get an API key at newsapi.org, just right for your needs.

# why pYneWs?
honestly I don't know why, I just thought of a easier way to search news without first opening the web browser.

<b>If you have any ideas for another project mail me at: yeetmail09@gmail.com (I am also available for any improvement options)</b>
 
