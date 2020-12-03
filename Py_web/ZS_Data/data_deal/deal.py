
import numpy as np
from string import digits
from datetime import datetime
import pandas as pd
import os
# dic={"数据框架字段简称":"数据库框架字段名称"}
# dic1={"数据库框架字段名称":"数据库框架字段简称"}
# cjdic={"数据库成绩字段简称":[源数据中该简称所有可能出现的全称]}
# qtdic={"数据库除成绩和投档单外的字段简称":[源数据中该简称所有可能出现的全称]}
cjdic = {
    'GKCJX01': ['语文', '语文成绩', '语文（含附加分）'],
    'GKCJX02': ['数学', '理科数学', '数学理', '数学成绩', '数学（含附加分）'],
    'GKCJX02X': ['文科数学', '数学文'],
    'GKCJX03': ['外语', '英语', '英语成绩', '外语成绩'],
    'GKCJX04': ['物理', '物理选测'],
    'GKCJX05': ['化学', '化学选测'],
    'GKCJX06': ['生物', '生物选测'],
    'GKCJX07': ['政治', '政治必测'],
    'GKCJX08': ['历史', '历史必测'],
    'GKCJX09': ['地理', '地理必测'],
    'GKCJX10': ['技术'],
    'GKCJX11': ['统考美术成绩', '美术专业分', '美术总分', '艺体专业成绩', '美术统考总分', '美术与设计学类', '美术本科统考成绩', '美术'],
    'GKCJX12': ['综合', '综合成绩', '理科综合', '综合/对口专业', '文综/理综'],
    'GKCJX12X': ['文科综合'],
    'GKCJX13': ['外语听力'],
    # 'GKCJX14': ['外语口试', '口语合格', '外语口试成绩', '英语口试', '外语口语','英语口试成绩']
}

qtdic = {
    'KSH': ['KSH'],
    'ZKZH': ['ZKZH'],
    'XM': ['XM'],
    'XBDM': ['XBDM'],
    'CSNY': ['CSNY', 'CSRQ'],
    'ZZMMDM': ['ZZMMDM'],
    'MZDM': ['MZDM'],
    'KSLBDM': ['KSLBDM'],
    'ZXDM': ['BYXXDM', 'ZXDM'],
    'ZXMC': ['BYXXMC', 'ZXMC'],
    'WYYZDM': ['WYYZDM'],
    'HKDJ': ['HKDJ'],
    'BMDW': ['BMDW'],
    'KSTZ': ['KSTZ'],
    'XTDW': ['考生系统单位'],
    'DQDM': ['DQDM'],
    'SFZH': ['ZJHM', 'SFZH'],
    'JTDZ': ['TXDZ', 'JTDZ'],
    'YZBM': ['YZBM'],
    'LXDH': ['LXDH', 'LXSJ'],
    'HKKH': ['HKKH'],
    'KSTC': ['KSTC'],
    'KSJLHCF': ['KSJLHCF'],
    'WYKS': ['WYKS'],
    'ZSYJ': ['ZSYJ'],
    'KSLXDM': ['KSLXDM'],
    'SJR': ['SJR'],
    'YSJZDM': ['YSJZDM'],
    'WYTL': ['WYTL'],
    'PCDM': ['PCDM', 'PCDM_y'],
    'KLDM': ['KLDM', 'KLDM_y'],
    'TDDW': ['TDDWDM'],
    'JHXZ': ['JHXZDM'],
    # 'TDCJ': ['TDCJ'],
    'CJ': ['CJ'],
    'TDZY': ['TDZY']
}
dic = {
    'KSH': '考生号',
    'ZKZH': '准考证号',
    'XM': '姓名',
    'XBDM': '性别',
    'CSNY': '出生年月',
    'ZZMMDM': '政治面貌',
    'MZDM': '民族',
    'KSLBDM': '考生类别',
    'XSLB': '学生类别',
    'ZXDM': '中学代码',
    'ZXMC': '中学名称',
    'WYYZDM': '外语语种代码',
    'HKDJ': '会考等级',
    'BMDW': '报名单位',
    'KSTZ': '考生特征',
    'XTDW': '考生系统单位',
    'DQDM': '地区代码',
    'DQDMMC': '地区代码名称',
    'SFZH': '身份证号',
    'JTDZ': '家庭地址',
    'YZBM': '邮政编码',
    'LXDH': '联系电话',
    'HKKH': '会考考号',
    'KSTC': '考生特长',
    'KSJLHCF': '考生奖励或处分',
    'WYKS': '外语口试',
    'ZSYJ': '政审意见',
    'KSLXDM': '考试类型代码',
    'SJR': '收件人',
    'YSJZDM': '应试卷种代码',
    'WYTL': '外语听力',
    'PCDM': '批次代码',
    'KLDM': '科类代码',
    'TDDW': '投档单位',
    'JHXZ': '计划性质',
    'CJ': '成绩',
    'TDCJ': '投档成绩',
    'TDZY': '投档志愿',
    'GKCJX01': '语文',
    'GKCJX02': '数学',
    'GKCJX02X': '文科数学',
    'GKCJX03': '外语',
    'GKCJX04': '物理',
    'GKCJX05': '化学',
    'GKCJX06': '生物',
    'GKCJX07': '政治',
    'GKCJX08': '历史',
    'GKCJX09': '地理',
    'GKCJX10': '技术',
    'GKCJX11': '统考美术成绩',
    'GKCJX12': '综合',
    'GKCJX12X': '文科综合',
    'GKCJX13': '外语听力',
    # 'GKCJX14': '外语口试',
    'BM': '通知书编号',
    'LQZY': '录取专业',
    'XY': '学院',
    'SYD': '生源地',
    'PC': '批次',
    'KL': '科类'
}

