def parse_query_string(query: str) -> dict:
    if query[0] == "?":
        query = query.strip("?")
    # print(query)

    qParams = query.split("&")

    d = {}

    def addToDict(key, value):
        if key in d:
            currValue = d[key]
            if type(currValue) is list:
                d[key].append(value)
            else:
                d[key] = [value, currValue]
        else: 
            d[key] = value
        
    for qParam in qParams:
        if "=" in qParam:
            [key, value] = qParam.split("=")
            addToDict(key, value)
        else:
            addToDict(key, True)
    
    return d

def inverse_query_string(d: dict) -> str:

    qps = []

    for key in d.keys():
        if type(d[key]) is list:
            for value in d[key]:
                qps.append("".join([key, "=", str(value)]))
        else:
            qps.append(key + "=" + str(d[key]))

    return "&".join(qps)

# query = "?foo=hello&bar=world"
# print(parse_query_string(query))

# query = "?foo=hello&bar=world&keyboard"
# print(parse_query_string(query))

# query = "?foo=hello&bar=world&bar=mars&bar=jupiter"
# print(parse_query_string(query))

query = "?foo=hello&bar=world&bar=mars&bar=jupiter&bar"
print(parse_query_string(query))
print(inverse_query_string(parse_query_string(query)))
# expect: {'foo': 'hello', 'bar': ['world', 'mars', 'jupiter', True]}

