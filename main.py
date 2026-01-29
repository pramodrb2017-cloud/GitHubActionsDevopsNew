def hello():
    print("hi")

def bye():
    print("bye")

methods = {
    "1": hello,
    "2": bye
}

choice = input("Enter 1 for hello, 2 for bye: ")
methods[choice]()
