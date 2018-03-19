import json
import jmespath
from case.jiekou.client import HTTPClient


class AbstractExtractor(object):
    """ Basic extractor, you only need to implement full_extract """

    extractor_type = None

    def extract(self):
        pass


class JMESPathExtractor(AbstractExtractor):
    """ Extractor that uses JMESPath syntax
        See http://jmespath.org/specification.html for details
    """
    extractor_type = 'jmespath'

    def extract(self, query=None, body=None):
        if isinstance(body, bytes):
            body = str(body, 'utf-8')

        try:
            res = jmespath.search(query, json.loads(body))  # Better way
            return res
        except Exception as e:
            raise ValueError("Invalid query: " + query + " : " + str(e))


# 下面做一个演示：
if __name__ == '__main__':

    res = HTTPClient(url='http://wthrcdn.etouch.cn/weather_mini?citykey=101010100').send()
    print(res.text)
    # 这是一个天气预报接口，返回的数据格式如下：
    # {"data": {
    #     "yesterday": {"date": "17日星期四", "high": "高温 31℃", "fx": "东南风", "low": "低温 22℃", "fl": "<![CDATA[<3级]]>",
    #                   "type": "多云"},
    #     "city": "北京",
    #     "aqi": "91",
    #     "forecast": [
    #         {"date": "18日星期五", "high": "高温 28℃", "fengli": "<![CDATA[<3级]]>", "low": "低温 22℃", "fengxiang": "东北风",
    #          "type": "多云"},
    #         {"date": "19日星期六", "high": "高温 29℃", "fengli": "<![CDATA[<3级]]>", "low": "低温 22℃", "fengxiang": "东风",
    #          "type": "雷阵雨"},
    #         {"date": "20日星期天", "high": "高温 29℃", "fengli": "<![CDATA[<3级]]>", "low": "低温 23℃", "fengxiang": "东南风",
    #          "type": "阴"},
    #         {"date": "21日星期一", "high": "高温 30℃", "fengli": "<![CDATA[<3级]]>", "low": "低温 24℃", "fengxiang": "西南风",
    #          "type": "晴"},
    #         {"date": "22日星期二", "high": "高温 29℃", "fengli": "<![CDATA[<3级]]>", "low": "低温 24℃", "fengxiang": "北风",
    #          "type": "雷阵雨"}
    #     ],
    #     "ganmao": "各项气象条件适宜，无明显降温过程，发生感冒机率较低。", "wendu": "25"
    # },
    #     "status": 1000,
    #     "desc": "OK"}

    j = JMESPathExtractor()
    j_1 = j.extract(query='data.forecast[1].date', body=res.text)
    j_2 = j.extract(query='data.ganmao', body=res.text)
    print(j_1, j_2)
    # 结果：
    # 19日星期六 各项气象条件适宜，无明显降温过程，发生感冒机率较低。
    #对接口测试来说，很多时候，我们的用例不是一次请求就OK了的，而是多个请求复合的，
    # 我们第二个请求可能会用到第一个请求返回值中的数据，这就要我们再次进行封装，做一个抽取器，从结果中抽取部分信息