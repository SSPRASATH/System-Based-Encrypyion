import random
import json

#part 1 Shamir
def gen():
    file = open("./keyvalue.txt","a")
    key_value = {}
    Secret = 1234
    N = raw_input("Enter the Total number of shares >")
    for x in range(1,int(N)+1):
        result = 0
        for y in range(1,int(N)+1):
            a = random.randint(1,9999)
            result = result + a*pow(x,y)
        result = result +Secret
        kvalue ={x : result}
        key_value.update(kvalue)
    file.write(json.dumps(key_value))
    file.close
    print key_value

#part 2
def decrypt():
    N = raw_input("Enter the Total Number of share >")
    a =[]
    for c in range(int(N)):
        j = raw_input("Enter input >")
        a.append(j)
    res = []
    for x in range(int(N)):
        p = 1
        for y in range(int(N)):
            if x != y:
                k = int(a[y])/float(int(a[x]) - int(a[y]))
                p = p * k
        res.append(p)
    print res
    value =[]
    for o in range(int(N)):
        l = raw_input("enter the value ")
        value.append(l)
    sums = 0
    for r in range(int(N)):
        sec = float(res[r])*float(value[r])
        sums = sums+sec
    print sums

if __name__ == "__main__":
    decrypt()