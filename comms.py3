import base64, requests, praw
from Judgement import Judgement

reddit = praw.Reddit(user_agent='sentinel');
all = reddit.subreddit("all")
judgements = []
for i in all.search("pepsi", limit=10):
    judgements.append(Judgement("REDDIT", i.id, i.title + ' ' + i.selftext, i.ups, i.upvote_ratio))
for i in judgements:
	print(i.toJson())