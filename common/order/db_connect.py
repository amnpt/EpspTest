# coding=utf-8
import cx_Oracle
from common import get_Config

# 获取数据库信息
username = get_Config.get_database_Username()
password = get_Config.get_database_Password()
database = get_Config.get_database_Url()

# 1、连接数据库，查询交易订单号
def order_query(out_trade_no):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    cursor = conn.cursor()   #创建游标
    res = cursor.execute('select transaction_no,state from TXS_PAY_TRADE_ORDER '
                         'where out_trade_no = \'{}\''.format(out_trade_no))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    data = res.fetchall()   #获取数据
    for transaction_no, state in data:
        return transaction_no
    cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接

# def order_query(sql):
#     conn = cx_Oracle.connect(username, password, database)
#     cursor = conn.cursor()  # 创建游标
#     res = cursor.execute(sql)  # 此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
#     data = res.fetchall()  # 获取数据
#     for transaction_no, state in data:
#         return transaction_no
#     cursor.close()  # 关闭游标
#     conn.close()  # 关闭数据库连接

# 2、连接数据库，查询支付交易记账流水及结算流水
def acc_sett_query(transaction_no):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    acc_cursor = conn.cursor()   #创建游标
    sett_cursor = conn.cursor()
    acc_res = acc_cursor.execute('select * from acc_accountflow  '
                                 'where rownum < 2 and transactionno = \'{}\''.format(transaction_no))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    sett_res = sett_cursor.execute('select * from SETT_SETTMENT_VOUCHER  '
                                   'where rownum < 2 and Transcation_No = \'{}\''.format(transaction_no))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    acc_flow = acc_res.fetchall()
    sett_flow = sett_res.fetchall()
    print(acc_flow)
    print(sett_flow)
    return acc_flow, sett_flow
    acc_cursor.close()   #关闭游标
    sett_cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接

# acc_sett_query(44202109278890838442530)

# 3、连接数据库，查分账订单
def split_order_query(out_trade_no):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    order_cursor = conn.cursor()   #创建游标
    split_order = order_cursor.execute('select state, transaction_no from  TXS_SPLIT_ORDER  '
                                       'where out_trade_no = \'{}\''.format(out_trade_no))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    order_data = split_order.fetchall()   #获取数据
    for state, transaction_no in order_data:
        # print(state,transaction_no)
        return state, transaction_no
    order_cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接

# 4、连接数据库，查询分账明细的订单状态
def split_record_query(transaction_no):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    record_cursor = conn.cursor()
    split_record = record_cursor.execute(
        'select state from TXS_SPLIT_RECORD where rownum<2 and transaction_no = \'{}\''.format(transaction_no))  # 分账明细有多条记录，只取一条rownum<2
    record_data = split_record.fetchall()  # 获取数据
    for state in record_data:
        return state   # ('3',)，返回值是一个元组
    record_cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接



# 5、连接数据库，查询退款交易流水
def refund_order_query(transaction_No):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    txs_cursor = conn.cursor()   #创建游标
    pay_cursor = conn.cursor()   #创建游标
    clr_cursor = conn.cursor()   #创建游标

    txs_res = txs_cursor.execute('select pay_state from Txs_Refund_Pre_Order'
                                 ' where transaction_no = \'{}\''.format(transaction_No))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    pay_res = pay_cursor.execute('select pay_state from PAY_REFUND_ORDER_INFO '
                                 'where transaction_no = \'{}\''.format(transaction_No))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    clr_res = clr_cursor.execute('select state from clr_refund_record '
                                 'where transaction_no = \'{}\''.format(transaction_No))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件

    txs_state = txs_res.fetchall()   #获取数据
    pay_state = pay_res.fetchall()   #获取数据
    clr_state = clr_res.fetchall()   #获取数据

    return txs_state, pay_state, clr_state
    txs_cursor.close()   #关闭游标
    pay_cursor.close()   #关闭游标
    clr_cursor.close()   #关闭游标

    conn.close()   #关闭数据库连接


# 6、连接数据库，查询退款失败记账流水
def refund_acc_query(transaction_No):
    # 建立连接
    conn = cx_Oracle.connect(username, password, database)
    acc_cursor = conn.cursor()  # 创建游标
    # sett_cursor = conn.cursor()
    acc_res = acc_cursor.execute('select type from acc_accountflow  where transactionno = \'{}\''.format(
        transaction_No))
    acc_data = acc_cursor.fetchall()  # 获取数据
    while acc_data == [(1,), (2,)]:
        return 1
    else:
        return 0
    acc_cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接

# refund_acc_query(31202109074885933878613)

# 7、连接数据库，查询退款失败结算流水
def refund_sett_query(transaction_No):
    # 建立连接
    conn = cx_Oracle.connect(username, password, database)
    sett_cursor = conn.cursor()  # 创建游标
    sett_res = sett_cursor.execute('select type from SETT_TK_PARAM  where transaction_no = \'{}\''.format(
        transaction_No))
    sett_data = sett_cursor.fetchall()  # 获取数据
    while sett_data == [('1',), ('2',)]:
        return 1
    else:
        return 0
    sett_cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接

# refund_sett_query(31202109074885933878613)


# 8、连接数据库，查询分账交易退款流水
def split_refund_query(transaction_No):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    cursor = conn.cursor()   #创建游标
    res = cursor.execute('select state from Txs_Refund_Split_Record  where transaction_no = \'{}\''.format(transaction_No))
    state = res.fetchall()   #获取数据
    # print(state)
    # print(state[0][0],state[1][0])
    return state
    cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接

# split_refund_query("31202109089447119882389")


