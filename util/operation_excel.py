#coding:utf-8
import xlrd

'''
#指定文件路径
data = xlrd.open_workbook('../dataconfig/pythoncase.xlsx')
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
			self.file_path = '../dataconfig/pythoncase.xlsx'
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
		return self.data.cell_value(row,col)

if __name__ == '__main__':
	opers = OperationExcel()
	print(opers.get_data().nrows)
	print(opers.get_lines())
	print(opers.get_cell_value(2,1))
