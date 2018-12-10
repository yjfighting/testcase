#coding:utf-8
class CommomUtil:
    def is_contain(self,strone,strtwo):
        '''
        判断strtwo中是否包含strone
        '''
        flag = None
        if strone in strtwo:
            flag = True
        else:
            flag = False
        return flag
