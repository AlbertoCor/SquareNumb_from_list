def run():
    numb = 1
    list = []
    squarelist = []

    while numb < 101:
        list.append(numb)
        squarenumb = (numb**2)
        numb = numb + 1
        squarelist.append(squarenumb)

    print(squarelist)
    print(list)

if __name__ == "__main__":
    run()
    