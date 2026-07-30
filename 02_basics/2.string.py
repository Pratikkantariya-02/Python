# string to list

chai="1,2,3,4,5"
print(chai.split(", "))

# -----------------------------------------------------

# representation
repr('chai')
# use for string representation and debugging

# string
str('chai')
# use for user friendly string representation

# print
print('chai')
# use for output

# -------------------------------------------------------

chai = 'Masala chai'
print(chai) or print(chai[0:6:2])
slice_chai=chai[0:6:2]
print(slice_chai)

print(chai.upper())
print(chai.strip())
print(chai.replace("Masala","Hello"))
print(chai.find("chai"))
print("Malasa" in chai)
print(chai.count("chai"))
print(len(chai))

# how to print one string to another string

chai_type = "masala"
quentity = 2
order = "I order {} cups of {} chai"
print(order.format(quentity,chai_type))

for letter in chai:
    print(letter, end="-")

chai="He said, \"Masala chai is good\""
print(chai)

# remove unicode error

chai=r"c:\user\pwd"
print(chai)
# or
chai = "c:\\user\\pwd"
print(chai)