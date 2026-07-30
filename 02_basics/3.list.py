# list to string

chai_type = ["masala","ginger","lemon"]
print(" " .join(chai_type))

# ----------------------------------------

# Replace the value

tea_varities = ["a","b","c","d","e"]
print(tea_varities)

tea_varities[1:3] = ["f","g"]

# add the value

tea_varities.append("h") # add value in last

tea_varities.insert(1,"z") # add value in any position

tea_varities_copy = tea_varities.copy()

# remove the value

tea_varities.pop() # remove last value

tea_varities.remove("a")

# -------------------------------

# for loop and if loop

for tea in tea_varities:
    print(tea,end="-")



if "h" in tea_varities:
    print("I have h tea")


squared_num = [x**2 for x in range(10)]
print(squared_num)