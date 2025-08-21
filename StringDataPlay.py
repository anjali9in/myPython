
multiline_string = """This is a
multiline string
in Python."""

multiline_string2 = '''This is another
multiline string
with single quotes.'''

slash_test="C:myPython\\test\\gtt"
slash_test_n = "Checking \n new line"
slash_test_quote = "QOUTE\" printed double"

print("slash_test:", slash_test)
print("slash_test_n:", slash_test_n)
print("slash_test_quote:", slash_test_quote)

temp=70
result = f"Todays temp is {temp}"

print(result)

print(f"check extra }} {{")

#string operation

star = "*"
print(star * 3)

print(star * -1)

print(len("Python"))
print(ord("A"))
print("apple">"Apple")
print(11>2)

print("\u0061")
print(chr(97))

txtVal = "Python"
# print(txtVal[len(txtVal)]) #will give: IndexError: string index out of range

print(txtVal[len(txtVal)-1])
print(txtVal[-2]) #negative indexing


#slice => val[start:end:step]
print(txtVal[0:3])
print(txtVal[0:])
print(txtVal[:])

print(txtVal[-5:-2])
print(txtVal[-2:-5])

print(txtVal[::-2])
print(txtVal[::-1]) #reverse


print(txtVal.upper()) #newString will be returned
print(txtVal.lower()) #newString will be returned
print(txtVal.capitalize())#newString will be returned
print(txtVal.title())
print(txtVal)

data_with_space= "   Welcome Anjali!   "
print(data_with_space.strip())
print(data_with_space.lstrip())
print(data_with_space.rstrip())

