# coding:utf-8

from base.runmethod import RunMethod
from data.get_data import GetData


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    # 程序执行的主入口
    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        # 去除第一行
        for i in range(1, rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)

            if is_run:
                res = self.run_method.runmain(method, url, data, header)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

