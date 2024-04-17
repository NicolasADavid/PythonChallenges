from typing import Dict
from collections import defaultdict

if __name__ == "__main__":
    # d = dict()

    # d['a'] = 1

    # # d.popitem() // Removes last inserted (key/val)

    # print(d.setdefault('a', 8))
    # print(d.values())

    d2 = dict().fromkeys([1, 2, 3, 4, 5, 6, 7], 1000)
    # print(d2['a'])
    # print(d2[1])
    print(d2.items())
    print(d2.values())
    print(d2.keys())

    def def_value():
        return 0

    dd = defaultdict(def_value)

    di = defaultdict(int)

    # Defining the dict and passing  
    # lambda as default_factory argument 
    d = defaultdict(lambda: "Not Present") 
    d["a"] = 1
    d["b"] = 2
    
    print(d["a"]) 
    print(d["b"]) 
    print(d["c"])


    # Defining a dict 
    d = defaultdict(list) 
    
    for i in range(5): 
        d[i].append(i) 
        
    print("Dictionary with values as list:") 
    print(d) 







