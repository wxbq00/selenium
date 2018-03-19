
"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os
from case.config.file_reader import YamlReader

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')

# CONFIG_FILE = BASE_PATH + '\config\config.yml'
# DATA_PATH = BASE_PATH + '\data\\'
# DRIVER_PATH = BASE_PATH + '\drivers\\'
# LOG_PATH = BASE_PATH + '\log\\'
# REPORT_PATH = BASE_PATH + '\report\\'
CONFIG_FILE = r'/Users/Tiernan/Desktop/projects/wcn_selenium/case/config/config.yml'

DATA_PATH = r'/Users/Tiernan/Desktop/projects/wcn_selenium/case/data'
DRIVER_PATH=r'/Users/Tiernan/Desktop/projects/wcn_selenium/case/drivers/chromedriver.exe'
LOG_PATH = r'/Users/Tiernan/Desktop/projects/wcn_selenium/case/log'
REPORT_PATH = r'/Users/Tiernan/Desktop/projects/wcn_selenium/case/report'


# CONFIG_FILE = '/Users/Tiernan/Desktop/wcn_selenium/case/config/config.yml'
# DATA_PATH = '/Users/Tiernan/Desktop/wcn_selenium/case/data/'
# DRIVER_PATH=''
# LOG_PATH = '/Users/Tiernan/Desktop/wcn_selenium/case/log/'
# REPORT_PATH = '/Users/Tiernan/Desktop/wcn_selenium/case/report/'



class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)

