# add default values to a python dictionary values, whenever there is no data in them

def add_default_value(dic):
    for key in dic.keys():
        if dic[key] in [None, '', 'blank']:
            dic[key] = 'default'

d1 = {"k1":None,"k2":"new","k3":3, "k4":"blank"}
add_default_value(d1)

# output: {'k1': 'default', 'k2': 'new', 'k3': 3, 'k4': 'default'}