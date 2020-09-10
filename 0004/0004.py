# 任一个英文的纯文本文件，统计其中的单词出现的个数
import os
import re


def count_words(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    res = {}
    for line in data:
        words = re.sub(r"[.?!,""/]", " ", line)   # 英文中可能出现的，要替换的标点符号
        for word in words.split(" "):
            key = res.get(word, None)
            if key is None:
                res[word] = 1
            else:
                res[word] += 1

    print_res(res)


def print_res(dict):
    for key, value in dict.items():
        print("word:", key, "\tcount:", value)


if __name__ == "__main__":
    file = os.path.join(os.getcwd(), "file")
    count_words(file)
