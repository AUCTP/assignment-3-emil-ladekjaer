# In this make task, you will write regular expressions to check if a given string 
# represents an IPv4 address, an IPv6 address or none of these.

# IPv4 was the first publicly used Internet Protocol which used 4 byte addresses 
# which permitted for 232 addresses. The typical format of an IPv4 address is A.B.C.D 
# where A, B, C and D are Integers lying between 0 and 255 (both inclusive).
# IPv6, with 128 bits was developed to permit the expansion of the address space. 
# To quote from the linked article: The 128 bits of an IPv6 address are represented 
# in 8 groups of 16 bits each. Each group is written as 4 hexadecimal digits and the 
# groups are separated by colons (:). 
# The address 2001:0db8:0000:0000:0000:ff00:0042:8329 is an example of this 
# representation.
# Use the list ipAddresses to test your regex. How many IPv4 and IPv6 Addresses are in the list?
import re
ipadresses=[]
list=open("ipAdresses.txt", "r")
for line in list:
    ip=line.strip()
    ipadresses.append(ip)

regipv6=re.compile('^([0-9a-fA-F]{4}:){7}[0-9a-fA-F]{4}$')
regipv4=re.compile('^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$')

ipv6_count = 0
ipv4_count = 0
invalid_count = 0
for ip in ipadresses:
    if regipv6.match(ip):
        ipv6_count += 1
    elif regipv4.match(ip):
        ipv4_count += 1
    else:
        invalid_count += 1

print(f"IPv6 Addresses: {ipv6_count}")
print(f"IPv4 Addresses: {ipv4_count}")
print(f"Invalid Addresses: {invalid_count}")