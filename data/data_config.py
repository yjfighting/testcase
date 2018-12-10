#coding:utf-8

class global_var:
	#caseid
	id = '0'
	url = '1'
	run = '2'
	request_way = '3'
	header = '4'
	rehead = '5'
	data = '6'
	case_depend = '7'
	data_depend = '8'
	field_depend = '9'
	exp_result = '10'
	actual_result = '11'

#获取caseid
def get_id():
	return global_var.id
#获取URL
def get_url():
	return global_var.url
#获取是否运行
def get_run():
	return global_var.run
#获取请求方式
def get_way():
	return global_var.request_way
#获取是否有header
def get_header():
	return global_var.header
#获取header的值,先写死
def get_header_value():
	header = {
		'Content-Type': 'application/x-www-form-urlencoded'
	}
	return header
#获取接口请求参数中的head参数值
def get_rehead():
	rehead = '{{"UserID":3,"TimeStamp":"1516156123","Sign":"FC7B4D3405863A6D06DC4D6961B708BF"}}'
	return rehead
#获取请求参数
def get_data():
	return global_var.data
#获取case依赖
def get_decase():
	return global_var.case_depend
#获取data依赖
def get_dedata():
	return global_var.data_depend
#获取字段依赖
def get_defield():
	return global_var.field_depend
#获取预期结果
def get_expresult():
	return global_var.exp_result
#获取实际结果
def get_actresult():
	return global_var.actual_result
