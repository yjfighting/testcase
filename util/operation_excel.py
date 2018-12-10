#coding:utf-8
import xlrd
from xlutils.copy import copy
'''
#指定文件路径
data = xlrd.open_workbook('../dataconfig/pythoncase.xls')
#通过索引拿到sheet0的数据
tables = data.sheets()[0]
#拿到table的行数
print(tables.nrows)
#拿到具体位置的参数
print(tables.cell_value(2,1))
'''
class OperationExcel:
	#调用类的构造函数
	def __init__(self,file_path = None,sheet_id = None):
		if file_path:
			self.file_path = file_path
			self.sheet_id = sheet_id
		else:
			self.file_path = '../dataconfig/pythoncase.xls'
			self.sheet_id= 0
		self.data = self.get_data()
	#获取sheets的内容
	def get_data(self):
		data = xlrd.open_workbook(self.file_path)
		tables = data.sheets()[self.sheet_id]
		return tables
	#获取单元格的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows
	#获取某个单元格的内容
	def get_cell_value(self,row,col):
		col = int(col)
		row = int(row)
		return self.data.cell_value(row,col)
	#写入数据
	def write_value(self,row,col,value):
		#读取Excel的内容
		read_data = xlrd.open_workbook(self.file_path)
		#将Excel复制一份出来
		write_data = copy(read_data)
		#拿到write_data的sheet（0）内容拿到
		sheet_data = write_data.get_sheet(0)
		#将内容写入sheet（0）
		sheet_data.write(row,col,value)
		#保存Excel write_data
		write_data.save(self.file_path)

	# 根据拿到的行号找到对应行的内容
	def get_rows_data(self, case_id):
		row_num = self.get_rows_num(case_id)
		rows_data = self.get_row_value(row_num)
		return rows_data

	#根据被依赖的caseid找到对应的行号
	def get_rows_num(self,case_id):
		num = 0
		cols_data = self.get_cols_data()
		for col_data in cols_data:
			if case_id == col_data:
				return num
			else:
				num = num+1

	#根据行号，找到该行内容
	def get_row_value(self,row):
		tables = self.data
		row_data = tables.row_values(row)
		return row_data

	#获取某一列的内容
	def get_cols_data(self,col_id = None):
		if col_id !=None:
			colvalues = self.data.col_values(col_id)
		else:
			colvalues = self.data.col_values(0)
		return colvalues

'''
if __name__ == '__main__':
	opers = OperationExcel()
	print(opers.get_data().nrows)
	print(opers.get_lines())
	print(opers.get_cell_value(2,1))
'''
