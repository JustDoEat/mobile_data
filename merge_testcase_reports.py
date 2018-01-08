#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-8
# merge_testcase_reports.py
'''
汇总多天的测试报告。

使用方法：

参数input_directory：为包含测试报告的目录。

参数：output：为汇总测试的输出文件。
'''
import traceback
import re
import shutil
import os
import glob

import pandas

from data_common import maps, count, convert_result, produce_xls

input_directory = r"D:\test2"
output = r"d:\output.xls"
results = {}

for name in glob.glob('{0}{1}*.xls'.format(input_directory, os.sep)):
    records = pandas.read_excel(name)
    for seq in range(len(records)):
        index = records.iloc[seq, 0]
        if re.match(r'\d+', str(index)):
            if not index in results:
                results[index] = []
            results[index].append(
                [records.iloc[seq, 2], records.iloc[seq, 3],
                 records.iloc[seq, 4], records.iloc[seq, 5],
                 records.iloc[seq, 6], ])

produce_xls(results, output)