dic1 = {
    '考生号': 'KSH',
    '准考证号': 'ZKZH',
    '姓名': 'XM',
    '性别': 'XBDM',
    '出生年月': 'CSNY',
    '政治面貌': 'ZZMMDM',
    '民族': 'MZDM',
    '考生类别': 'KSLBDM',
    '学生类别': 'XSLB',
    '中学代码': 'ZXDM',
    '中学名称': 'ZXMC',
    '外语语种代码': 'WYYZDM',
    '会考等级': 'HKDJ',
    '报名单位': 'BMDW',
    '考生特征': 'KSTZ',
    '考生系统单位': 'XTDW',
    '地区代码': 'DQDM',
    '地区代码名称': 'DQDMMC',
    '身份证号': 'SFZH',
    '家庭地址': 'JTDZ',
    '邮政编码': 'YZBM',
    '联系电话': 'LXDH',
    '会考考号': 'HKKH',
    '考生特长': 'KSTC',
    '考生奖励或处分': 'KSJLHCF',
    '外语口试': 'GKCJX14',
    '政审意见': 'ZSYJ',
    '考试类型代码': 'KSLXDM',
    '收件人': 'SJR',
    '应试卷种代码': 'YSJZDM',
    '外语听力': 'GKCJX13',
    '批次代码': 'PCDM',
    '科类代码': 'KLDM',
    '投档单位': 'TDDW',
    '计划性质': 'JHXZ',
    '成绩': 'CJ',
    '投档成绩': 'TDCJ',
    '投档志愿': 'TDZY',
    '语文': 'GKCJX01',
    '数学': 'GKCJX02',
    '文科数学': 'GKCJX02X',
    '外语': 'GKCJX03',
    '物理': 'GKCJX04',
    '化学': 'GKCJX05',
    '生物': 'GKCJX06',
    '政治': 'GKCJX07',
    '历史': 'GKCJX08',
    '地理': 'GKCJX09',
    '技术': 'GKCJX10',
    '统考美术成绩': 'GKCJX11',
    '综合成绩': 'GKCJX12',
    '文科综合': 'GKCJX12X',
    '外语听力': 'GKCJX13',
    '通知书编号': 'BM',
    '录取专业': 'LQZY',
    '学院': 'XY',
    '生源地': 'SYD',
    '批次': 'PC',
    '科类': 'KL'
}


def file_dirs(file_path):
    List = []
    for root, dirs, files in os.walk(file_path):
        if len(dirs) != 0:
            List += dirs
    return List


def file_files(file_path):
    List = []
    for root, dirs, files in os.walk(file_path):
        if len(files) != 0:
            List += files
    return List


def cuts(dic, Dt, In, x):
    if '1' <= x[0] <= '6' or x[0] == ' ':
        Dt['XY'].at[i] = dic[x[1:x.index(In)]]
        Dt['LQZY'].at[i] = x[1:x.index(In)]
    else:
        Dt['XY'].at[i] = dic[x[0:x.index(In)]]
        Dt['LQZY'].at[i] = x[0:x.index(In)]


