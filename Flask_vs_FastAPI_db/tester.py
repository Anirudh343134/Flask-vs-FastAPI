from random import randint
from time import time
import requests
from statistics import mean

def test(url, rank):
    start = time()
    res = requests.get(url + str(rank))
    end = time()
    diff = end - start
    return diff


tests = 7500

url_fastapi = 'http://127.0.0.1:8000/'
url_flask = 'http://127.0.0.1:5000/'

delays_fastapi, delays_flask = [], []

for i in range(0, tests):
    if i%100 == 0:
        print('Running test #' + str(i) + '\n')
    id = randint(1, 200001)
    delta = test(url_fastapi, id)
    delays_fastapi += [delta]
    id1 = randint(1, 200001)
    delta1 = test(url_flask, id1)
    delays_flask += [delta1]

highest_flask = max(delays_flask)
lowest_flask = min(delays_flask)
average_flask = mean(delays_flask)

highest_fastapi = max(delays_fastapi)
lowest_fastapi = min(delays_fastapi)
average_fastapi = mean(delays_fastapi)

if average_fastapi < average_flask:
    faster = 'FastAPI'
    percent = (average_flask - average_fastapi)*100/average_flask
else:
    faster = 'Flask'
    percent = (average_fastapi- average_flask)*100/average_fastapi


f = open('results.txt', 'a')
f.write('The highest Flask delay was '+ str(highest_flask))
f.write('\nThe lowest Flask delay was ' + str(lowest_flask))
f.write('\nThe average Flask delay was ' + str(average_flask))
f.write('\nThe highest FastAPI delay was '+ str(highest_fastapi))
f.write('\nThe lowest FastAPI delay was ' + str(lowest_fastapi))
f.write('\nThe average FastAPI delay was ' + str(average_fastapi))

f.write('\nOn average, ' + faster + ' was ' + str(percent) + ' percent faster')

f.close()