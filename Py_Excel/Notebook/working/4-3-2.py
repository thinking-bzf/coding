import pandas as pd
df = pd.read_excel(r"C:\Py_Excel\Notebook\working\数据透视表text.xlsx")

#建立数据透视表
dv = pd.pivot_table(df,
                    values="cj",
                    index=["syd", "bz"],
                    columns="kl",
                    aggfunc="min").fillna("/")
dv.to_excel(r"C:\Py_Excel\Notebook\working\result.xlsx")
v1 = pd.read_excel("Notebook/working/result.xlsx")

# 自动填充省份空白格
v1["syd"] = v1["syd"].fillna("m")
s = v1["syd"].at[0]
for i in v1.index:
    if v1["syd"].at[i] == "m":
        v1["syd"].at[i] = s
    else:
        s = v1["syd"].at[i]
drop = ["2018年预科转入", "国家专项", "地方专项", "国家专项（定向阿克苏）", "艺术类", "台湾免试生", "内地高中班"]

# 去掉不需要的几行
# v2 = v1[((v1["bz"] != "2018年预科转入") & (v1["bz"] != "国家专项") &
#          (v1["bz"] != "地方专项") & (v1["bz"] != "国家专项（定向阿克苏）") &
#          (v1["bz"] != "艺术类") & (v1["bz"] != "台湾免试生") &
#          (v1["bz"] != "内地高中班"))].iloc[:, 0:5]
drop = ["2018年预科转入", "国家专项", "地方专项", "国家专项（定向阿克苏）", "艺术类", "台湾免试生", "内地高中班"]
v2 = v1[~v1["bz"].isin(drop)]

v2.sort_values(by="syd", ascending=True)
v2.to_excel("Notebook/working/result.xlsx")
