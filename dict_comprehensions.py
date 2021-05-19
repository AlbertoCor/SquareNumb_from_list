def run():
    my_dict = {}

    for i in range(1, 100):
        if i % 3 !=0:
            my_dict[i] = i**3

    print(my_dict)

if __name__ == "__main__":
    run()