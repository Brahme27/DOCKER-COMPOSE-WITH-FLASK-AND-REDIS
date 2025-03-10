import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

def get_refresh_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')  # Increment Redis key "hits"
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_refresh_count()
    return f'Hello! This page has been refreshed {count} times.\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

