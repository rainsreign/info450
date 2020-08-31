import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = []
    for x in range (1,4):
        return_value.append((x*3)**2) 
    #using list comprehension
    #return_value = [(x*3)**2 for x in range(1,4)]
    return return_value

if __name__ == "__main__":
    for x in squared_threes():
        print(x)

    #should print out all numbers between 0 and 99 (inclusive)
    #that are evenly divisible by 3, then squared
    #e.g
    #9
    #36
    #81
    #... etc.