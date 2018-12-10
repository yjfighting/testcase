#coding:utf-8
from data import data_config
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
#import data.data_config as a

class GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()

	#获取Excel行数，即case个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = data_config.get_run()
		run_model = self.opera_excel.get_cell_value(row,col)
		if run_model == 'Y':
			flag = True
		else:
			flag = False
		return flag

	#是否携带header
	def is_header(self,row):
		col = data_config.get_header()
		header = self.opera_excel.get_cell_value(row,col)
		if header == 'Y':
			return data_config.get_header_value()
		else:
			return None

	#获取请求方式
	def get_request_method(self,row):
		col = int(data_config.get_way())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method

	#获取URL
	def get_request_url(self,row):
		col = int(data_config.get_url())
		url = self.opera_excel.get_cell_value(row,col)
		return url

	#获取请求数据
	def get_request_data(self,row):
		col = int(data_config.get_data())
		data = self.opera_excel.get_cell_value(row,col)
		if data == '':
			return None
		else:
			return data

	#通过获取关键字拿到data数据
	def get_data_for_json(self,rowvalue):
		#因为不是所有的情况都会需要使用此方法，所有不需要在构造函数中将此类进行实例化。但是在构造函数中实例化也没有问题
		opera_json = OperationJson()
		request_data = opera_json.get_data(self.get_request_data(rowvalue))
		return request_data

	#获取预期结果
	def get_expect_data(self, row):
		col = int(data_config.get_expresult())
		result_data = self.opera_excel.get_cell_value(row,col)
		if result_data =='':
			return None
		else:
			return result_data

	#写入实际结果
	def write_result(self,row,value):
		col = int(data_config.get_actresult())
		actresult = self.opera_excel.write_value(row,col,value)
		return actresult

	#获取依赖数据的key
	def get_depend_key(self,row):
		col = int(data_config.get_defield())
		depend_key = self.opera_excel.get_cell_value(row,col)
		if depend_key == '':
			return None
		else:
			return depend_key

	#判断是否有case依赖
	def is_depend(self,row):
		col = int(data_config.get_decase())
		depend_case_id = self.opera_excel.get_cell_value(row,col)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id

	#获取数据依赖的字段
	def get_depend_field(self,row):
		col = int(data_config.get_defield())
		depend_field = self.opera_excel.get_cell_value(row,col)
		if depend_field == "":
			return None
		else:
			return depend_field