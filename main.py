import hashlib 

import math 

import os 

def is_prime(n): 

    if n <= 1: 

        return False 

    if n == 2: 

        return True 

    if n > 2 and n % 2 == 0: 

        return False 

    max_div = math.floor(math.sqrt(n)) 

    for i in range(3, 1 + max_div, 2): 

        if n % i == 0: 

            return False 

    return True 

j=int(input("num: ")) 

while(True): 

    j=j+1 

    if is_prime(j): 

        print(j) 

        result = hashlib.sha256(str(j).encode()) 

        os.system('curl -H \"Content-type:application/json" --data \'{"data":{"id":"<YOUR ID>","prime":"%s"}} \' http://<YOUR IP SERVER>:8080/mineBlock' % result.hexdigest().upper()) 
