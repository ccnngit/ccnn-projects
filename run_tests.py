import unittest
import yagmail
import time
from HTMLTestRunner import HTMLTestRunner

#  测试报告作为附件发送指定邮箱
sender = '1434748447@qq.com'
receivers = ['893447389@qq.com', '1434748447@qq.com']


def send_mail(report):
    yag = yagmail.SMTP(user=sender, password='amkdsqkxmcpzihbg', host='smtp.qq.com')
    subject = '主题：自动化测试报告'
    contents = '正文，请查看附件。'
    yag.send(receivers, subject, contents, report)
    print('email has send out')


if __name__ == '__main__':
    #  定义测试用例的目录为当前目录下的test_case目录
    test_dir = 'C:/Users/huatu/PycharmProjects/poium/test_case/'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    #  获取当前日期和时间
    now_time = time.strftime('%Y-%m-%d %H%M%S')
    report_dir = 'C:/Users/huatu/PycharmProjects/poium/test_report/'
    html_report = './test_report/' + now_time + 'result.html'
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='UI自动化测试报告',
                            description='运行环境：windows 10，Chrome 浏览器'
                            )
    runner.run(suit)
    fp.close()
    send_mail(html_report)