# 9、连接数据库，查询分账退款失败记账流水
def split_refund_acc_query(customercode,transaction_No):
    # 建立连接
    conn = cx_Oracle.connect(username, password, database)
    acc_cursor = conn.cursor()  # 创建游标
    acc_res = acc_cursor.execute('select type from acc_accountflow  where  '
                                 'sourcecustomercode= \'{}\' and transactionno= \'{}\' order by type asc'.format(customercode, transaction_No))
    acc_type= acc_res.fetchall()  # 获取数据
    #print(acc_type)  # [(1,), (2,)]
    while acc_type == [(1,), (2,)]:
        return 1  # 说明退款失败记账流水正常
    else:
        return 0
    # return acc_type
    acc_cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接

#split_refund_acc_query(5651200003063343,31202109087612132289461)


# 10、连接数据库，查询分账退款失败结算流水
def split_refund_sett_query(customercode,transaction_No):
    # 建立连接
    conn = cx_Oracle.connect(username, password, database)
    sett_cursor = conn.cursor()  # 创建游标
    sett_res = sett_cursor.execute('select type from SETT_TK_PARAM  where  customer_code = \'{}\' '
                                   'and transaction_no = \'{}\' order by type asc'.format(customercode, transaction_No))
    sett_type = sett_res.fetchall()  # 获取数据
    #print(sett_type)   #  [('1',), ('2',)]
    while sett_type == [('1',), ('2',)]:
        return 1   # 说明退款失败结算流水正常
    else:
        return 0
    # return sett_type
    sett_cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接

#split_refund_sett_query(5651200003063343,31202109087612132289461)


# 11、连接数据库，查询原分账金额
def split_amnout_query(transaction_no):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    record_cursor = conn.cursor()
    split_record = record_cursor.execute(
        'select customer_code, orig_amount from TXS_SPLIT_RECORD where transaction_no = \'{}\''.format(transaction_no))  # 分账明细有多条记录，只取一条rownum<2
    record_data = split_record.fetchall()  # 获取数据
    # print(record_data[0],record_data[1])
    if record_data[0][0] == get_Config.get_customercode_Conf() and record_data[1][0] == get_Config.get_customercode_Conf2():
        # print(record_data[0][1], record_data[1][1])
        return record_data[0][1], record_data[1][1]

    elif record_data[0][0] == get_Config.get_customercode_Conf2() and record_data[1][0] == get_Config.get_customercode_Conf():
        # print(record_data[1][1], record_data[0][1])
        return record_data[1][1], record_data[0][1]

    else:
        print("数据错误，请人工检查数据")

    record_cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接

# split_amnout_query(67202109080955433162731)


# 12、连接数据库，查询 clr_withdraw_record 表状态
def clr_withdraw_query(transactionNo):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    cursor = conn.cursor()   #创建游标
    res = cursor.execute('select state，channel_resp_code, channel_resp_msg from clr_withdraw_record where transaction_no = \'{}\''.format(transactionNo))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    order_data = res.fetchall()  # 获取数据
    for pay_state, channel_resp_code, channel_resp_msg in order_data:
        return pay_state, channel_resp_code, channel_resp_msg
    cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接


# 13、连接数据库，查询 txs_withdraw_trade_order 数据
def txs_withdraw_query(transactionNo):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    cursor = conn.cursor()   #创建游标
    res = cursor.execute('select pay_state from txs_withdraw_trade_order where transaction_no= \'{}\''.format(transactionNo))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    pay_state = res.fetchall()   #获取数据
    return pay_state
    cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接


# 14、连接数据库，查询 pay_withdraw_record 表状态
def pay_withdraw_query(transactionNo):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    cursor = conn.cursor()   #创建游标
    res = cursor.execute('select pay_state from pay_withdraw_record  where transaction_no= \'{}\''.format(transactionNo))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    pay_state = res.fetchall()   #获取数据
    return pay_state
    cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接


# 2、连接数据库，查询单笔代付(成功)记账流水及结算流水
def withdrawal_acc_sett_query(transaction_no):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    acc_cursor = conn.cursor()   #创建游标
    sett_cursor = conn.cursor()
    acc_res = acc_cursor.execute('select * from acc_accountflow  '
                                 'where transactionno = \'{}\''.format(transaction_no))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    sett_res = sett_cursor.execute('select * from SETT_SETTMENT_VOUCHER  '
                                   'where Transcation_No = \'{}\''.format(transaction_no))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    acc_flow = acc_res.fetchall()
    sett_flow = sett_res.fetchall()

    return acc_flow, sett_flow
    acc_cursor.close()   #关闭游标
    sett_cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接

#withdrawal_acc_sett_query(44202109278890838442530)


# 2、连接数据库，查询子商户提现(失败)记账流水（回滚）,失败时不会生成结算流水
def withdrawal_acc_toTail_query(customercode, transaction_no):
    #建立连接
    conn = cx_Oracle.connect(username, password, database)
    acc_cursor = conn.cursor()   #创建游标
    sett_cursor = conn.cursor()
    acc_res = acc_cursor.execute('select type from acc_accountflow  where sourcecustomercode= \'{}\' '
                                 'and transactionno= \'{}\' order by type asc'.format(customercode, transaction_no))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    acc_type = acc_res.fetchall()
    # print(acc_type)
    while acc_type == [(1,), (2,)]:
        return 1
    else:
        return 0
    acc_cursor.close()   #关闭游标
    sett_cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接

#withdrawal_acc_toTail_query(5651200003063343, 44202109272738604944641)
#withdrawal_acc_toTail_query(5651200003063377, 44202109272738604944641)