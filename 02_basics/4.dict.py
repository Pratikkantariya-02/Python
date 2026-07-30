# how to print dict

chai_type={"masala":"spicy", "ginger":"zesty", "green":"mild"}

print(chai_type)
print(chai_type["masala"])
print(chai_type.get("ginger"))

chai_shop={
    "chai":{"malasa":"spicy","ginger":"zesty"},
    "tea":{"green":"mild","black":"strong"}
    }

print(chai_shop)
print(chai_shop["chai"]["ginger"])

# how add key and values

chai_type["ealy grey"]="citrus"

# how to chage value

chai_type["green"]="cool"

# how to remove key and values

chai_type.popitem()
chai_type.pop("ginger")
del chai_type["green"]

# loop

for chai in chai_type:
    print(chai)
    print(chai,chai_type[chai])

for key, value in chai_type.items():
    print(key,value)

if "masala" in chai_type:
    print("I have masala chai")


squared_num = {x:x**2 for x in range(10)}
print(squared_num)

# how to creat new dict using list and string

keys=["masala","ginger","lemon"]
default_value="good"
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)