import string, random
from hashlib import sha256

d = string.ascii_letters+string.digits

for i in d:
    for j in d:
        for k in d:
            for l in d:
                x = i+j+k+l+"PU5a9N6lFog9VXb7"
                h = sha256(x.encode()).hexdigest()
                if h == "4ce80bdb3424a743713400a442cdbcf9b18de1c9a6655c1f5336ff04453f47d3":
                    print(x)
                    exit(0)
