import os


def createFilesAndFolders():
    if not os.path.exists(os.path.join(os.getcwd(), "data")):
        os.mkdir(os.path.join(os.getcwd(), "data"))

    with open(os.path.join(os.getcwd(), "data", "auth.csv"), 'w+') as fp:
        pass

    with open(os.path.join(os.getcwd(), "data", "employees.csv"), 'w+') as fp:
        pass

    print("[i] Required files and folders are created.")
