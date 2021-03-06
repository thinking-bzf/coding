# 字典变量说明:
# dic={"数据框架字段简称":"数据库框架字段名称"}
# dic1={"数据库框架字段名称":"数据库框架字段简称"}
# dic2={"源数据成绩字段简称":"源数据成绩字段名称"}
# cjdic={"数据库成绩字段简称":[源数据中该简称所有可能出现的全称]}
# qtdic={"数据库除成绩和投档单外的字段简称":[源数据中该简称所有可能出现的全称]}
# tdddic={"数据库投档单相关信息的字段简称":[源数据中该简称所有可能出现的全称]}
dic = {
    'KSH': '考生号',
    'ZKZH': '准考证号',
    'XM': '姓名',
    'XBDM': '性别',
    'CSNY': '出身年月',
    'ZZMMDM': '政治面貌',
    'MZDM': '民族',
    'KSLBDM': '考生类别',
    'ZXDM': '中学代码',
    'ZXMC': '中学名称',
    'WYYZDM': '外语语种代码',
    'HKDJ': '会考等级',
    'BMDW': '报名单位',
    'KSTZ': '考生特征',
    'XTDW': '考生系统单位',
    'DQDM': '地区代码',
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
    'GKCJX14': '外语口试',
    'BM': '通知书编号',
    'KL': '科类',
    'LQZY': '录取专业',
    'XY': '学院',
    'SYD': '生源地',
    'PC': '批次'
}

dic1 = {
    '考生号': 'KSH',
    '准考证号': 'ZKZH',
    '姓名': 'XM',
    '性别': 'XBDM',
    '出身年月': 'CSNY',
    '政治面貌': 'ZZMMDM',
    '民族': 'MZDM',
    '考生类别': 'KSLBDM',
    '中学代码': 'ZXDM',
    '中学名称': 'ZXMC',
    '外语语种代码': 'WYYZDM',
    '会考等级': 'HKDJ',
    '报名单位': 'BMDW',
    '考生特征': 'KSTZ',
    '考生系统单位': 'XTDW',
    '地区代码': 'DQDM',
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
    '通知书编号': 'BM',
    '科类': 'KL',
    '录取专业': 'LQZY',
    '学院': 'XY',
    '生源地': 'SYD',
    '批次': 'PC'
}

dic2 = {}  # 待导入
kldic = {}
pcdic = {}

cjdic = {
    'CJ': ['总分', '原始总分'],
    'GKCJX01': ['语文', '语文成绩'],
    'GKCJX02': ['数学', '理科数学'],
    'GKCJX02X': ['文科数学'],
    'GKCJX03': ['外语', '英语'],
    'GKCJX04': ['物理'],
    'GKCJX05': ['化学'],
    'GKCJX06': ['生物'],
    'GKCJX07': ['政治'],
    'GKCJX08': ['历史'],
    'GKCJX09': ['地理'],
    'GKCJX10': ['技术'],
    'GKCJX11': ['统考美术成绩', '美术专业分','艺体专业成绩','美术统考总分'],
    'GKCJX12': ['综合', '综合成绩', '理科综合'],
    'GKCJX12X': ['文科综合'],
    'GKCJX13': ['外语听力'],
    'GKCJX14': ['外语口试', '口语合格', '外语口试成绩', '英语口试','外语口语'],
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
    'JTDZ': ['TXDZ'],
    'YZBM': ['YZBM'],
    'LXDH': ['LXDH'],
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
    'TDCJ': ['TDCJ']
}
tdddic = {}
import os
from string import digits
from dbfread import DBF
import pandas as pd
import numpy as np


# 单元素的查找和复制
def findcopy(dic, x, target, copy):
    for k, v in dic.items():
        if x in v:
            target[k] = copy[col]
            break


# 将数据库结构字典做成表格并转置变成框架
s = pd.Series(dic)
DataStruct = pd.DataFrame(s)
DT = DataStruct.T
result = DT


def file_dirs(file_path):
    List = []
    for root, dirs, files in os.walk(file_path):
        if len(dirs) != 0:
            List += dirs
    return List


