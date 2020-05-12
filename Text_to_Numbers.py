#Regex Module
import re

#Reads the input processed from Stanford coreNLP lex Parser module
file = open("input1.txt.OUT", "r")
with open('output.txt', 'w') as redirect:
    for line in file:
        match_person = re.match("(.*)NNP Lemma=(.*)", line)
        if match_person:
            print (match_person.group(2)[:-23],file=redirect)
        match_entity = re.match("(.*)NNS Lemma=(.*)", line)
        if match_entity:
            print (match_entity.group(2)[:-18],file=redirect)
        match_dict = re.match("(.*)VBD Lemma=(.*)", line)
        if match_dict:
            print (match_dict.group(2)[:-18],file=redirect)
        match_number = re.match("(.*)NUMBER NormalizedNamedEntityTag=(.*)", line)
        if match_number:
            print (match_number.group(2)[:-1],file=redirect)
file.close()

#Convert the matched pattern into list of strings
with open('output.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
print (content)

#Subtract key-value pair dictionary
dict_subtract = {'gave': 'Subtract',
                 'lost': 'Subtract',
                 'decreased': 'Subtract',
                 'removed':'Subtract',
                 'subtracted':'Subtract',
                 'give':'Subtract',
                 'lose':'Subtract',
                 'decrease':'Subtract',
                 'remove':'Subtract',
                 'subtract':'Subtract',
                 'donate':'Subtract',
                 'sell':'Subtract',
                 'gift':'Subtract',
                 'give away':'Subtract',
                 'cutback':'Subtract'}

#Addition key-value pair dictionary
dict_add = {'had': 'Add',
            'increased': 'Add',
            'added': 'Add',
            'found':'Add',
            'have':'Add',
            'find':'Add',
            'increase':'Add',
            'add':'Add',
            'get':'Add',
            'gain':'Add',
            'acquire':'Add',
            'carry':'Add',
            'retain':'Add',
            'bear':'Add',
            'obtain':'Add',
            'own':'Add'}

#Arithmetic operations to solve the word-numeric problem
x = int(float(content[2]))
y = int(float(content[6]))
print (x)
print (y)
if content[5] in dict_add.keys():
    result =  x + y
    print (result)
if content[5] in dict_subtract.keys():
    result = x -y
    print (result) 

# Results  
if result > 0:
    print ("%s is now left with %d %s." % (content[0],result,content[3]+'s'))
else:
    print ("Invalid input.Please correct the query")
