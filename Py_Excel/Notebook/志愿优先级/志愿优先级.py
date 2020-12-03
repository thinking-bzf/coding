import pandas as pd


def yxj(path):
    a = input("输入文件名:")
    b = input("输入sheet名称:")
    df = pd.read_excel(path + "/" + a, sheet_name=b)
    print("Creating Dataframe...")
    # 制作第一张数据透视表作为基础
    dv = pd.pivot_table(
        df, values="XM", index="ZYDH1",
        aggfunc="count").reset_index().rename(columns={"ZYDH1": "ZYDH"})
    dv = dv.rename(columns={"XM": "志愿1"})

    # 生成另外五张数据透视表并拼接
    List = ["ZYDH2", "ZYDH3", "ZYDH4", "ZYDH5", "ZYDH6"]
    i = 2
    for s in List:
        dv1 = pd.pivot_table(
            df, values="XM", index=s,
            aggfunc="count").reset_index().rename(columns={s: "ZYDH"})
        dv1 = dv1.rename(columns={"XM": "志愿" + str(i)})
        i += 1
        dv = pd.merge(dv, dv1, on="ZYDH", how="outer")
    dv = dv.fillna(0)
    dv["yxj"] = dv.iloc[:, 1:7].apply(lambda x: x["志愿1"] + x["志愿2"] * 0.8 +
                                      (x["志愿3"] + x["志愿4"]) * 0.6 +
                                      (x["志愿5"] + x["志愿6"]) * 0.4,
                                      axis=1)

    # 排序并在输出文件前对文件路径补充
    dv = dv.sort_values(by="yxj", ascending=False)
    if a[-1] != 'x':
        a = path + "/finished/result_of" + a + "x"
    else:
        a = path + "/finished/result_of" + a
    print("Outing file")
    dv.to_excel(a)
    print("Finished")


path = input("请输入文件所在文件夹的绝对路径 分隔符为\"/\":")
x = input("输入exit以结束,任意键继续:")
while (x != "exit"):
    yxj(path)
    x = input("输入exit以结束,任意键继续:")

input('Press <Enter> to exit')
