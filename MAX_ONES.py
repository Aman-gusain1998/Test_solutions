'''Python program to print max number of
   consucitive binary either 0 or 1 from a
   list'''

def max_ones(l1):

    total = 0
    count = 0

    for i in range(0,len(l1)):

        if(l1[i] == 0):
            count = 0

        else:
            count = count + 1
            total = max(total, count)

    return total

l1 = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]

print(max_ones(l1))