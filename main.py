import praw
import pandas as pand
import datetime as dt

reddit = praw.Reddit(
    client_id="redacted",
    client_secret="redacted",
    user_agent="Scrape"
)

inputSub = input()
if inputSub == '' or ' ':
    inputSub = 'all'
sub = reddit.subreddit(inputSub)

postDict = {
    "title": [], "url": [], "body": []
}

for post in sub.hot(limit=10):
    postDict["title"].append(post.title)
    postDict["url"].append(post.url)
    postDict["body"].append(post.selftext)

postData = pand.DataFrame(postDict)
print(postData)
postData.to_csv('test.csv', index=False)