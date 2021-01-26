'''python program for the
      sum of elements in the list using recursion'''

def list_sum(li, size):

    if (size == 0):
        return 0
    else:
        return li[size - 1] + list_sum(li, size - 1)

lst = [1,4,6,7,8]

total = list_sum(lst, len(lst))

print("Sum of list numbers: ", total)
