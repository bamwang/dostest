import requests
import concurrent.futures
import time
import datetime
import random
import re

cookies = {
    "csno": "548318796",
    "csid": "0d27da94cc166ddf678ef2e3b3db6db1",
}

# requests.cookies.cookiejar_from_dict()
# requests.cookies.create_cookie("csno", "548318796", domain="https://www.dospara.co.jp")
# requests.cookies.create_cookie("csid", "0d27da94cc166ddf678ef2e3b3db6db1", domain="https://www.dospara.co.jp")
# cookie_obj = requests.cookies.create_cookie(domain='.www.dospara.co.jp',name='csno',value='548318796')


def f(id, moji, cd=0):
    time.sleep(5)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = "https://www.dospara.co.jp/5cart/cartin_parts.php?mdb=n&qty=1&ic="+id
    product_url = "https://www.dospara.co.jp/5shopping/detail_parts.php?lf=1&ic="+id

    a = requests.get(url, headers=headers, cookies=None)
    if a.status_code == 403:
        raise Exception("403 FORBITTEN")
    if a.status_code == 429:
        cd += random.random()*10+20
        time.sleep(cd)
        print("!!!!" + id)
        return f(id, moji, cd)
    a.encoding = a.apparent_encoding
    if "申し訳ございません" not in a.text and "申し訳ありません" not in a.text:
        print(str(datetime.datetime.now()) + " => " + moji+": "+product_url)
        print(id)
        print(a.text)
        print(a.cookies.get("csno"))
        print(a.cookies.get("csid"))
        noti = requests.post("https://maker.ifttt.com/trigger/pc4u/with/key/dN390pdhTwKRlHT4443oOa", json={ "id":"Udc7d580e086b4e8b7f956638fcb316aa", "value1": "dos bot: %s %s" % (moji, id), "value2": product_url})
        # print(a.cookies.items)
    elif "データメンテナンス" in a.text:
        print(a.text)
        print(id)
        noti = requests.post("https://maker.ifttt.com/trigger/pc4u/with/key/dN390pdhTwKRlHT4443oOa", json={ "id":"Udc7d580e086b4e8b7f956638fcb316aa", "value1": "dos bot: mentainance %s %s" % (moji, id), "value2": product_url})
    else:
        # print(a.text)
        # noti = requests.post("https://maker.ifttt.com/trigger/pc4u/with/key/dN390pdhTwKRlHT4443oOa", json={ "id":"Udc7d580e086b4e8b7f956638fcb316aa", "value1": "dos bot", "value2": product_url})
        # print(noti.status_code)
        pass
    return id


gpu = ['472180', '470290', '471007', '471008']

gpu1 = ['471631', '472733', '471630', '471486', '471487', #'471595', 
        '471594', '471633', '472161', '471077', '471632', '471485', '472221']
gpu2 = ['458108', '469977', '470056', '472480', '469978', '470055', '470054', '470658',
        '470066', '469982', '469981', '469979', '471078', '469240', '469649', '472160']
gpu3 = ['469657', '469318', '469208', '469207', '469205', '469206', '471205', #'470802'
        '469319', '468874', '469335', '469310', '470790', '469336', ] #'468873', '468617' '469309', 
gpu4 = ['468868', '468628', '468631', '468627', '468620', '469631', '469126', '470310', '470388', '471596',
        '468430', '468621', '469147', '468611', '468649', '472481', '468614', '468429', '469925'] #'469630', 
f0 = False
f1 = False
f2 = f3 = f4 = True

r0 = []
r1 = []
r2 = []
r3 = []
r4 = []
exec = concurrent.futures.ThreadPoolExecutor(max_workers=1)
match = "search list:"
if f0:
    match = match+" HDD"
    for r in gpu:
        r0.append(exec.submit(f, r, "HDD"))
if f1:
    match = match+" RTX3060"
    for r in gpu1:
        r1.append(exec.submit(f, r, "RTX3060"))
if f2:
    match = match+" RTX3060Ti"
    for r in gpu2:
        r2.append(exec.submit(f, r, "RTX3060ti"))
if f3:
    match = match+" RTX3070"
    for r in gpu3:
        r3.append(exec.submit(f, r, "RTX3070"))
if f4:
    match = match+" RTX3080"
    for r in gpu4:
        r4.append(exec.submit(f, r, "RTX3080"))
print(match)
while(1):
    # print("wait for 30s")
    time.sleep(30)
    if f:
        for r in r0:
            if r.done():
                r = exec.submit(f, r.result(), "HDD")
    if f1:
        for r in r1:
            if r.done():
                r = exec.submit(f, r.result(), "RTX3060")
    if f2:
        for r in r2:
            if r.done():
                r = exec.submit(f, r.result(), "RTX3060ti")
    if f3:
        for r in r3:
            if r.done():
                r = exec.submit(f, r.result(), "RTX3070")
    if f4:
        for r in r4:
            if r.done():
                r = exec.submit(f, r.result(), "RTX3080")

