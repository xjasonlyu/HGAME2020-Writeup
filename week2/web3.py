import html
import base64
import requests

functionMap = {
    'base64_encode': lambda x: base64.b64decode(x.encode()).decode(),
    'encrypt': lambda x: ''.join([ chr(ord(i) - 1) for i in x ]),
    'strrev': lambda x: x[::-1],
    'str_rot13': lambda x: x.translate(str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")),
    }

s = requests.Session()

def getOutput():
    r = s.get('http://17f37c65aa.php.hgame.n3ko.co/')
    r.raise_for_status()
    return html.unescape(r.text.split('\n')[4][:-4])

def getCode():
    r = s.get('http://17f37c65aa.php.hgame.n3ko.co/mycode')
    r.raise_for_status()
    code = ''
    for i in r.text.split('\n'):
        if i[:4] == 'echo':
            code = i
            break
    # print(code)
    code = code[5:code.find('($_SERVER')]
    return code.split('(')

def postToken(token):
    r = s.post('http://17f37c65aa.php.hgame.n3ko.co/', data = {'token': token})
    r.raise_for_status()
    return r.text

def calcToken(output, code):
    for c in code:
        # print(c, repr(output))
        f = functionMap[c]
        output = f(output)
    return output

def parseFlag(result):
    for l in result.split('\n'):
        if 'hgame' in l:
            return l

def main():
    output = getOutput()
    print(output)

    code = getCode()
    print(code)

    token = calcToken(output, code)
    print(token)

    result = postToken(token)
    # print(result)

    flag = parseFlag(result)
    print(flag)


if __name__ == "__main__":
    main()
