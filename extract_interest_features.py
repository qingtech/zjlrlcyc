#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'woniu17'

import os

DELIMITER = ','

'''
interest features only contains mfd_daily_yield, mfd_7daily_yield
'''
def extract_interest_features(interest_file_path):
    interest_features = {}
    interest = open(interest_file_path)
    first_line = True
    for line in interest:
        if first_line:
            first_line = False
            continue
        mfd_date, mfd_daily_yield, mfd_7daily_yield = line.split(DELIMITER)
        interest_features[mfd_date] = [float(mfd_daily_yield), float(mfd_7daily_yield)]

    return interest_features


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))
    print path
    interest_file_path = path + '/mfd_day_share_interest.csv'
    interest_features = extract_interest_features(interest_file_path)
    for key, val in interest_features.items():
        print key, val
