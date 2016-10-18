import pprint

# Dictionary
dic = {'1':2,'2':3}
page_id = 3
dic[str(page_id)] = 4
print(dic)

# (1, 'http://stackoverflow.com', 'stack')
list1 = (1, 'http://stackoverflow.com', 'stack')
list1 = list1 + (2,)
pprint.pprint(list1)
