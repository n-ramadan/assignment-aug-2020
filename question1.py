# Split a file which has n number of schema def. And store them in a dict of lists(no 3rd party imports)
# File to read: to_read.txt


#Set first field value as dictionary key
dic1 = {}
with open("to_read.txt", "r") as file:
    for line in file:
        line_split = line.split(',')
        line_split = [x.strip(" ").strip("\n") for x in line_split]
        dic1[line_split[0]] = line_split[1:]

#Set ordered integer as dictionary key
dic2 = {}
key = 0
with open("to_read.txt", "r") as file:
    for line in file:
        line_split = line.split(',')
        line_split = [x.strip(" ").strip("\n") for x in line_split]
        dic2[key] = line_split
        key = key + 1