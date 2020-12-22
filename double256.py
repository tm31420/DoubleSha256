
import binascii, hashlib, base58, sys, ecdsa, codecs
fly1 = open('double256s.txt', 'w')


def convertstring(aa):
    string = aa
    aa = (hashlib.sha256(hashlib.sha256(string).digest()).hexdigest())
    fly1.write("%s \n" % aa)    
    print aa
    
with open("addr.txt") as file:
    for line in file:

        ss = str.strip(line)
        print "__________________________________________________\n"
        print "Converting pvk: " + ss
        
        convertstring(ss)


print "__________________________________________________\n"


