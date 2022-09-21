import requests
import random
import argparse
import threading
import time


red='\033[31m'
green='\033[92m'

class Args:
	def __init__(self):
		argu=argparse.ArgumentParser(description="paramas for sending traffics")
		argu.add_argument("--pages",dest="pages",help="file of pages to send traffics [ must be txt]")
		argu.add_argument("--url",default=None,dest="url",help="for single url to send traffics")
		argu.add_argument("--at",dest="amount",help="amount of traffic to send per page",default=100,type=int)


		self.allargs=argu.parse_args()

	def pages(self):
		return self.allargs.pages

	def url(self):
		return self.allargs.url

	def amount(self):
		return self.allargs.amount

class Traffic(Args):
	def site(self):
		return open(self.pages(),"r")
		
	def amountTraffic(self):
		return self.amount()
	def singleurl(self):
		return self.url()

	def useragent(self):
		return open("useragent.txt",'r').readlines()


	def start(self):
		site=self.site().readlines()
		amount=self.amountTraffic()
		url=self.singleurl()
		user=self.useragent()

		number=0
		num=open("number.txt","w")

		for i in range(amount):
			us=random.choice(user)
			br=us.replace("\n","")
			
			sit=random.choice(site)
			s=sit.replace("\n","")
			print(red+'Sending Request...')
			req=requests.get(s,headers={'User-Agent':br})
			print(green+"Respond Code: ",req.status_code)
			number +=1
		num.write(str(number))


class MultiTraffic:
	def __init__(self,targets):
		self.targets=targets

	def thread(self):
		self.targets()

	def run(self):
		t=threading.Thread(target=self.thread)
		t.start()
		self.thread()

		

		


run=Traffic()

app=MultiTraffic(run.start)
app.run()




