import ssl
import urllib.parse
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

try:
    url_google=urllib.request.urlopen("https://google.com")
    print(url_google.read())
    # 2
    print('----------INFO---------')
    print(url_google.info())
    print(url_google.geturl())

    print('------END-----')
except urllib.error.URLError as e:
    print('Error', e.reason)

try:
    url_python=urllib.request.urlopen("https://www.python.org/search/?q=urlopen&submit=Search")
    print(url_python.read())
except urllib.error.URLError as e:
    print('Error', e.reason)

url='https://www.python.org/search'
values={'q':'basic','submit':'search'}
data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
try:
    resp=urllib.request.urlopen(req)
    respData=resp.read()
    print(respData)
except urllib.error.URLError as e:
    print('Error', e.reason)
