# coding:utf-8
import sys
sys.path.append('D:/MyConfiguration/yj26956/PycharmProjects/testcase')
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommomUtil
from data.depend_data import DependData
import json


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.comutil = CommomUtil()

    # 程序执行的主入口
    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        i = 0
        # 去除第一行
        for i in range(1, rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            jsondata = self.data.get_data_for_json(i)
            print(jsondata)
            print(type(jsondata))
            reqdata = {
                'Head':'{"UserID":3,"TimeStamp":"1516156123","Sign":"FC7B4D3405863A6D06DC4D6961B708BF"}',
                'Data':jsondata
            }
            header = self.data.is_header(i)
            expect = self.data.get_expect_data(i)
            print(reqdata)
            print(type(reqdata))
            depend_case = self.data.is_depend(i)
            if depend_case != None:
                self.depend_data = DependData(depend_case)
                #返回依赖的响应数据
                depend_response_data_list = self.depend_data.get_data_for_key(i)
                print(depend_response_data_list)
                ratecode_response_list = depend_response_data_list[0]
                print(ratecode_response_list)
                attachment_key_response_list= depend_response_data_list[1]
                print(attachment_key_response_list)
                '''
                #获取依赖的字段
                depend_key = self.data.get_depend_field(i)
                print(depend_key)
                #将配置在json文件中的dependkey的值更新一下
                print(depend_key[0],depend_key[1])
                '''
                for i in range(0,len(ratecode_response_list)):
                    jsondatadict=json.loads(jsondata)
                    #print(jsondatadict['RateCode'],jsondatadict['AttachmentKey'])
                    #从列表接口返回的ratecodelist赋值给请求参数RateCode
                    jsondatadict["RateCode"] = ratecode_response_list[i]
                    # 从列表接口返回的attachmentkeylist赋值给请求参数中的attachmentkey
                    jsondatadict["AttachmentKey"] = attachment_key_response_list[i]
                    #jsondatadict_to_str = str(jsondatadict)
                    #reqdata['Data'] = jsondatadict_to_str.replace('\'', '\"')
                    jsondatadict_to_str = json.dumps(jsondatadict)
                    reqdata['Data'] = jsondatadict_to_str
                    print(reqdata)
                    res = self.run_method.runmain(method, url, reqdata, header)
                    print(res)

            else:
                if is_run:
                    res = self.run_method.runmain(method, url, reqdata, header)
                    print(res)
                '''
                if self.comutil.is_contain(expect,res):
                    self.data.write_result(i,'测试通过')
                    #print("测试通过")
                else:
                    self.data.write_result(i, '测试失败')
                    #print("测试失败")
                 
            '''

if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

