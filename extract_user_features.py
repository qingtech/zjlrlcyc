#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'woniu17'

import os

DELIMITER = ','

'''
user features only contains sex and city now
'''
def extract_user_features(user_profile_file_path):
    user_features = {}
    user_profile = open(user_profile_file_path)
    first_line = True
    for line in user_profile:
        if first_line:
            first_line = False
            continue
        uid, sex, city, cslt = line.split(DELIMITER)
        user_features[uid] = [int(sex), int(city)]

    return user_features


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))
    print path
    user_profile_file_path = path + '/user_profile_table.csv'
    user_features = extract_user_features(user_profile_file_path)
    for key, val in user_features.items():
        print key, val
