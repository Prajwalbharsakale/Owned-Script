#if we have array = [4,2,0,1,8,0]
#output should be = [4,2,1,8,0,0] 
# Explnation = place zero values at end by keeping the order of values, order of the values should'nt change but the zero shold be at end

# we will follow two pointors approch here.
#--------------------------------------------
# Nested Loops, brute force method -->
#--------------------------------------------
# a = [4,2,0,1,8,0]
# for i in range(len(a)):
#     if a[i] == 0:
#         for j in range (i+1, len(a)):
#             if a[j] != 0:
#                 a[i], a[j] = a[j], a[i]

# print(a)


# #--------------------------------------------
# # two pointer method
# a = [4,2,0,1,8,0]
# i = 0
# j = 1

# while j < (len(a)):
#     if a[i] != 0:
#         i += 1
#         if i >= j:
#             j = i + 1

#     elif a[j] == 0:
#         j += 1

#     else:
#         a[i],a[j] = a[j], a[i]
#         i += 1
#         j += 1
        

# print(a)




#--------------------------------------------
# slow and fast pointer 
#--------------------------------------------
# a = [4,2,0,1,8,0]
# i = 0
# for j in range(len(a)):
#     if a[j] != 0:
#         a[i], a[j] = a[j], a[i]
#         i += 1

# print(a)

# iteration 1 -
# a[i] = a[0] = 4
# a[j] = a[0] = 4
# a[j] != a[0] ~~ 4 != 0
# a[0], a[0] = a[0], a[0]
# no change 
# i ++1 = i = 1

# iteration 2 -
# a[i] = a[1] = 2
# a[j] = a[1] = 2
# a[j] != a[1]  ~~ 2 != 0
# a[1], a[1] = a[1], a[1]
# no change
# i ++1 = i = 2

# iteration 3 -
# a[i] = a[2] = 0
# a[j] = a[2] = 0
# a[j] != a[2]  ~~ 0 != 0
# nothing
# i = 2

# iteration 4 -
# a[i] = a[2] = 0
# a[j] = a[3] = 1
# a[j] != a[3]  ~~ 1 != 0
# change
# a[2], a[3] = a[3], a[2]
# 0,1 = 1,0
# i += 1 = 3
# a = [4,2,1,0,8,0]

# iteration 4 -
# a[i] = a[3] = 0
# a[j] = a[4] = 8
# a[j] != a[3]  ~~ 8 != 0
# change
# a[3], a[4] = a[4], a[3]
# 0,8 = 8,0
# i += 1 = 4
# a = [4,2,1,8,0,0]

# iteration 5 -
# a[i] = a[4] = 0
# a[j] = a[5] = 0
# a[j] != a[5]  ~~ 0 != 0
# nothing 
# i = 4
# a = [4,2,1,8,0,0]

# iteration 6 -
# a[i] = a[4] = 0
# a[j] = a[6] = out of range
# stop the loop
# --> a = [4,2,1,8,0,0]
#--------------------------------------------



############################################
# extra arry method
#############################################
a = [4,2,0,1,8,0]
b = []

for i in a:
    if i != 0:
        b.append(i)

while len(b) < len(a):
    b.append(0)

print(b)
