# -*- coding: gbk -*-
import requests
import json
import notify


try:
  r1 = requests.get('https://ipv4.ipw.cn/api/ip/myip')
  r1text = "ipv4:" + r1.text + "\n"
except Exception as e:
  
  r1text = "ipv4:" + "blank" + "\n"

try:
  r2 = requests.get('https://ipv6.ipw.cn/api/ip/myip')
  r2text = "ipv6:" + r2.text + "\n"
except Exception as e:
  
  r2text = "ipv6:" + "blank" + "\n"

clientIP1 =  r1text + r2text 
#print(clientIP1)

try:
  r3 = requests.get('http://v4.ip.zxinc.org/info.php?type=json')
  r3tt = json.loads(r3.text)['data']['myip']
  r3text = "ipv4:" + r3tt + "\n"
except Exception as e:
  
  r3text = "ipv4:" + "blank" + "\n"



try:
  r4 = requests.get('http://v6.ip.zxinc.org/info.php?type=json')
  r4tt = json.loads(r4.text)['data']['myip']
  r4text = "ipv6:" + r4tt + "\n"
except Exception as e:
  
  r4text = "ipv4:" + "blank" + "\n"

clientIP2 =  r3text + r4text 
#print(clientIP2)

result = clientIP1 + clientIP2

print(result)
notify.send('myip', result)

