import pandas as pd


def addUserToCSV(df, username, password, designation):
    df.loc[len(df.index)] = [username, password, designation]
    return df


def getUser(df, username):
    user = df.loc[df['Name'] == username]
    return user


def checkIfUserExists(df, username):
    user = df.loc[df['Name'] == username]

    return True if len(user) != 0 else False
