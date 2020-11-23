import os
import unittest

#On importe app depuis flaskapp.py
from flaskapp import app
from redis import Redis

class CounterTest(unittest.TestCase):

    def setUp(self):
        self.app=app.test_client()
        #procure des méthodes



    def tearDown(self):
        pass

#Définitions des tests

    #test1
    def test_welcome_page(self):
        #make a get request on path '/'
        response=self.app.get('/')
        self.assertEqual(response.status_code, 200)

    #test2
    def test_redis_connection(self):
        #connecte au redis server
        redis=Redis(host="redis-server", db=0)
        self.app.get('/visit')
        self.app.get('/visit')
        self.app.get('/visit')
        self.assertEqual(int(redis.get("counter")), 3)
        
        
if __name__ == "__main__":
    unittest.main()