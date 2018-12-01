#coding:utf-8
import requests

class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:
			res = requests.post(url=url,data = data,headers= header).json()
		else:
			res = requests.post(url=url,data = data).json()
		return res

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.get(url=url,data = data,headers= header).json()
		else:
			res = requests.get(url=url,data = data).json()
		return res

	def runmain(self,method,url,data=None,header=None):
		res = None
		if method == 'post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return res

