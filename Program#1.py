# Program 1 is about inputting 5 info about a person and put it in a file

# Make list
information = []

# Add inputs and indicate when to stop
while True:
    name = input("Input name: ")
    try:
        age = int(input("Please input age: "))
        salary = float(input("Please input salary: "))
    except ValueError:
        print("Try again")
        continue
    address = input("Input address: ")
    fav_food = input("Input favorite food: ")

    # Store inputs in a Library and put it in a variable
    info = {"Name": name, "Salary": salary, "Age": age, "Address": address, "Favorite Food": fav_food}

    # Append variable in a list
    information.append(info)

    # Write the list in a file (specifically the Information.txt file)
    with open("Information.txt", "a") as file_handle:
        file_handle.write(f"{info}\n")

    stop = input("Do you want to stop inputting data? (yes/no): ").strip().lower()
    if stop == "yes":
        break





