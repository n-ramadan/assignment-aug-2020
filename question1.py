# Split a file which has n number of schema def. And store them in a dict of lists(no 3rd party imports)
# File to read: to_read.txt / question1_text.txt


#Set first field value as dictionary key
dic1 = {}
with open("question1_text.txt", "r") as file:
    for line in file:
        line_split = line.split(',')
        line_split = [x.strip(" ").strip("\n") for x in line_split] #clean trailing whitespaces
        key = line_split[0]
        try:
            dic1[key].append(line_split[1:])
        except:
            dic1[key] = []
            dic1[key].append((line_split[1:]))
