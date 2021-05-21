import math         #library help to apply sqrt to iterable number

def run():

    my_dict = {i: math.sqrt(i) for i in range(1,1001)} #dict comprehension that reduce code space

    print(my_dict)      #show dictionary keys, values 

if __name__ == "__main__":
    run()