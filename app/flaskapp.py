from flask import Flask
from redis import Redis, RedisError
import socket


#connect to redis-server
redis = Redis(host="redis-server", db=0)
#redis-server est le nom du serveur, mieux que adresse IP

#create a new flaskapp instance
app = Flask(__name__)

#functions to trigger when a client goes to /<path>

@app.route("/")
def index():
    return "<h1> Bienvenue sur mon site jeune entrepeneur ! </h1>"

@app.route("/visit")
def counter_incr():
    try:
        visits=redis.incr("counter")
    except:
        visits="<i> Erreur !!! </i>"

    html="<h1> Number of visits : {} </h1>".format(visits)
    return html

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=80)