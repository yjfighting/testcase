# coding:utf-8
import smtplib
from email.mime.text import MIMEText
import requests
import json

class SendEmail:
    #def __init__(self,message):
    message = ''
    '''
    global send_user_email
    global email_host
    global password
    global port
    send_user_email = '412769776@qq.com'
    port = 25
    email_host = 'smtp.qq.com'
    password = 'ujiovmqocsdpbhfj'

    def send_email(self,user_list,sub,content):
        send_user = "yj"+"<"+send_user_email+">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = send_user
        # 以冒号分割收件人
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host,port)
        server.login(send_user,password)
        server.sendmail(send_user,user_list,message.as_string())
        server.close()
    '''
    def send_email(self,message):
        mail_url = 'http://tccommon1.qa.17usoft.com/internalemailservice/send'
        headers_mail = {"Content-Type": "application/json"}
        data_mail = {
            "account": "commontest",
            "password": "123456",
            "emailTo": "yj26956@ly.com,lmy47205@ly.com",
            "parameter": {
                "emailSubject": "政策可订查询结果",
                "mPriority": 1,
                "emailFromDisplay": "国际酒店质量保障组"
            }
        }

        data_mail['parameter']['emailBody'] = message
        resp_mail = requests.post(url=mail_url, headers=headers_mail, data=json.dumps(data_mail))
        resp_json_mail = resp_mail.json()
        print(resp_json_mail)

    def send_result_statistics(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        # %.2f 表示取小数点后俩位，%% 表示取一个%
        pass_percent = "%.2f%%" %(pass_num/count_num*100)
        fail_percent = "%.2f%%" %(fail_num/count_num*100)
        message = '此次一共运行可订接口次数为%s次，通过次数为%s次，失败次数为%s次，通过率为%s,失败率为%s' %(count_num,pass_num,fail_num,pass_percent,fail_percent)
        self.send_email(message)

if __name__ == '__main__':
    sen = SendEmail()
    '''
    user_list = ['1931703952@qq.com']
    sub = '这是一封测试邮件'
    content = '这是发出来的第一份email'
    sen.send_email(user_list,sub,content)
    '''
    message = 'this is a test email'
    sen.send_result_statistics([1,2,3],[1,2,3,4,5])
