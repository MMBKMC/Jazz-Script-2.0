#Main.py
import sys
from sys import*

def token(sys):
    for tokens in token(sys):
        'print',
        'set',
        'let',
        'import',
        'class',
        'println'
        
    token = "[print]"
    token = "[set]"
    token = "[let]"
    token = "[import]"
    token = "[class]"
    token = "[println]"
    
def string(sys):
    for strings in string:
        'Hello World!',
        'Good Bye World!'
        
    string = "[Hello World!]"
    string = "[Good Bye World!]"
    
    format('import')
    append = "A module has imported!"
    print(append)
    string1 = "sys"
    string2 = "Jazz"
    append(string1)
    append(string2)
    
    def operators(sys):
        '+',
        '-',
        '(',
        ')',
        '"',
        "'",
        '#',
        '/'
        

        
# print "Hello World" --> [Hello World!]
# import(os) --> A module has imported!
# let x = 10 --> Let variable x be 10
# set x 11 --> Set variable x to 11

operator1 = "PLUS"
operator2 = "MINUS"
operator3 = "LPAREN"
operator4 = "RPAREN"
operator5 = "HASHTAG"

comment_sign = "#"
comment1_sign = "/"

# #test.jazz = ignore it in the runner
# // test.jazz = ignore it in the runner
#*Example
# a = 10
# let a = 11
# set a 12
# 
# *# runs = Let a variable be 11 Set a variable 12

format('print')
append = ("")

format('Hello World')
append = ("[Hello World]")

format('Good Bye World')
append = ("[Good Bye World]")

format('class')
append = ("[class],[{varname}]")

top_number = '21'

# 21

format('println')
append = ("[println],[{varname}")

token_output1 = "[print],"
strings_output1 = "[Hello World]"
strings_output2 = "[Good Bye World]"
token_output2 = "[Let {varname} variable be {varname}]"
token_output3 = "[Set {varname} to {varname}]"
token_output4 = "[A class created called {varname}!]"