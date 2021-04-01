import pandas as pd


def saveEmployee(df, **kwargs):
    df.loc[len(df.index)] = [kwargs['name'], kwargs['post'],
                             kwargs['salary'], kwargs['department']]
    return df


def checkIfEmployeeExistsInDepartment(df, name, deptName):
    user = df.loc[(df['Name'] == name) & (df['Department'] == deptName)]

    return True if len(user) != 0 else False


def getUser(df, name):
    user = df.loc[df['Name'] == name]
    return user


def deleteUser(df, name):
    df.drop(df.loc[df['Name'] == name].index, inplace=True)
    print(df)
    return df


def getCount(df):
    data = df.groupby("Department").count()
    print("")
    for k, v in data['Name'].items():
        print("[i] Department :>", k, "contains", v, "employees.")
    print("")


def getUsersByPost(df, post):
    users = df.loc[df['Post'] == post]
    return users


def getUsersBySalaryRange(df, salaryRange):
    users = df.loc[(df['Salary'] >= salaryRange[0])
                   & (df['Salary'] <= salaryRange[1])]
    return users
