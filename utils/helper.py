import os
import pandas as pd


def createFilesAndFolders():
    if not os.path.exists(os.path.join(os.getcwd(), "data")):
        os.mkdir(os.path.join(os.getcwd(), "data"))

    if not os.path.exists(os.path.join(os.getcwd(), "data", "auth.csv")):
        with open(os.path.join(os.getcwd(), "data", "auth.csv"), 'w+') as fp:
            pass

    if not os.path.exists(os.path.join(os.getcwd(), "data", "employees.csv")):
        with open(os.path.join(os.getcwd(), "data", "employees.csv"), 'w+') as fp:
            pass

    print("[i] Required files and folders are created.")


def createDFs():
    try:
        authDf = pd.read_csv("./data/auth.csv")
        authDf = authDf.loc[:, ~authDf.columns.str.contains('^Unnamed')]

        employeeDf = pd.read_csv("./data/employees.csv")
        employeeDf = employeeDf.loc[:, ~
                                    employeeDf.columns.str.contains('^Unnamed')]

    except pd.errors.EmptyDataError:
        authDf = pd.DataFrame(
            columns=["Name", "Password", "Designation"])
        authDf = authDf.loc[:, ~authDf.columns.str.contains('^Unnamed')]
        authDf.to_csv("./data/auth.csv")

        employeeDf = pd.DataFrame(
            columns=["Name", "Post", "Salary", "Department"])
        employeeDf = employeeDf.loc[:, ~
                                    employeeDf.columns.str.contains('^Unnamed')]
        employeeDf.to_csv("./data/employees.csv")
    return authDf, employeeDf
