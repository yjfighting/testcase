#coding:utf-8
import json

'''
fp = open("../dataconfig/ratelist.json")
data=json.load(fp)
print(data['ratelist01'])
'''

class OperationJson:
	def __init__(self):
		self.data = self.read_data()

	#读取JSON文件
	def read_data(self):
		'''
		#用完文件之后要close，否则会一直占用文件
		fp=open("../dataconfig/ratelist.json")
		fp.close()
		'''
		#这种方法用完json文件之后会自动关闭，不需要再次close
		with open("../dataconfig/ratelist.json") as fp:
			data = json.load(fp)
			return data
	#根据关键字获取数据
	def get_data(self,idvalue):
		return self.data[idvalue]

if __name__ == '__main__':
	opjson = OperationJson()
	print(opjson.get_data("ratelist01"))
