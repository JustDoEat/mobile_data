#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-8
# data_common.py

import os
import shutil
import traceback
import time
from pathlib import Path
import glob

import pandas

title = [u"用例编号", u"测试用例", u"重试总次数", u"比对成功次数", u"活体成功次数",
         u"成功次数", u"测试次数", u"比对通过率", u"活体通过率", u"用户通过率"]

maps = {
    1: (u"白天-室内-正常光-非走动-720的7人间的中间位置", u"白天-室内-正常光"),
    2: (u"白天-室内-正常光-非走动-路演区第4排(低)中间位置", u"白天-室内-正常光"),
    3: (u"白天-室内-正常光-非走动-海翔通往荔园路的楼下通道门口", u"白天-室内-正常光"),
    4: (u"白天-室内-正常光-非走动-701健身区域", u"白天-室内-正常光"),
    5: (u"白天-室内-正常光-非走动-电梯间内", u"白天-室内-正常光"),
    6: (u"白天-室内-正常光-走动-七楼楼道", u"白天-室内-正常光"),
    7: (u"白天-室内-正常光-走动-717办公室", u"白天-室内-正常光"),
    8: (u"白天-室内-正常光-动作-平躺", u"白天-室内-正常光"),
    9: (u"白天-室内-正常光-动作-侧躺", u"白天-室内-正常光"),
    10: (u"白天-室内-暗光-非走动-720办公室4人间关灯后", u"白天-室内-暗光"),
    11: (u"白天-室内-逆光-非走动-路演区窗口逆光", u"白天-室内-逆光"),
    12: (u"白天-室内-逆光-非走动-717办公室过道顶灯光", u"白天-室内-逆光"),
    13: (u"白天-室内-逆光-非走动-厕所头顶灯光", u"白天-室内-逆光"),
    14: (u"白天-室内-逆光-非走动-701健身区域", u"白天-室内-逆光"),
    15: (u"白天-室内-逆光-走动-路演区窗口逆光", u"白天-室内-逆光"),
    16: (u"白天-室内-逆光-走动-717办公室过道顶灯光", u"白天-室内-逆光"),
    17: (u"白天-室内-逆光-走动-厕所头顶灯光", u"白天-室内-逆光"),
    18: (u"白天-室外-正常光-非走动-海翔楼下空旷处（品骏快递）（背阴处正常光）",
         u"白天-室外-正常光"),
    19: (u"白天-室外-正常光-非走动-荔园路树荫下", u"白天-室外-正常光"),
    20: (u"白天-室外-正常光-走动-海翔楼下空旷处（品骏快递）（背阴处正常光）",
         u"白天-室外-正常光"),
    21: (u"白天-室外-正常光-走动-荔园路树荫下", u"白天-室外-正常光"),
    22: (u"白天-室外-逆光-非走动-海翔楼下空旷处 (品骏快递)(建议中午左右)（背对太阳）",
         u"白天-室外-逆光"),
    23: (u"白天-室外-逆光-非走动-荔园路树荫下（建议中午左右）（背对太阳）",
         u"白天-室外-逆光"),
    24: (u"白天-室外-逆光-非走动-（阴天）海翔通往荔园路的楼下通道门口（人物背对门口）",
         u"白天-室外-逆光"),
    25: (u"白天-室外-逆光-非走动-（阴天）手机朝上，背朝天空", u"白天-室外-逆光"),
    26: (u"白天-室外-逆光-走动-海翔楼下空旷处（品骏快递）（建议中午左右)（背对太阳）",
         u"白天-室外-逆光"),
    27: (u"白天-室外-逆光-走动-荔园路树荫下（建议中午左右）（背对太阳）",
         u"白天-室外-逆光"),
    28: (u"白天-室外-逆光-走动-（阴天）手机朝上，背朝天空", u"白天-室外-逆光"),
    29: (u"白天-室外-强光-非走动-海翔楼下空旷处（建议中午左右）（面对太阳）",
         u"白天-室外-强光"),
    30: (u"白天-室外-强光-非走动-荔园路树荫下（面对太阳）", u"白天-室外-强光"),
    31: (u"白天-室外-强光-走动-海翔楼下空旷处（建议中午左右）（面对太阳）",
         u"白天-室外-强光"),
    32: (u"白天-室外-强光-走动-荔园路树荫下（面对太阳）", u"白天-室外-强光"),
    33: (u"白天-室内-正常光-表情", u"白天-室内-正常光-表情"),
    34: (u"白天-室内-正常光-不戴眼镜注册，戴近视眼镜认证", u"白天-室内-正常光-脸"),
    35: (u"白天-室内-正常光-不戴眼镜注册，戴墨镜认证", u"白天-室内-正常光-脸"),
    36: (u"白天-室内-正常光-戴近视眼镜注册，不戴眼镜认证", u"白天-室内-正常光-脸"),
    37: (u"白天-室内-正常光-戴近视眼镜注册，戴墨镜认证", u"白天-室内-正常光-脸"),
    38: (u"晚上-室内-正常光-夜晚路演区沙发位置", u"晚上室内正常光"),
    39: (u"晚上-室内-正常光-七楼过道", u"晚上室内正常光"),
    40: (u"晚上-室内-正常光-701健身区域", u"晚上室内正常光"),
    41: (u"晚上-室内-正常光-平躺（路演区域沙发位置）", u"晚上室内正常光"),
    42: (u"晚上-室内-正常光-侧躺（路演区域沙发位置）", u"晚上室内正常光"),
    43: (u"晚上-室内-暗光-夜晚路演区沙发位置（19：00左右关灯）", u"晚上室内暗光"),
    44: (u"晚上-室内-暗光-7楼710的客梯间（关灯后）", u"晚上室内暗光"),
    45: (u"晚上-室内-暗光-720的4人间关灯后", u"晚上室内暗光"),
    46: (u"晚上-室内-暗光-平躺（720的4人间关灯后）", u"晚上室内暗光"),
    47: (u"晚上-室内-暗光-侧躺（720的4人间关灯后）", u"晚上室内暗光"),
    48: (u"晚上-室外-暗光-海翔楼下空旷处（品骏快递）（人物背景无灯光）",
         u"晚上室外暗光"),
    49: (u"晚上-室外-暗光-海翔楼下上坡处路灯下（广州银行）", u"晚上室外暗光"),
    50: (u"晚上-室外-强光-海翔楼下上坡处路灯下（广州银行）（面朝路灯）",
         u"晚上室外强光"),
}


