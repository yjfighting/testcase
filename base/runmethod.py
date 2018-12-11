#coding:utf-8
import requests
import json
#from requests_toolbelt import MultipartEncoder
class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:
			res = requests.post(url=url,data = data,headers= header)
		else:
			res = requests.post(url=url,data = data)
		return res.text

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.get(url=url,data = data,headers= header)
		else:
			res = requests.get(url=url,data = data)
		return res.text

	def runmain(self,method,url,data=None,header=None):
		res = None
		if method == 'post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False)

if __name__ == '__main__':
	url = 'http://ebkapi.t.17u.cn/ghotel/disopenplatform/OpenApi/1.0/GetHotelRateList'
	data = {
			'Head':'{"UserID":3,"TimeStamp":"1516156123","Sign":"FC7B4D3405863A6D06DC4D6961B708BF"}',
			'Data':'{"HotelId":260807,"ArrivalDate":"2018-12-25T00:00:00","DepartureDate":"2018-12-26T00:00:00","RoomNum":1,"NumberOfAdults":2,"NumberOfChildren":0,"PartnerKey":"64b7a5f65a2ac326070699ba651691cc","ChildAges":null,"IP":null,"Nationality":null}'
	}
	print(data)
	print(type(data['Data']))
	run = RunMethod()
	header = {
		'Content-Type': 'application/x-www-form-urlencoded'
	}
	result = run.runmain('post',url,data, header=header)
	print(json.loads(result))




