
import binascii, hashlib, base58, sys, ecdsa, codecs
fly1 = open('double256s.txt', 'w')
#Header order info


def convertstring(aa):
    # Step 1: get the privatekey in extended format, this is hexadecimal upper or lower case.
    string = aa
    # Step 2: adding 80 in the front for select de MAINNET channel bitcoin address
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


