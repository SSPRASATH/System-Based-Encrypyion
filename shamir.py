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
    print "hello world"


if __name__ == "__main__":
    gen()