def deal_FirstZY(DF):
    # 制作第一张数据透视表作为基础
    dv = pd.pivot_table(
        DF, values="XM", index="ZYDH1",
        aggfunc="count").reset_index().rename(columns={"ZYDH1": "ZYDH"})
    dv = dv.rename(columns={"XM": "志愿1"})
    # 生成另外五张数据透视表并拼接
    List = ["ZYDH2", "ZYDH3", "ZYDH4", "ZYDH5", "ZYDH6"]
    i = 2
    for s in List:
        DF[s] = DF[s].fillna('空白')
        dv1 = pd.pivot_table(
            DF, values="XM", index=s,
            aggfunc="count").reset_index().rename(columns={s: "ZYDH"})
        dv1 = dv1.rename(columns={"XM": "志愿" + str(i)})
        i += 1
        dv = pd.merge(dv, dv1, on="ZYDH", how="outer")
    dv = dv.fillna(0)
    dv["志愿指数"] = dv.iloc[:, 1:7].apply(lambda x: x["志愿1"] + x["志愿2"] * 0.8 +
                                       (x["志愿3"] + x["志愿4"]) * 0.6 +
                                       (x["志愿5"] + x["志愿6"]) * 0.4,
                                       axis=1)
    # 排序并在输出文件前对文件路径补充
    dv = dv[dv['ZYDH'] != '空白']
    dv = dv.sort_values(by="志愿指数", ascending=False)
    return dv


def data_clean(result_path, file_name, original_path):
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    zyml = pd.read_excel(
        "File/static/2020专业学院名称.xlsx")
    zydic = {}
    for i in zyml.index:
        zydic[zyml['招生专业目录'].at[i]] = zyml['所属学院'].at[i]

    result = pd.DataFrame([['生源地', '批次', '科类', '考生号', '姓名', '联系电话', '收件人', '家庭住址', '', '录取专业', '学院', '邮政编码']], index=[
                          0], columns=['SYD', 'PC', 'KL', 'KSH', 'XM', 'LXDH', 'SJR', 'JTDZ', 'TXDZ', 'LQZY', 'XY', 'YZBM'])
    DT = pd.DataFrame([['生源地', '批次', '科类', '考生号', '姓名', '学院', '录取专业', '家庭住址', '', '联系电话', '收件人', '邮政编码']], index=[
                      0], columns=['SYD', 'PC', 'KL', 'KSH', 'XM', 'XY', 'LQZY', 'JTDZ', 'TXDZ', 'LXDH', 'SJR', 'YZBM'])

    original_file = os.path.join(original_path, file_name+'.xlsx')
    strl = file_name.split()
    of = pd.ExcelFile(original_file)
    sheetlist = of.sheet_names
    tddxx = pd.read_excel(original_file,
                          sheet_name='t_tddxx', dtype='object')
    if "T_BMK" in sheetlist:
        df = pd.read_excel(
            original_file, sheet_name='T_BMK', dtype='object')
    else:
        df = pd.read_excel(
            original_file, sheet_name='T_TDD', dtype='object')
    re = pd.DataFrame(df[['KSH', 'XM', 'SJR', 'YZBM']])
    if 'JTDZ' in df.columns:
        re['JTDZ'] = df['JTDZ']
    elif 'TXDZ' in df.columns:
        re['TXDZ'] = df['TXDZ']
    if 'LXDH' in df.columns:
        if 'LXSJ' in df.columns:
            re['LXDH'] = df['LXSJ']
            for i in df.index:
                if re['LXDH'].isnull().at[i] and ~df['LXDH'].isnull().at[i]:
                    re['LXDH'].at[i] = df['LXDH'].at[i]
        else:
            re['LXDH'] = df['LXDH']
    dv = pd.merge(re, tddxx[['KSH', 'LQZY']], on='KSH')
    res = pd.concat([DT, dv], ignore_index=True)
    for i in res.iloc[1:, :].index:
        res["SYD"].at[i] = strl[0]
        res['PC'].at[i] = strl[1]
        res['KL'].at[i] = strl[2]
    for i in res.iloc[1:, :].index:
        res["SYD"].at[i] = strl[0]
        LQZY = res['LQZY'].at[i]
        if '(' in LQZY and '定向' not in LQZY and '中外合作办学' not in LQZY:
            cuts(zydic, res, '(', LQZY)
        elif '（' in LQZY and '定向' not in LQZY and '中外合作办学' not in LQZY:
            cuts(zydic, res, '（', LQZY)
        elif '#' in LQZY and '定向' not in LQZY and '中外合作办学' not in LQZY:
            cuts(zydic, res, '#', LQZY)
        else:
            if '1' <= LQZY[0] <= '6' or LQZY[0] == ' ':
                res['XY'].at[i] = zydic[LQZY[1:]]
                res['LQZY'].at[i] = LQZY[1:]
            else:
                res['XY'].at[i] = zydic[LQZY]
    res = res.iloc[1:, :].sort_values(by=['XY', 'LQZY', 'XM'])
    # result = pd.concat([result,res.iloc[1:,:]],ignore_index=True)
    res['TXDZ'] = res['TXDZ'].fillna('')
    res['JTDZ'] = res['JTDZ'].fillna('')
    res['JTDZ'] = res['TXDZ']+res['JTDZ']
    res = res.drop(columns='TXDZ')
    res.to_excel(os.path.join(result_path, file_name+'录取汇总.xlsx'), index=False)


