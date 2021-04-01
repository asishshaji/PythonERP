import erp
import auth

while True:
    # choice = int(input("1: Authentication\n2: ERP\n:>"))
    choice = 1
    if choice == 1:
        auth.main()
    elif choice == 2:
        erp.main()
    else:
        print("[i] Shutting down application")
        exit()
