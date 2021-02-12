import praw
import pandas as pand
import datetime as dt

reddit = praw.Reddit(
    client_id="redacted",
    client_secret="redacted",
    user_agent="Scrape"
)