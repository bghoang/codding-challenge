'''
Given a list of classes such as
 [['CSE 100', 'CSE 101'], ['CSE 12', 'CSE 30'], ['CSE 11', 'CSE 12'], ['CSE 101', 'CSE 105'], ['CSE 30', 'CSE 100']]
with the first one in each pair as the pre-req and the second one is the class.
Find the middle class of this list
Ex: with this list
[['CSE 100', 'CSE 101'], ['CSE 12', 'CSE 30'], ['CSE 11', 'CSE 12'], ['CSE 101', 'CSE 105'], ['CSE 30', 'CSE 100']]
we have this relationship CSE 11-> CSE 12-> CSE 30-> CSE 100-> CSE 101-> CSE 105
Output will be CSE 30
'''

def findMid(l):
    d = dict()
    # populate the dictionary
    for i in range(len(l)):
        d[l[i][0]] = l[i][1]
        startKey =''

    # Get the starting key 
    for key,value in d.items():
        if key not in list(d.values()):
            startKey = key
            break

    # Loop through the dict, stop at the middle class 
    i= 0
    while i in range(len(d)):
        if i == int(len(d)/2):
            break
        startKey = d[startKey]  
        i+=1
    return startKey

def main():
    l = [['CSE 100', 'CSE 101'], ['CSE 12', 'CSE 30'], ['CSE 11', 'CSE 12'], ['CSE 101', 'CSE 105'], ['CSE 30', 'CSE 100']]
    print(findMid(l))

if __name__ == "__main__":
    main()