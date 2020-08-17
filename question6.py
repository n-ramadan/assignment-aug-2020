# Split a json tree having multiple table structures using python


tree=[{ "text": "Parent 1", "id" : "1", "nodes": [ { "text": "Child 1", "id" : "2", "parentid" : "1", "nodes": [ { "text": "Grandchild 1", "id" : "4", "parentid" : "2", }, { "text": "Grandchild 2", "id" : "8", "parentid" : "2", } ] }, { "text": "Child 2", "id" : "10", "parentid" : "1", } ] }, { "text": "Parent 2", "id" : "19" } ]

res = []
def split_tree(tree):
    for node in tree:
        dic = {}
        for key in node.keys():
            if not isinstance(node[key], list):
                dic[key] = node[key]
            else:
                split_tree(node[key])
        res.append(dic)

split_tree(tree)
res
                    
# output
# [{'text': 'Grandchild 1', 'id': '4', 'parentid': '2'},
#  {'text': 'Grandchild 2', 'id': '8', 'parentid': '2'},
#  {'text': 'Child 1', 'id': '2', 'parentid': '1'},
#  {'text': 'Child 2', 'id': '10', 'parentid': '1'},
#  {'text': 'Parent 1', 'id': '1'},
#  {'text': 'Parent 2', 'id': '19'}]

# However, this is not foolproof. Above solution assumes the only field that in form of list are the child nodes