# coding=utf-8

import requests

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}
url = "https://passport.cnblogs.com/user/signin"
s = requests.session()
r = s.get(url,headers=headers)
print(s.cookies)
print(r.cookies)
print(r.json())
