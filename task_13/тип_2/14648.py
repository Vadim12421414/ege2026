from ipaddress import *

ip_1 = ip_address('218.48.192.56')
ip_2 = ip_address('218.48.192.0')

for mask in range(10, 25):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net.hosts() and ip_2 == net.network_address:
        if net.num_addresses - 2 >=500:
            print(net.netmask)