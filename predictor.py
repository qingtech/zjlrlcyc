#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os

import sklearn.linear_model as lm
import sklearn.datasets as ds

from extract_profile_features import extract_profile_features
from extract_balance_features import extract_balance_features
from extract_interest_features import extract_interest_features


def predict():
    path = os.path.abspath(os.path.dirname(__file__))
    user_profile_file_path = path + '/user_profile_table.csv'
    profile_features = extract_profile_features(user_profile_file_path)
    interest_file_path = path + '/mfd_day_share_interest.csv'
    interest_features = extract_interest_features(interest_file_path)
    user_balance_file_path = path + '/user_balance_table.csv'
    balance_features = extract_balance_features(user_balance_file_path)
