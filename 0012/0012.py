"""
 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
 当用户输入敏感词语，则用 星号 * 替换，
 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""
import os


def filter(string):
    file_path = os.path.join(os.getcwd(), "filtered_words.txt")
    with open(file_path, "rb") as fd:
        words = fd.read()
    filter_string = words.decode("utf8")
    filter_words = filter_string.split("\r\n")
    for i in filter_words:
        if i in string:
            string = string.replace(i, "*"*len(i))

    return string


if __name__ == "__main__":
    string = input("请输入内容：")
    res = filter(string)
    print(res)