import twint
import csv
from flask import Flask, jsonify, request

def convertTweet(x):
    return {'link':x.link, 'tweet': x.tweet, 'username': x.username}


f = open('badterms.csv')
tmpArray = []
csv_f = csv.reader(f)

app = Flask(__name__)

for row in csv_f:
    tmpArray = row

@app.route('/t/<username>')
def show_user_profile(username):
    # show the user profile for that user
    data = []
    for word in tmpArray:
        c = twint.Config()
        c.Limit = 10
        c.Username = username
        c.Translate = True
        c.Search = word
        c.Store_object = True
        twint.run.Search(c)
        data = twint.output.tweets_list

    tweetsMap = list(map(convertTweet, data))

    return jsonify(tweetsMap)

   