def count(datas, values):
    '''
    生成统计的用例
    '''
    total_number = compare_number = live_number = success_number = \
        test_number = 0
    # print(datas)

    for num, case_name, total, compare, live, success, test, r1, r2, r3 in \
            datas:
        if num in values:
            total_number += total
            compare_number += compare
            live_number += live
            success_number += success
            test_number += test

    compare, live, user = convert_result(
        compare_number, live_number, total_number, success_number, test_number)

    return ["====", maps[values[0]][0], total_number, compare_number,
            live_number, success_number, test_number, compare, live, user]


def convert_result(compare_number, live_number, total_number, success_number,
                   test_number):

    compare = 0 if total_number == 0 else float(compare_number) / total_number
    compare = 0 if not compare else "{0:.5f}%".format(compare * 100)
    live = 0 if total_number == 0 else float(live_number) / total_number
    live = 0 if not live else "{0:.5f}%".format(live * 100)
    user = 0 if test_number == 0 else float(success_number) / test_number
    user = 0 if not user else "{0:.5f}%".format(user * 100)
    return compare, live, user


def produce_xls(results, output):
    tag = old_tag = None
    values = []
    datas = [title, ]

    for i in range(1, len(maps) + 1):

        total_number = compare_number = live_number = success_number = \
            test_number = 0
        old_tag = tag
        tag = maps[i][1]

        # 用例标签与上一用例不一致时，需要对前面用例进行汇总
        if (old_tag is not None) and values and old_tag != tag:
            datas.append(count(datas, values))
            values = []
        values.append(i)

        # 没有数据的生成空表,有数据则统计
        if i not in results:
            datas.append([i, maps[i][1], 0, 0, 0, 0, 0, 0, 0, 0, ])
        else:
            for total, compare, live, success, test in results[i]:
                total_number += total
                compare_number += compare
                live_number += live
                success_number += success
                test_number += test

            compare, live, user = convert_result(
                compare_number, live_number, total_number, success_number,
                test_number)

            datas.append(
                [i, maps[i][0], total_number, compare_number, live_number,
                 success_number, test_number, compare, live, user])

        # 最后的用例需要进行汇总
        if i == len(maps):
            datas.append(count(datas, values))
            values = []

    try:
        writer = pandas.ExcelWriter(output)
        df = pandas.DataFrame(datas)
        df.to_excel(writer, sheet_name='output', index=False)
        writer.save()
    except IOError:
        print("please close the output file!")


