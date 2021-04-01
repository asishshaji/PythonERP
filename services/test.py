def myFun(arg1, *argv):
    print("First argument :", arg1)
    print(argv[0])


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
