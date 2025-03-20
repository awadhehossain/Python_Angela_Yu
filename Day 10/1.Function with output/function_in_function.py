def function_1(text):
    return text + " " + text

def function_2(text):
    return text.title()

output=function_2(function_1("hello"))
print(output)

#same thing
Output_2=function_1(function_2("hEllo"))
print(Output_2)