import json
import ast

# Write dictionary to file
def add_user(returned_data):
    f = open("text.txt", "r+")
    j = f.read()
    f.close()

    new_dictionary = ast.literal_eval(j)
    index_next_item = len(new_dictionary)
    new_dictionary[index_next_item] = returned_data

    f = open("text.txt", "w+")
    f.write(str(new_dictionary))
    f.close()

def find(search,term):
    f = open("text.txt", "r+")
    j = f.read()
    f.close()
    new_dictionary = ast.literal_eval(j)
    indexdictionary=dict()
    for item in new_dictionary:
        if item[search]==term:
            indexdictionary[len(indexdictionary)]=item
    return indexdictionary
