checklist = list()
#checklist.append('Blue')
#print(checklist)
#checklist.append('Orange')
#print(checklist)
# CREATE
def create(item):
    checklist.append(item)
    # READ
def read(index):
    return checklist[int(index)]
# UPDATE
def update(index, item):
    checklist[int(index)] = item
# DESTROY
def destroy(index):
    checklist.pop(int(index))

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index):
    print("[ Items completed √ ]")
    checklist[int(index)] = '√' + checklist[int(index)]
    print(checklist[int(index)])


def select(function_code):
    # Create item
    if function_code == "C" or function_code == "c":
        input_item = user_input("Input item: ")
        create(input_item)
        return True

    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number?: ")
                    # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))
        return True

    elif function_code == "U" or function_code == "u":
        update_ix = user_input("index to upate: ")
        update_item = user_input("item you want to add: ")
        update(update_ix, update_item)
        return True

    # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()
        return True

    elif function_code == "D" or function_code == "d":
        remove = user_input("Which index would you like to delete?: ")
        destroy(remove)
        return True




    elif function_code == "M" or function_code == "m":
        mark_input = input("which item would you like to check: ")
        mark_completed(mark_input)
        return True

    elif function_code == "Q" or function_code == "q":
        return False
    # Catch all
    else:
        print("Unknown Option")
        return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
    #print(read(1))
    # Your testing code here
    # ...
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
#test()
#list_all_items()
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, U to update, M for checkmark, d to delete, and Q to quit: ")
    running = select(selection)
