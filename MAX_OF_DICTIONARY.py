'''printing the maximum key value pair
          from the dictionary using list comprehension'''

dic1 = {'a': 1000,

        'b': 3000,

        'c': 100}

inverse = [{key, value} for key, value in dic1.items()]

print(max(inverse))
