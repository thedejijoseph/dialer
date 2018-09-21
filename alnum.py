# so ive been thnn thinking about this keypad thingy on phones and how you can find contacts with names or phone numbers...

import sys

keys = {
    0: ['0', '+'],
    1: ['1', 'voice mail'],
    2: ['2', 'A', 'B', 'C'],
    3: ['3', 'D', 'E', 'F'],
    4: ['4', 'G', 'H', 'I'],
    5: ['5', 'J', 'K', 'L'],
    6: ['6', 'M', 'N', 'O'],
    7: ['7', 'P', 'Q', 'R', 'S'],
    8: ['8', 'T', 'U', 'V'],
    9: ['9', 'W', 'X', 'Y', 'Z']
}

def search(query):
    

script_actions = ['search']

if __name__ == "__main__":
    args = sys.argv
    command  = args[1]

    if command not in script_actions:
        print(f"Command '{command}' is not available.")
    
    if command == "search":
        query = args[2:]
        search(query)