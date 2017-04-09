import redis
import random
import sys


try:
  redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
except:
  print("failed to connect to the host")
  sys.exit(1)

class ShortenURL:
	_charmap = '123456789abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ'
	_base = len(_charmap)
	def createurl(self, sid):
		string = ''
		while(sid > 0):
			string = self._charmap[sid % self._base] + string
			sid //= self._base
		return string

	def createsid(self, shortenedurl):
		number = 0
		for char in shortenedurl:
			number = number * self._base + self._charmap.index(char)
		return number
	def checkexists(self,sid):
		if redis_db.exists(sid):
			return True
		return False
	def inserturl(self,url):
		sid=(random.randint(100000,999999999))
		if self.checkexists(sid):
			sid=(random.randint(100000,999999999))
			inserturl(self,url)		
		else:
			try:
				# Write a record
				redis_db.set(sid,url)
			except Exception as e:
				print("error: {0}".format(e), file=sys.stderr)
			return sid	
		
	def getoriurl(self,shortenedurl):
		sid=self.createsid(shortenedurl)
		if self.checkexists(sid):
		      return redis_db.get(sid).decode()
		else:
			return 'No Record exist for given short url'
