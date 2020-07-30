import twint
import csv
from flask import Flask, jsonify, request


def convertData(x):
    return {'avi': x.avatar, 'followers:': x.followers, 'username': x.username}
def convertTweet(x):
    return {'link': x.link, 'tweet': x.tweet, 'username': x.username}


f = open('badterms.csv')
tmpArray = []
data = []
csv_f = csv.reader(f)

app = Flask(__name__)

for row in csv_f:
    tmpArray = row


@app.route('/u/<username>')
def show_user_avatar(username):
    c = twint.Config()
    c.Username = username
    c.User_full = True
    c.Store_object = True

    twint.run.Lookup(c)
    users = twint.output.users_list
    
    tweetsMap = list(map(convertData, users))
    data.clear()
    return jsonify(tweetsMap)


@app.route('/t/<username>')
def show_user_profile(username):
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
    data.clear()
    return jsonify(tweetsMap)
