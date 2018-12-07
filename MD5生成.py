# coding:utf-8
import hashlib

def get_token(md5str):
    # md5str = "abc"
    # 生成一个md5对象
    m1 = hashlib.md5()
    # 使用md5对象里的update方法md5转换
    m1.update(md5str.encode("utf-8"))
    token = m1.hexdigest()
    return token


md = '927bb7757be0465d87bc2dd05adbc02e'
a = get_token("md")
print(a)