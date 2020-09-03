# 生成200个激活码
import uuid

ids = []

for i in range(200):
    id = uuid.uuid1()
    ids.append(str(id)+"\n")

with open("ids", "w") as fd:
    fd.writelines(ids)
