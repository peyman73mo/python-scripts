#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    #arp_req.show()
    #print(arp_req.summary())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #broadcast.show()
    #print(broadcast.summary())
    arp_req_broadcast = broadcast/arp_req
    #arp_req_broadcast.show()
    #print(arp_req_broadcast.summary())
    answered, unanswered = scapy.srp(arp_req_broadcast,timeout=1,verbose=False)
    # print(answered.summary())
    
    client_list = []
    for ans in answered:
        client_dict = { "ip" : ans[1].psrc, "mac" : ans[1].hwsrc }
        client_list.append(client_dict)
    return client_list


def print_result(result_list):
    print("IP\t\t\tMAC Address\n----------------------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])



print_result(scan("10.0.2.1/24"))

