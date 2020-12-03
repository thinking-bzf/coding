list1 = ['第章1为我2额2e', '\n', '1    \n']
list = [
    x.replace(' ', '').replace('\n', '')[x.find('章') + 1:] for x in list1
    if x.replace(' ', '') != '\n'
]
list3 = [x[x.find('章') + 1:] for x in list1]
print(list)
