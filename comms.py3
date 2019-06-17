import base64, requests, praw

# secret secret shhhhhhhhhh
encoded = base64.b64encode(b'sTyk33T5di492w:V28bZx4eFhR5BvztuLWsfR1wltk')

payload = {'grant_type':'client_credentials'}
authHeader = 'Basic ' + encoded.decode('utf-8')
header = {'Authorization': authHeader, 'Content-Type': 'application/x-www-form-urlencoded', 'User-agent': 'sentinel'}
r = requests.post('https://www.reddit.com/api/v1/access_token', headers=header, data=payload)
print(r.text)

reddit = praw.Reddit(user_agent='sentinel');
for submission in reddit.front.hot():
    print(submission.selftext)