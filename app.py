from services import auth, erp
from utils import helper
import pandas as pd


def createDFs():
    try:
        authDf = pd.read_csv("./data/auth.csv")
        authDf = authDf.loc[:, ~authDf.columns.str.contains('^Unnamed')]

        departmentDf = pd.read_csv("./data/employees.csv")
        departmentDf = departmentDf.loc[:, ~
                                        departmentDf.columns.str.contains('^Unnamed')]

    except pd.errors.EmptyDataError:
        authDf = pd.DataFrame(
            columns=["Name", "Password", "Designation"])
        authDf = authDf.loc[:, ~authDf.columns.str.contains('^Unnamed')]
        authDf.to_csv("./data/auth.csv")

        departmentDf = pd.DataFrame(
            columns=["Name", "Post", "Salary", "Department"])
        departmentDf = departmentDf.loc[:, ~
                                        departmentDf.columns.str.contains('^Unnamed')]
        departmentDf.to_csv("./data/employees.csv")
    return authDf, departmentDf


def main():

    authenticated = False
    loggedInUser = None

    authDf, departmentDf = createDFs()

    while True:
        print("---------------------------------")

        choice = int(input("1: Enroll\n2: Authenticate\n \n:> "))

        if choice == 1:
            while True:
                username = input("Enter username :> ")

                if not auth.checkIfUserExists(authDf, username):
                    password = input("Enter password :> ")
                    if len(password) > 6:
                        designation = input("Enter designation :> ")

                        authDf = auth.addUserToCSV(
                            authDf, username, password, designation)
                        authDf.to_csv("./data/auth.csv")

                        break
                    else:
                        print("[i] Enter strong password")
                        continue
                else:
                    print("[i] Username exists")
                    continue
        elif choice == 2:
            username = input("Enter username :> ")
            password = input("Enter password :> ")
            user = auth.getUser(authDf, username)
            if user["Password"].values[0] == password:
                print("")
                print("[i] Authenticated")
                authenticated = True
                loggedInUser = user
                print("")

            else:
                print("[i] Invalid credentials")

        if authenticated and loggedInUser is not None:

            while True:
                erpChoice = int(
                    input("1: Enroll\n2: Search\n3: Show All\n4: Delete\n5: Get count\n6: Search employees based on post\n7: Enter salary range('-' separated)\n8: Sign out\n:> "))
                print("")

                if erpChoice == 1:
                    if loggedInUser["Designation"].values[0] == "HR" or loggedInUser["Designation"].values[0] == "Manager":
                        name = input("Enter name :> ")
                        deptName = input("Enter department name :> ")

                        if not erp.checkIfEmployeeExistsInDepartment(departmentDf, name, deptName):
                            post = input("Enter post :> ")
                            salary = int(input("Enter salary :> "))
                            departmentDf = erp.saveEmployee(
                                departmentDf, name=name, post=post, salary=salary, department=deptName)
                            departmentDf.to_csv("./data/employees.csv")
                            print("")

                        else:
                            print("[!] User already exists in department")
                    else:
                        print("[i] You are not authorised.")
                elif erpChoice == 2:
                    name = input("Enter the user's name :> ")
                    user = erp.getUser(departmentDf, name)
                    print(user)
                    print("")
                elif erpChoice == 3:
                    print(departmentDf)
                    print("")
                elif erpChoice == 4:
                    name = input("Enter user's name to delete :> ")
                    departmentDf = erp.deleteUser(departmentDf, name)
                    departmentDf.to_csv("./data/employees.csv")

                    print("")
                    print("[i] Deleted")
                    print("")
                elif erpChoice == 5:
                    print(erp.getCount(departmentDf))
                elif erpChoice == 6:
                    post = input("Enter post :> ")
                    print("")
                    print(erp.getUsersByPost(departmentDf, post))
                    print("")
                elif erpChoice == 7:
                    salaryRange = input("Enter salary range(-) :> ")
                    salaryRange = salaryRange.split("-")
                    salaryRange = [int(sal) for sal in salaryRange]
                    print("")
                    print(erp.getUsersBySalaryRange(departmentDf, salaryRange))
                    print("")
                elif erpChoice == 8:
                    authenticated = False
                    loggedInUser = None
                    print("[i] Logged out")
                    break


helper.createFilesAndFolders()
main()
