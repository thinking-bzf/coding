# 获取字符串中指定字符最后一次出现的位置
def find_last(string, str):
    last_position = -1
    while True:
        position = string.find(str, last_position+1)
        if position == -1:
            return last_position
        last_position = position
