person_dict = {"fname": "Neuron",
               "lname": "Planets",
               "address": "Malang"
               }

# Get All Dict
print(person_dict)

# Get The First Name
print("GET NAME : ", person_dict["fname"])

# Reassign Value
person_dict["address"] = "Kediri"
print("CHANGED ADDR : ", person_dict)

# Assingning New Key Value Pairs
person_dict["phone"] = 23013801313

# Test is there some spesific key
print("IS THERE A PHONE : ", "phone" in person_dict)

# Get Only The Values
print("VALUES ONLY")
print(person_dict.values())

# Get Only The Keys
print("KEYS ONLY")
print(person_dict.keys())


for k in person_dict.keys():
    print(k)

for v in person_dict.values():
    print(v)

for k, v in person_dict.items():
    print(k, v)


# Get The Keys Using Get To avoid "KEYERROR"
# print(person_dict["mname"]) => This will return KeyError
print(person_dict.get("mname", "Keys Not Found"))


# DELETING
del person_dict["phone"]
print("PHONE DELETED : ", person_dict)

# CLEAR THE DATA
person_dict.clear()
print("LIST CLEARED : ", person_dict)

# USING THE USER INPUT
data_user = []
fname, lname = input("Enter Your Name : ").split()

data_user.append({"fname":fname, "lname":lname})
print(data_user)
