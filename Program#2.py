# Program 2 ties to get the info on the text file and searches for a match

# Search for user in the file
ask_user = input("Search for user: ").strip()

# Read the lines in the file
with open('Writing.txt', 'r') as file_handle:
    lines = file_handle.readlines()

    # Search in the file for a file with the same name use also an if function
    for line in lines:

        # This allows each line to turn back into a library than just a string
        info = eval(line)

        if info['Name'] == ask_user:
            print("Person found!\n")
            print("Name: ", info["Name"])
            print("Age: ", info["Age"])
            print("Salary: ", info["Salary"])
            print("Address: ", info["Address"])
            print("Favorite food: ", info["Favorite Food"])


    else:
        print("User not found")