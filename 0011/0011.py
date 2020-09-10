import os


def filter(string):
    file_path = os.path.join(os.getcwd(), "filtered_words.txt")
    with open(file_path, "rb") as fd:
        words = fd.read()
    filter_string = words.decode("utf8")
    filter_words = filter_string.split("\r\n")
    if any(i in string for i in filter_words):
        return "Freedom"
    else:
        return "Human Rights"


if __name__ == "__main__":
    string = input("请输入内容：")
    res = filter(string)
    print(res)