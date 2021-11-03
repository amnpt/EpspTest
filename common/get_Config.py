# -*- coding: utf-8 -*-
import yaml
from config import globalparam

config_file = globalparam.config_file_path + "\\" + "config.yml"

# 1、获取邮箱配置
def get_email_Conf():
    # with open ("G:/Git/pytest_testApi/config/config.yml", "r", encoding='utf-8') as f:
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        # print(type(dic))
        # print(dic)
        sender = dic['email']['sender']
        receiver = dic['email']['receiver']
        smtpserver = dic['email']['smtpserver']
        username = dic['email']['username']
        password = dic['email']['password']
        # print(sender, receiver, smtpserver, username, password)
        return sender, receiver, smtpserver, username, password

# 2、获取商户的证书配置5651200003063343
def get_signno_Conf():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        sign_no = dic['customer']['sign_no']
        return sign_no

# 3、获取商户
def get_customercode_Conf():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        customer_code = dic['customer']['customer_code']
        return customer_code


# 4、获取商户号1的证书配置 5651200003067490
def get_signno_Conf1():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        sign_no = dic['customer1']['sign_no']
        return sign_no

# 5、获取商户1
def get_customercode_Conf1():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        customer_code = dic['customer1']['customer_code']
        return customer_code


# 6、获取运营门户登录配置
def get_admin_Url():
    # with open("G:/Git/pytest_testApi/config/config.yml", "r", encoding='utf-8') as f:
    with open(config_file, "r", encoding='utf-8') as f:
        print(config_file)
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        admin_url = dic['admin']['admin_url']
        return admin_url

# 7、获取运营门户登录账号
def get_admin_Username():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        admin_username = dic['admin']['username']
        return admin_username

# 8、获取运营门户登录密码
def get_admin_Password():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        admin_password = dic['admin']['password']
        return admin_password

# 9、获取数据库登录账号
def get_database_Username():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        database_username = dic['database']['username']
        return database_username

# 10、获取数据库登录密码
def get_database_Password():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        database_password = dic['database']['password']
        return database_password

# 11、获取数据库登录地址
def get_database_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        database_url = dic['database']['database_url']
        return database_url

# 12、获取修改支付订单状态地址
def get_order_modify_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        modify_url = dic['order']['modify_url']
        return modify_url

# 13、获取查询交易结果地址
def get_order_result_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        result_url = dic['order']['result_url']
        return result_url

# 14、获取主扫地址
def get_mainScaning_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        mainScaning_url = dic['request_Url']['mainScaning_url']
        return mainScaning_url

# 15、获取商户2
def get_customercode_Conf2():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        customer_code = dic['customer2']['customer_code']
        return customer_code

# 14、获取分账地址
def get_splitPay_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        splitPay_url = dic['request_Url']['splitPay_url']
        return splitPay_url

# 15、获取退款地址
def get_refund_apply_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        refund_apply_url = dic['request_Url']['refund_apply_url']
        return refund_apply_url

# 16、获取分账交易退款地址
def get_splitRefund_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        splitRefund_url = dic['request_Url']['splitRefund_url']
        return splitRefund_url

# 17、获取账户分账地址
def get_accountSplit_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        accountSplit_url = dic['request_Url']['accountSplit_url']
        return accountSplit_url

# 18、获取单笔代付地址
def get_withdrawalToCard_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        withdrawalToCard_url = dic['request_Url']['withdrawalToCard_url']
        return withdrawalToCard_url

# 19、获取修改代付订单状态地址
def get_withdrawal_modify_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        withdrawal_modify_url = dic['order']['withdrawal_url']
        return withdrawal_modify_url



# 20、获取子商户提现地址
def get_withdraw_subMerchant_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        withdraw_subMerchant_url = dic['request_Url']['withdraw_subMerchant_url']
        return withdraw_subMerchant_url


# 21、获取请求参数验签地址
def get_req_encrypt_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        req_encrypt_url = dic['encrypt']['req_encrypt_url']
        return req_encrypt_url

# 22、获取银行卡信息加密地址
def get_auth_encrypt_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        auth_encrypt_url = dic['encrypt']['auth_encrypt_url']
        return auth_encrypt_url

# 23、获取协议支付预交易地址
def get_protocolPayPre_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        protocolPayPre_url = dic['request_Url']['protocolPayPre']
        return protocolPayPre_url

# 24、获取协议支付交易确认地址
def get_protocolPayConfirm_Url():
    with open(config_file, "r", encoding='utf-8') as f:
        cfg = f.read()
        dic = yaml.load(cfg, Loader=yaml.FullLoader)
        protocolPayConfirm_url = dic['request_Url']['protocolPayConfirm']
        return protocolPayConfirm_url
