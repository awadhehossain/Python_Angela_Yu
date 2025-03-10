print("Nop problem")
# print("Indentation error!!!")# it gives indentation error,you can check it removing # sign
# Because before starting any line or statement no space or tab is allowed

a=int(input("Give an integer:"))

if a>20: # This is a parent line of code
    print("Greater than 20") # this is a child line of code,so it doesn,t gives us any error
    
else: 
    print("Less than or equal 20")

if a>20:
     print("Greater than 20")
     # (else) we can't start else styatement ferom their,it gives us indentation error
