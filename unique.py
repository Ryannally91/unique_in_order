

def unique_values(iterable):
    list= []
    for char in iterable:
        if char not in list:
            list.append(char)
    return list


# Implement the function unique_in_order which takes as 
# argument a sequence and returns a list of items without
#  any elements with the same value next to each other and
#   preserving the original order of elements

def unique_in_order(iterable):
    list= []
    for i in range(0,len(iterable)):
        print(i)
        if i == (len(iterable)-1):
            list.append(iterable[i])
            break
        if iterable[i] != iterable[i+1]:
            print(i)
            list.append(iterable[i])
            print(len(iterable)-1)
           
    print(list)    
    return list

#test
unique_in_order('ggoohijl')