# Health Management System
"""This health management system keeps a record for your daily diet and exercise
    Log is to add your activity
    It creates an text file with time stamp when you added yor activity
    Retrive is to see the activity"""

client_list = {1: "Tejas", 2: "Harry", 3: "Anand"}
log_list = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())

    print("Selected Client : ", client_list[client_name], "\n")

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    op = int(input())

    if op is 1:
        for key, value in log_list.items():
            print("Press", key, "to log", value, "\n", end="")
        log_name = int(input())
        print("Selected Job : ", log_list[log_name])
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k = 'y'
        while (k is not "n"):
            print("Enter", log_list[log_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()).replace(":", "-") + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op is 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        log_name = int(input())
        print(client_list[client_name], "-", log_list[log_name], "Report :", "\n", end="")
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")

except Exception as e:
    print("Wrong Input !!!")
