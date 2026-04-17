from ipaddress import *
cnt=0
net=ip_network('172.16.168.0/255.255.248.0', False)
for ip in net:
    ip=f'{int(ip):032b}'
    if ip.count('1')%5!=0:
        cnt+=1
print(cnt)
