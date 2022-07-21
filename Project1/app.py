import time 
import redis 
import flask 

app = flask.Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 10
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    print('Hello World! I have been seen {} times.\n'.format(count))
    print("Hi. My name is Joseph Jefries and I am learning DevOps")
    print("createdBy = joshuajosephjefries")