def clean_concat(path):
    List = file_files(path)
    result = pd.read_excel(os.path.join(path, List[0]), dtype='object')
    for x in List[1:]:
        join = pd.read_excel(os.path.join(path, x), dtype='object')
        result = pd.concat([result, join], ignore_index=True).drop_duplicates()
    return result


# 单元素的查找和复制
def findcopy(dic, x, target, copy):
    for k, v in dic.items():
        if x in v:
            target[k] = copy[x]
            break


def original_merge(original_Dirpath):

    # 字典变量说明:
    # dic2={"源数据成绩字段简称":"源数据成绩字段名称"}

    # tdddic={"数据库投档单相关信息的字段简称":[源数据中该简称所有可能出现的全称]}
    dic2 = {}  # 待导入
    kldic = {}
    pcdic = {}
    zydic = {}
    dqdic = {}
    tdddic = {}

    # 将数据库结构字典做成表格并转置变成框架
    s = pd.Series(dic)
    DataStruct = pd.DataFrame(s)
    DT = DataStruct.T
    result = DT

    zyml = pd.read_excel(
        r"File\static\2020专业学院名称.xlsx")
    for i in zyml.index:
        zydic[zyml['招生专业目录'].at[i]] = zyml['所属学院'].at[i]
    List = file_files(original_Dirpath)
    result = DT.iloc[1:, :]

    for x in List:
        strl = x.strip(".xlsx").split()
        File_path = os.path.join(original_Dirpath, x)
        of = pd.ExcelFile(File_path)
        sheetlist = of.sheet_names
        tddxx = pd.read_excel(File_path, sheet_name='t_tddxx', dtype='object')
        if "T_BMK" in sheetlist:
            # 导入BMK文件并作为df   表格对象
            bmk = pd.read_excel(File_path, sheet_name='T_BMK', dtype='object')
            # 导入TDD文件作为tdd表格对象
            tdd = pd.read_excel(File_path, sheet_name='T_TDD', dtype='object')
            df = pd.merge(bmk, tdd, on='KSH')
        else:
            df = pd.read_excel(File_path, sheet_name='T_TDD', dtype='object')

        # 成绩代码说明文件导入
        cjdmsm = pd.read_excel(
            File_path, sheet_name='TD_CJXDM', dtype='object')
        # 批次代码文件导入
        pcdm = pd.read_excel(File_path, sheet_name='TD_PCDM', dtype='object')
        # 科类代码文件导入
        kldm = pd.read_excel(File_path, sheet_name='TD_KLDM', dtype='object')
        # 地区代码文件导入
        dqdm = pd.read_excel(File_path, sheet_name='TD_DQDM', dtype='object')

        # 成绩说明字典初始化
        dic2 = {}
        # 导入成绩代码解释
        for i in cjdmsm.index:
            dic2["GKCJX"+str(cjdmsm["CJXDM"].at[i])
                 ] = cjdmsm["CJXMC"].at[i].replace(u'\u3000', u'')

        dqdic = {}
        for i in dqdm.index:
            dqdic[dqdm['DQDM'].at[i]] = dqdm['DQMC'].at[i]
        # kldic = {}
        # for i in kldm.index:
        #     kldic[kldm['KLDM'].at[i]] = kldm['KLMC'].at[i]

        # 新建新表并增加一列以填充长度
        dv = pd.DataFrame(df["KSH"])
        # df文件字段匹配
        cols = list(df.columns)
        for col in cols:
            findcopy(qtdic, col, dv, df)

        # 成绩代码匹配
        for k, v in dic2.items():
            for s, t in cjdic.items():
                if v in t:
                    dv[s] = df[k]
                    break

        if 'LXDH' in df.columns:
            if 'LXSJ' in df.columns:
                dv['LXDH'] = df['LXSJ']
                for i in df.index:
                    if dv['LXDH'].isnull().at[i] and ~df['LXDH'].isnull().at[i]:
                        dv['LXDH'].at[i] = df['LXDH'].at[i]
            else:
                dv['LXDH'] = df['LXDH']

        # dv['KSH'] = dv['KSH'].astype('string_')
        # tddxx['KSH'] = tddxx['KSH'].astype('string_')
        dv = pd.merge(dv, tddxx[['KSH', 'LQZY', 'TDCJ']], on='KSH')
        # dv['KSH']=dv['KSH'].astype('int64')
        # 将dv新表中的内容与框架表的字段匹配 实现按照框架表排序
        re = pd.merge(DT.T,
                      dv.T,
                      left_index=True,
                      right_index=True,
                      how="left",
                      sort=False).T

        for i in re.iloc[1:, :].index:
            re["SYD"].at[i] = strl[0]
            LQZY = re['LQZY'].at[i]
            if '(' in LQZY and '定向' not in LQZY and '中外合作办学' not in LQZY:
                cuts(re, '(', LQZY)
            elif '（' in LQZY and '定向' not in LQZY and '中外合作办学' not in LQZY:
                cuts(re, '（', LQZY)
            elif '#' in LQZY and '定向' not in LQZY and '中外合作办学' not in LQZY:
                cuts(re, '#', LQZY)
            else:
                if '1' <= LQZY[0] <= '6' or LQZY[0] == ' ':
                    re['XY'].at[i] = zydic[LQZY[1:]]
                    re['LQZY'].at[i] = LQZY[1:]
                else:
                    re['XY'].at[i] = zydic[LQZY]

        # for i in pcdic:
        #     print(pcdic[i])
        re['GKCJX02'] = re['GKCJX02'].fillna(0)
        re['GKCJX02X'] = re['GKCJX02X'].fillna(0)
        re['GKCJX12'] = re['GKCJX12'].fillna(0)
        re['GKCJX12X'] = re['GKCJX12X'].fillna(0)
        # re['CJ']=re['CJ'].fillna(0)
        # re['CJX']=re['CJX'].fillna(0)
        for i in re.iloc[1:, :].index:
            if re['DQDM'].at[i] in dqdic.keys():
                re['DQDMMC'].at[i] = dqdic[str(re['DQDM'].at[i])]
            else:
                re['DQDMMC'].at[i] = re['DQDM'].at[i]
            if not any(str(re['GKCJX02'].at[i])):
                re['GKCJX02'].at[i] = 0
            if not any(str(re['GKCJX02X'].at[i])):
                re['GKCJX02X'].at[i] = 0
            if not any(str(re['GKCJX12'].at[i])):
                re['GKCJX12'].at[i] = 0
            if not any(str(re['GKCJX12X'].at[i])):
                re['GKCJX12X'].at[i] = 0
            # re['KL'].at[i] = kldic[re['KLDM'].at[i]]
            # re['PC'].at[i] = pcdic[re['PCDM'].at[i]]
            re['GKCJX02'].at[i] = max(
                re['GKCJX02'].at[i], re['GKCJX02X'].at[i])
            re['GKCJX12'].at[i] = max(
                re['GKCJX12'].at[i], re['GKCJX12X'].at[i])
            # re['CJ'].at[i] = max(re['CJX'].at[i], re['CJ'].at[i])
            # re['CJ'].at[i]=re['TDCJ'].at[i]//1
            re['KL'].at[i] = strl[2]
            re['PC'].at[i] = strl[1]

        if List.index(x) != 0:
            result = pd.concat([result, re.iloc[1:, :]],
                               ignore_index=True).drop_duplicates()
        else:
            result = pd.concat([result, re],
                               ignore_index=True).drop_duplicates()
        print(x + " completed")

        result = result.drop(columns=['GKCJX02X', 'GKCJX12X'])
    return result

    # print("All Completed")
