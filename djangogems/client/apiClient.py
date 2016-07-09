import sys
import requests
import json
from contextlib import redirect_stdout
from io import StringIO
import jwt

def getItemString(d, depth, buf, sortReverse = False):
        try:
            for k, v in sorted(d.items(), key = lambda x: x[0], reverse = sortReverse):
                if isinstance(v, dict):
                    with redirect_stdout(buf):
                        print((" " * depth) + ("%s" % k))
                    getItemString(v, depth + 4, buf, sortReverse)
                else:
                    with redirect_stdout(buf):
                        print((" " * depth) + "%s %s" % (k, v))

            return buf.getvalue()
        except:
            exceptionType, error = sys.exc_info()[:2]
            retstr = "Error in getItemString(): " + str(error)
            print(retstr)




def getToken():
    try:
        buf = StringIO()

        LOGIN_URL = 'http://127.0.0.1:7177/api-token-auth/'

        loginData = {'username' : 'dbrady', 'password' : '****' }

        r = requests.post(LOGIN_URL, data = loginData)

        if r.status_code == 200:
            d = json.loads(r.content.decode("utf-8"))
            print(getItemString(d, 0, buf, False))
            token = d["token"]
            return token

    except Exception:
        # Extract only the exception type and value from the tuple returned by sys.exc_info()
        exceptionType, error = sys.exc_info()[:2]
        print(repr(exceptionType) + " " + str(error))

def generateJwtToken():
    secret = "-dp$gj!kwe%7*4v)g2yula$czgitmo#*w65vp2j2$386e^rvx%"
    return jwt.encode({'some': 'payload'}, secret, algorithm='HS256')

def getProducts(token):
    try:
        buf = StringIO()

        PRODUCT_URL = "http://127.0.0.1:7177/api/products"

        headerData = {"Content-Type" : "application/json",
                      "Accept" : "application/json",
                      "Authorization" : "JWT %s" % token}

        print(headerData)

        r = requests.get(PRODUCT_URL, headers = headerData)

        if r.status_code == 200:
            d = json.loads(r.content.decode("utf-8"))
            print(d)
        else:
            print(r.content.decode("utf-8"))

    except Exception:
        # Extract only the exception type and value from the tuple returned by sys.exc_info()
        exceptionType, error = sys.exc_info()[:2]
        print(repr(exceptionType) + " " + str(error))



if __name__ == '__main__':
    token = getToken()
    products = getProducts(token)
    #createUser(token, user)

