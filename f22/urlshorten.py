import aerospike
import random
import sys

config = {
  'hosts': [ ('127.0.0.1', 3000) ]
}

try:
  client = aerospike.client(config).connect()
except:
  print("failed to connect to the cluster with", config['hosts'])
  sys.exit(1)

class ShortenURL:
	_charmap = '123456789abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ-_'
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
		key=('test','por',sid)	
		(key, meta) = client.exists(key)
		if meta == None:
			return True
		return False
	def inserturl(self,url):
		sid=(random.randint(100000,999999))
		if self.checkexists(sid):
			key=('test','por',sid)		
		
			try:
				# Write a record
				client.put(key, {
				str(sid): url
 					})
			except Exception as e:
				print("error: {0}".format(e), file=sys.stderr)
			return sid		
		else:
			sid=(random.randint(100000,999999))			
			inserturl(self,url)
		
	def getoriurl(self,shortenedurl):
		sid=self.createsid(shortenedurl)
		key=('test','por',sid)
		try:
			(key, metadata, record) = client.get(key)
			return record[str(sid)]	 
		except:
			return 'No Record exist for given short url'
      


