def items():
    items_list = ["wooden staff", "wizard hat", "cloth shoes", "potion of invisibility"]
    for x in items_list:
       print(x)

def main():
    select_command = input("Please select a command: ")
    if select_command == "show":
        print(items())
    elif select_command == "grab":
        print(items())
        grab = input("What do you want to grab: ")
        if grab == items():
            print(f"Name:{grab}")

        

print("\nThe Wizards Inventory program\n" )
print("COMMAND MENU")
print("show - Show all items \ngrab - Grab an item \nedit - Edit an item \ndrop - Drop an item \nexit - Exit program\n",)
main()


# # user entry (command) must be in the list of acceptable commands
# def validate_menu_option(prompt, commands):
#     command = ""
#     valid_entry = False
#     while not valid_entry:
#         command = input(prompt)
#         if command in commands:
#             valid_entry = True
#         else:
#             print("Invalid command. Please try again.")
#     return command

# chuck = ["Candy","Obi","Ada"]

# def items():
#     for me in chuck:
#         print(me)

# # for me in range(1,len()):
# #     print(f"{me}. {chuck}\n")
# # for you in range(len(chuck)):
# #     print(f"{you + 1}. {chuck}")
