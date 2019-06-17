import base64, requests, praw



reddit = praw.Reddit(user_agent='sentinel');
for submission in reddit.front.hot():
    print(submission.selftext)