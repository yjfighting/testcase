#coding:utf-8
import json

class CommomUtil:
    def is_contain(self,strone,strtwo):
        '''
        判断strtwo中是否包含strone
        '''
        flag = None
        if isinstance(strone,str):
            if strone.find(strtwo) > 0:
                flag = True
            else:
                flag = False
        return flag
        #if dictone.__contains__(keydict):

if __name__ == '__main__':
    com = CommomUtil()
    a = '{"result":{"code":105,"message":"可订","result":None}}'
    b = '{"code":105,"result":None}'

    res = com.is_contain(a,b[:-1])

    print(b[:-1],type(json.dumps(b)[:-1]),a,type(a),res)

