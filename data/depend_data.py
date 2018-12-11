#coding:utf-8
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
#from jsonpath_rw import jsonpath,parse
import json

#处理所有数据依赖的相关问题
class DependData:
    def __init__(self,case_id):
        self.opera_excel = OperationExcel()
        self.case_id = case_id
        self.data=GetData()

    #通过caseid获取该case的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    #执行依赖case，获取接口返回结果
    def run_depend(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_rows_num(self.case_id)
        request_data = {
                'Head':'{"UserID":3,"TimeStamp":"1516156123","Sign":"FC7B4D3405863A6D06DC4D6961B708BF"}',
                'Data': self.data.get_data_for_json(row_num)
         }
        header = self.data.is_header(row_num)
        url = self.data.get_request_url(row_num)
        method = self.data.get_request_method(row_num)
        res = run_method.runmain(method,url,request_data,header)
        return json.loads(res)

    #根据依赖的key获取获取执行依赖测试case的响应数据然后返回给下一个接口的请求字段----难点
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        #拿到了依赖case的结果
        response_data = self.run_depend()
        print(type(response_data))
        response_data_dict = json.loads(response_data)
        print(type(response_data_dict))
        #拿到RoomList
        roomlist = response_data_dict['result']['Result'][0]['RoomList']
        rateinfoList = []
        rate_code_list=[]
        attachment_key_list = []
        i = 0
        j = 0
        #遍历response_data_dict循环获取ratecode和attachmentkey
        for i in range(0, len(roomlist)):
            rateinfoList.append(roomlist[i]['RateInfoList'])
            # print(rateinfoList[0])
            for j in range(0, len(rateinfoList[i])):
                rate_code_list.append(roomlist[i]['RateInfoList'][j]['RateCode'])
                attachment_key_list.append(roomlist[i]['RateInfoList'][j]['AttachmentKey'])

        #在结果集中找字段
        #depend_data_a = ["result"]["Result"][0]["roomlist"][0]["RateInfoList"][0][depend_data]
        #json_exe = parse('result.Result[*].roomlist[*].RateInfoList[*].RateCode')
        #结果集
        #rate_code_list = [match.value for match in parse('result.Result[0].RoomList[0].RateInfoList[*].RateCode').find(response_data_dict)]
        #返回list的第一个结果

        print(rate_code_list)
        print(attachment_key_list)
        return [rate_code_list,attachment_key_list]


