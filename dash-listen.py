from scapy.all import *
import requests
url = 'http://www.arethedishesclean.com/toggle'
#Replace with the Key set in ACCESS_KEY on production.
payload = {'key': 'S3CR3T'}

def arp_display(pkt):
  if pkt[ARP].op == 1:
    if pkt[ARP].psrc == '0.0.0.0':
      #Replace with the MAC Address of your Dash Button 
      if pkt[ARP].hwsrc == '<dash_button_mac>':
        print "Dash Button Has Been Pressed"
        r = requests.post(url, data=payload)
        print r.status_code
        print r.text

print sniff(prn=arp_display, filter="arp")
