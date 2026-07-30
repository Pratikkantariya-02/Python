l1=[1,2,3]
l2=l1
print (l1)
print (l2)

# l1 == l2
# ans is true
# l1 is l2
# ans is true 

# l2=[1,2,3] when we give value separately
# l1 == l2
# ans is true
# it check the values are equal or not
# l1 is l2 
# ans is false
# because we give diff reference so is check the reference of the list

l1=[4,5,6]
print (l1)
print (l2)



# --------------------------

k1=[1,2,3]
k2=k1[:] # we can give values as a copy

# --------------------------

p1=[1,2,3]
p2=p1
print (p1)
print (p2)

p1[0]=4
print (p1)
print (p2)
