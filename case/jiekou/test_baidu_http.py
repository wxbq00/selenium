import unittest
import os
from case.jiekou.client import HTTPClient
from case.log.log import Logger,logger
from case.config.config import Config, REPORT_PATH
import HTMLTestRunner
from case.jiekou.assertion import assertHttpCode
import requests

report_path = os.path.join(os.getcwd(), "report1")


class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        assertHttpCode(res,[400])
        self.assertIn('百度一下，你就知道', res.text)
        print(res.text)


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner =HTMLTestRunner.HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='接口html报告')
        runner.run(TestBaiDuHTTP('test_baidu_http'))
