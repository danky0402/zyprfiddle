import json

#  Brief overview of key-value pairs types
#   1. string literals
#   2. json literal
#   3. python dictionary


# a string literal refers to creating/building a variable

my_name = "Dan"
status = "okay"
message = my_name + " is " + status
print(message)

# or it can be constructed using f-string for containing variables inside the string litera -  inside double or single quotes

message = f"{my_name} is {status}"
print(message)


#  constructing a JSON literal - a key-value pair  { "key" : "value" }, when value is a string.  Or { "key" : 10} when value is a number

json_string = '{ "Name" : "Dan" }'
print(json_string) 

json_string = f'{{ "Name" : "{my_name}" }}'             # user single quote on outside and double quotes around key-value pair
                                                        # use double braces with f-string to include single braces in string
print(json_string)

json_string_age = '{ "Age" : 30}'
print(json_string_age)

# python dictionary literal

py_dict = { "Name": "Dan"}                              #   key-value pair enclosed in braces that are not enclosed in quotes
print("My python dictionary is next")
print(py_dict)
print(str())    # print an empty line


# convert json string literal to python dictionary (i.e., python's version of key-value pair)

name_dict = json.loads(json_string)
print(type(name_dict))

# convert python dictionary to json string
back_to_json = json.dumps(name_dict)
print(back_to_json)
print(type(back_to_json))


variable1 = "value1"
variable2 = "value2"
s = f'{{"key1": "{variable1}", "key2": "{variable2}"}}'
d = eval(s)                                             # eval() to set string representation into python dictionary type
print(type(d))
print(d)
# Expected output: {"key1": "value1", "key2": "value2"}
