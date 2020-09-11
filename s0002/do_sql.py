"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
"""
import uuid
import mysql.connector
from s0002.configs.db_config import db_config

# 连接数据库
db = mysql.connector.connect(**db_config)
cursor = db.cursor()

# 建表
create_table_sql = """
CREATE TABLE IF NOT EXISTS `ids`(
    `id` INT(10) AUTO_INCREMENT,
    `number` VARCHAR(40),
    PRIMARY KEY(`id`) USING BTREE
)COMMENT='激活码' ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
cursor.execute(create_table_sql)

# 生成激活码并存入表中
for i in range(200):
    id = uuid.uuid1()
    id = str(id)
    sql = "INSERT INTO `ids`(`number`) values (%s)"
    cursor.execute(sql, (id,))
