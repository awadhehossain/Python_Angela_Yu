public_information={"Awadhe":{"Age":21,"Hometown":"Magura","Favourite food":["Biriyani","Payesh","Pizza"]},
                    "Shawon":{"Age":22,"Hometown":"Dhaka","Favourite sports":["Football","Cricket","Table tanis"]},
                    "Arfan":["Nickname",{"Gmail":"awadhehossain762@gmail.com","Phone number":["01821947177","01601377569"],"Age":21}]}

# For Awadhe
print(public_information["Awadhe"])
print(public_information["Awadhe"]["Age"])
print(public_information["Awadhe"]["Hometown"])
print(public_information["Awadhe"]["Favourite food"])
print(public_information["Awadhe"]["Favourite food"][0])
print(public_information["Awadhe"]["Favourite food"][1])
print(public_information["Awadhe"]["Favourite food"][2])

# For Arfan
print(public_information["Arfan"])
print(public_information["Arfan"][0])
print(public_information["Arfan"][1])
print(public_information["Arfan"][1]["Gmail"])
print(public_information["Arfan"][1]["Phone number"][0])
print(public_information["Arfan"][1]["Phone number"][1])
print(public_information["Arfan"][1]["Age"])