List = file_dirs(r"C:\Py_Excel\Notebook\总表拼接")

for x in List:
    path = "C:/Py_Excel/Notebook/总表拼接/"
    path += x
    if '浙江' in x or '上海' in x:
        # 导入BMK文件并作为df表格对象
        table = DBF(os.path.join(path, "T_BMK.dbf"), encoding="GBK")
        bmk = pd.DataFrame(iter(table))

        # 导入TDD文件作为tdd表格对象
        td = DBF(os.path.join(path, "T_TDD.dbf"), encoding="GBK")
        tdd = pd.DataFrame(iter(td))
        df = pd.merge(bmk, tdd, on='KSH')
    # elif '上海' in x:
    #     table = DBF(os.path.join(x,"T_BMK.dbf"), encoding="GBK")
    #     df = pd.DataFrame(iter(table))
    else:
        # try:
        table = DBF(os.path.join(path, "T_TDD.dbf"),
                    encoding="GBK",
                    char_decode_errors='ignore')
        # except:
        #     table = DBF(os.path.join(x,"T_TDD.dbf"), encoding="UTF-8")
        df = pd.DataFrame(iter(table))

    # 导入CJXDM文件作为cjdmsm表格对象
    cjdm = DBF(os.path.join(path, "TD_CJXDM.dbf"),
               encoding="GBK",
               char_decode_errors='ignore')

    cjdmsm = pd.DataFrame(iter(cjdm))
    pcdmdbf = DBF(os.path.join(path, "TD_PCDM.dbf"),
                  encoding="GBK",
                  char_decode_errors='ignore')
    pcdm = pd.DataFrame(iter(pcdmdbf))
    kldmdbf = DBF(os.path.join(path, "TD_KLDM.dbf"),
                  encoding="GBK",
                  char_decode_errors='ignore')
    kldm = pd.DataFrame(iter(kldmdbf))

    dic2 = {}  # 每次循环初始化
    # 导入成绩代码解释
    for s in cjdmsm.iloc[:, 0]:
        dic2["GKCJX" + s.upper()] = cjdmsm.iloc[np.where(cjdmsm == s)[0],
                                                [1]].values[0][0]

    pcdic = {}
    for i in pcdm.index:
        pcdic[pcdm['PCDM'].at[i]] = pcdm['PCMC'].at[i]
    kldic = {}
    for i in kldm.index:
        kldic[kldm['KLDM'].at[i]] = kldm['KLMC'].at[i]

    # 新建新表并增加一列以填充长度
    dv = pd.DataFrame(df["KSH"])
    # df文件字段匹配
    cols = list(df.columns)
    for col in cols:
        findcopy(qtdic, col, dv, df)
    # 投档单字段匹配
    # col2s = list(tdd.columns)
    # for col in col2s:
    #     findcopy(tdddic, col, dv, tdd)

    # 成绩代码匹配
    for k, v in dic2.items():
        for s, t in cjdic.items():
            if v in t:
                dv[s] = df[k]
                break

    # 将dv新表中的内容与框架表的字段匹配 实现按照框架表排序
    re = pd.merge(DT.T,
                  dv.T,
                  left_index=True,
                  right_index=True,
                  how="left",
                  sort=False).T
    #生源地填充x 去掉数字
    remove_digits = str.maketrans('', '', digits)
    res = x.translate(remove_digits)
    for i in re.index:
        re["SYD"].at[i] = res

    # for i in pcdic:
    #     print(pcdic[i])
    for i in re.iloc[1:-1, :].index:
        re['KL'].at[i] = kldic[re['KLDM'].at[i]]
        re['PC'].at[i] = pcdic[re['PCDM'].at[i]]
        re['GKCJX02'].at[i] = max(re['GKCJX02'].at[i], re['GKCJX02X'].at[i])
        re['GKCJX12'].at[i] = max(re['GKCJX12'].at[i], re['GKCJX12X'].at[i])

    result = pd.concat([result, re.iloc[1:-1, :]],
                       ignore_index=True).drop_duplicates()

result.to_excel("C:/Py_Excel/Notebook/总表拼接/Total.xlsx")