def check_directory(name):
    if Path(name).exists():
        print("{0} Exists，Now Delete it!".format(name))
        try:
            shutil.rmtree(name)
            time.sleep(0.5)
        except Exception as info:
            print('Error: shutil.rmtree {}'.format(name))
            print(info)
            traceback.print_exc()
            print('Please close file and directories and continue...')

    print("mkdir {0} .".format(name))
    Path(name).mkdir(parents=True, exist_ok=True)


def copy_files_by_types(src, dst, types="csv,py",
                        directories=None, one_directory=True):
    '''
    拷贝指定扩展名的文件从源目录src到目的目录dst。
    directories: 是否指定目录，多个目录用逗号分隔。
    one_directory：是否拷贝到一个目录，选择为False会建立目录层次。

    示例：

    copy_files_by_types(r"d:\tmp", r"d:\tmp2", types="csv,py",
        directories=None, one_directory=False)

    copy_files_by_types(r"d:\tmp", r"d:\tmp2", types="csv,py,pdf",
        one_directory=False, directories="back,test")
    '''

    check_directory(dst)

    p = Path(src)
    for file_ext in types.split(','):
        for file_name in p.glob('**/*.{0}'.format(file_ext)):
            # print(file_name)

            if directories is not None:
                flag = False
                for directory in directories.split(','):
                    if os.sep + directory + os.sep in str(file_name):
                        flag = True
                if not flag:
                    continue

            if not one_directory:

                dirname = str(file_name.parent).replace(src, dst)
                dst_filename = "{}{}{}".format(
                    dirname, os.sep, file_name.name)

                if not Path(dirname).exists():
                    print("mkdir {}".format(dirname))
                    Path(dirname).mkdir(parents=True, exist_ok=True)
            else:
                dst_filename = "{}{}{}".format(
                    dst, os.sep, Path(file_name).name)

            print("Copying {} to {}".format(file_name, dst_filename))
            shutil.copyfile(str(file_name), dst_filename)
            

def count_number_by_filetypes(directory, file_types, output=False):
    '''
    统计用户目录directory的用例目录下的指定类型文件的个数。
    可以指定多种文件类型。
    output为True时会在屏幕输出。
    比如：count_number_by_filetypes(r'd:\tmp3',"jpg,pdf", output=True)
    '''
    datas = {}
    for file_ext in file_types.split(','):
        datas[file_ext] = count_number_by_filetype(directory, file_ext, output)
    return datas

def count_number_by_filetype(directory, file_type, output=False):
    '''
    统计用户目录directory的用例目录下的指定类型文件的个数。
    output为True时会在屏幕输出。
    比如：count_number_by_filetypes(r'd:\tmp3',"jpg", output=True)
    '''    
    datas = {}
    dirs = glob.glob("{0}/*/".format(directory))
    
    if output:
        print('\n', file_type, ':\n')
    
    for dir_ in (dirs):
        files = glob.glob("{0}/*.{1}".format(dir_, file_type))
        datas[int(dir_.split(os.sep)[-2].lstrip('0'))] = len(files)         
    
    for seq in range(1,len(maps) + 1):         
        if seq not in datas:
            datas[seq] = 0
        if output:
            print(datas[seq])
            
    return datas            

if __name__ == '__main__':
    datas = count_number_by_filetypes(r'd:\tmp3',"jpg,pdf", output=True)
