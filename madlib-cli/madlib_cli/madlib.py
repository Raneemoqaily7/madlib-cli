
from cgitb import text
import re


# file_path = '../assets/dark_and_stormy_night_template.txt'
def read_template(file_path):
  try:
    with open(file_path , 'r') as file:
        text = file.read()
        file.close()
    return text
  except FileNotFoundError:
      raise(FileNotFoundError)
# print(read_template(file_path ))


# print(userinput())

def parse_template(text):
    stripped =re.sub('{(.*?)}', '{}', text )
    parts= tuple(re.findall(r'{(.*?)}', text))
    return  stripped , parts

def userinput(parts):
    user_input=[]
    for i in parts:
        user_input.append(input(i))
    return user_input

def merge(stripped ,user_input):
    stripped=str(stripped)
    text= stripped.format(*user_input)
    return text


if __name__=='__main__': 
  text= read_template('../assets/dark_and_stormy_night_template.txt')
  parts , stripped = parse_template(text)
  user_input= userinput(parts)
  output = merge (user_input,stripped)
  print(output)



#   ///helped by ayat 
# # i was thinking about format and the last step doesnt work

# from random import randint
# from typing import Type
# import copy
# import re


# def read_file(path):
#     try:
#       f = open(path)
      
      
#     except FileNotFoundError:
#         story ="error not exist"
#     else:
# # #         story=f.read()
# def open_file(path):
#   with open(path)as f:
#         story=f.read()            
#   return story




# def merge(story,parts):
#     language=[]
#     for part in parts:
#         item=
#   print (story)

#             f.write(f"this iss a copy of/n{story}")
#     return story

# story= (

# 'I the {} and {} {} have   {}. '+
#  'sister and plan to steal her {} {}. ' + 
#  'What are a  and backpacking  to do? Before you can help {} ' +
# 'youll have to collect the   and {} that open up the  ' +
# 'worlds connected to A {} Lair. There are  ' +
# 'along with hundreds of other goodies for you to find '
# )


# adjective=[i for i in input("give me two adjective").split(",")]
# Plural=[i for i in input ("give 4 plural").split(",")]
# firstname=[i for i in input("give me tweo f name").split(",")]
# plural_Noun=[i for i in input("give me plural noun").split(",")]
# Number=[i for i in input ("give me two numbers").split(",")]


# import random
# story= (

# 'I the {Adjective} and {Adjective} {Plural} have   {Number}. '+
#  'sister and plan to steal her {firstname} {Plural}. ' + 
#  'What are a  and backpacking  to do? Before you can help {Plural} ' +
# 'youll have to collect the   and {Plural} that open up the  ' +
# 'worlds connected to A {firstname} Lair. There are  ' +
# 'along with hundreds of other goodies for you to find '
# )

# Adjective=[i for i in input("give me two adjective").split(",")]
# Plural=[i for i in input ("give 4 plural").split(",")]
# firstname=[i for i in input("give me tweo f name").split(",")]
# plural_Noun=[i for i in input("give me plural noun").split(",")]
# Number=[i for i in input ("give me two numbers").split(",")]

# print(story.format
# (Adjective=random.choice(Adjective))
# (Plural=random.choice(Plural))
# (firstname=random.choice(firstname))
# (Number=random.choice(Number)))





# word_dict= {
#     'Adjective':[i for i in input("give me two adjective").split(",")],
#     'Plural':[i for i in input ("give 4 plural").split(",")],
#     'firstname':[i for i in input("give me tweo f name").split(",")],
#     'plural_Noun':[i for i in input("give me plural noun").split(",")],
#     'Number':[i for i in input ("give me two numbers").split(",")]
# }

# def creat_story():

#     return story.format(
#          (Adjective,randint(0,len(Adjective))),
#          (Plural,randint(0,len(Plural))),
#          (firstname,randint(0,len(firstname))),
#          (plural_Noun,randint(0,len(plural_Noun))),
#          (Number,randint(0,len(Number))),
#          (Plural,randint(0,len(Plural))),
#          (Plural,randint(0,len(Plural))),
#          (firstname,randint(0,len(firstname))),
#          (Adjective,randint(0,len(Adjective))))
# for i in word_dict:
#     Adjective=i
#     print(i) 


# print (word_dict)

# ={}
# n=int(input("please type number 9 to start"))
# for i in range(n):
#     v=input("enter a word ")
#     a.update({i:v})a

# def get_word(type,local_dict):
#     words =local_dict[type]
#     cnt=len(words)-1
#     index=randint(0,cnt)
#     return local_dict[type].pop(index)
   

    

# def creat_story():
#     local_dict=copy.deepcopy(word_dict)
#     return story.format(
#          get_word('Adjective',local_dict),
#          get_word('Plural',local_dict),
#          get_word('firstname',local_dict),
#          get_word('plural_Noun',local_dict),
#          get_word('Number',local_dict),
#          get_word('Plural',local_dict),
#          get_word('Plural',local_dict),
#          get_word('firstname',local_dict),
#          get_word('Adjective',local_dict)


    
# def get_word(type,local_dict):
#     words =local_dict[type]
#     cnt=len(words)-1
#     index=randint(0,cnt)
#     return local_dict[type].pop(index)

# # print (story)
# print ("Make Me A Video Game!")
# print(creat_story())


# # ///////////////////////////////////////////////////
# import random
# story= (

# 'I the {Adjective} and {Adjective} {Plural} have   {Number}. '+
#  'sister and plan to steal her {firstname} {Plural}. ' + 
#  'What are a  and backpacking  to do? Before you can help {Plural} ' +
# 'youll have to collect the   and {Plural} that open up the  ' +
# 'worlds connected to A {firstname} Lair. There are  ' +
# 'along with hundreds of other goodies for you to find '
# )

# Adjective=[i for i in input("give me two adjective").split(",")]
# Plural=[i for i in input ("give 4 plural").split(",")]
# firstname=[i for i in input("give me tweo f name").split(",")]
# # plural_Noun=[i for i in input("give me plural noun").split(",")]
# Number=[i for i in input ("give me two numbers").split(",")]

# Adjective=random.choice(Adjective)
# Plural=random.choice(Plural)
# firstname=random.choice(firstname)
# Number=random.choice(Number)





