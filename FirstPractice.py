print("Hello, World!")
x=2
floatVal=5.6
name="Anjali"
isStudying=True
age=27
address=["123 Main St", "Cityville", "Countryland"]
dataObject = {
    "name": name,
    "isStudying": isStudying,
    "age": age,
    "address": address
}

print("x:", x, "floatVal:", floatVal, "name:", name, "isStudying:", isStudying, "age:", age, "address:", address, "dataObject:", dataObject)
print("\n type of x:", type(x),
    "\n type of floatVal:", type(floatVal),
    "\n type of name:", type(name),
    "\n type of isStudying:", type(isStudying), 
    "\n type of age:", type(age), 
    "\n type of address:", type(address),
    "\n type of dataObject:", type(dataObject)
)
#  type of x: <class 'int'> 
#  type of name: <class 'str'> 
#  type of isStudying: <class 'bool'> 
#  type of age: <class 'int'> 
#  type of address: <class 'list'> 
#  type of dataObject: <class 'dict'>


# reserved keywords -> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# function in python->
def is_reserved_keyword(word):
    reserved_keywords = [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
        'while', 'with', 'yield'
    ]
    return word in reserved_keywords

print(is_reserved_keyword("class"))

print('\U0001F913')