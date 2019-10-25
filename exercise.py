# String Indexing
s = 'django'

# 'd'
print(s[0])

# 'o'
print(s[-1])

# 'djan'
print(s[:4])

# 'jan'
print(s[1:4])

# 'go'
print(s[4:])

# Nested List

l = [3,7,[1,4,'hello']]

# Reassign 'hello' to 'goodbye'
l[2][2] = 'goodbye'
print(l);

# Using keys and indexing grab 'hello'

d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])

d3 = {'k1': [{'nest_key': ['this_is_deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

# Print only unique numbers
numbs = [1,2,3,3,1,1,1,1,1,1]
set1 = set(numbs)
print(set1)


# Functions

# Function 1
def check_pattern(arr):
    count = 0
    bool = False
    for i in arr:
        print(i)
        count = count + 1
        if i == 1:
            print('count', count);
            if (arr[count] == 2 and arr[count+1] == 3):
                bool = True
                return True
            else:
                continue    
        else:
            continue
    if bool == False:
        return False
                  
arr = [1,3,1,3]
print(check_pattern(arr))  

# Function 2
def string_bits(str):
    return str[0::2]
        
str = 'Heeololeo'
print(string_bits(str))   

# Function 3   
def end_other(a1 ='ab',b1 = 'thgjab'):
    if(a1[-3:-1] == b1[-3:-1]):
        return True
    else:
        return False
    
print(end_other())

# Function 4 - Count of even integers
def count_even(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
        else:
            continue
    return count


print('No of even numbers:', count_even([1,2,3,4,5,6]))
