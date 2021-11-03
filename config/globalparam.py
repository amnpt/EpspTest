import os
from common.readconfig import ReadConfig

# Read configguration file
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))
# Projwct parameter setting
prj_path = read_config.getValue('projectConfig', 'project_path')
# Log path
log_path = os.path.join(prj_path, 'logs')
# Screenshot file path
img_path = os.path.join(prj_path, 'file', 'image')
# Exception screenshot file path
eximg_path = os.path.join(prj_path,'file', 'exception_img')
# Test report path
report_path = os.path.join(prj_path, 'report')
# Upload the outoit file path
auto_path = os.path.join(prj_path, 'file')
# Test data path
data_path = os.path.join(prj_path, 'data')
# testCase path
test_case_path = os.path.join(prj_path, 'testCase')
apiTest_path = os.path.join(test_case_path, 'apiTest')

# Default brower
browser = 'chrome'
