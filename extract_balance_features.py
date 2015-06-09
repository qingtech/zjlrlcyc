#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'woniu17'

import os

import pandas as pd

DELIMITER = ','

def extract_balance_features(user_balance_file_path):
    balance_features = {}
    '''
    user_balance = pd.read_csv(user_balance_file_path)
    print user_balance.iloc[:1,:1]
    print user_balance.loc[:0,'user_id']
    '''
    user_balance = open(user_balance_file_path)
    first_line = True
    for line in user_balance:
        if first_line:
            first_line = False
            continue
        #用户ID, 日期
        #今日余额, 昨日余额
        #今日总购买量=直接购买+收益
        #今日直接购买量, 今日余额宝购买量
        #今日银行购买量, 今日总赎回量
        #今日消费总量, 今日转出总量
        #进入转出到余额宝总额, 今日转出到银行卡总额
        #今日收益, 今日类目1消费总额, ...
        #..., ...
        uid, report_date, \
            t_balance, y_balance, \
            total_purchase_amt, \
            direct_purchase_amt, purchase_bal_amt, \
            purchase_bank_amt, total_redeem_amt, \
            consume_amt, transfer_amt, \
            tftobal_amt, tftocard_amt, \
            share_amt, category1, category2, \
            category3, category4  \
            = line.split(DELIMITER)
        key = '%s:%s' % (uid, report_date)
        balance_features[key] = [total_purchase_amt, total_redeem_amt]
    return balance_features


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))
    user_balance_file_path = path + '/user_balance_table.csv'
    balance_features = extract_balance_features(user_balance_file_path)
    for key, val in balance_features.iteritems():
        print key, val
