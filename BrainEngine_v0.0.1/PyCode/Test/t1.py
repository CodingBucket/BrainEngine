import json

num = {1: 2,2: 3}

h = '{"foo":"bar", "foo2":"bar2"}'
d = json.loads(h)
#print(d)
num = 2

c = {1: 2, 2: 3}
print(c)
print(type(c))
jsonarray = json.dumps(c, ensure_ascii=False)
print(jsonarray)
print(type(jsonarray))
d = json.loads(jsonarray)
print(d)
print(d[str(num)])
print(type(d))