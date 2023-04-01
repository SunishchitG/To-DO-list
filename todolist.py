import argparse

TODO_LIST_FILE = 'todo.txt'

def add_item(item):
    with open(TODO_LIST_FILE, 'a') as f:
        f.write(item + '\n')

def remove_item(item):
    
    with open(TODO_LIST_FILE, 'r') as f:
        lines = f.readlines()

    with open(TODO_LIST_FILE, 'w') as f:
        for line in lines:
            if line.strip() != item:
                f.write(line)

def list_items():
    with open(TODO_LIST_FILE, 'r') as f:
        lines = f.readlines()

    if len(lines) == 0:
        print('Your to-do list is empty.')
    else:
        for i, line in enumerate(lines):
            print(f'{i+1}. {line.strip()}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple command-line to-do list application.')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new item to the to-do list.')
    add_parser.add_argument('item', type=str, help='The item to add to the to-do list.')

    remove_parser = subparsers.add_parser('remove', help='Remove an item from the to-do list.')
    remove_parser.add_argument('item', type=str, help='The item to remove from the to-do list.')

    list_parser = subparsers.add_parser('list', help='List all items in the to-do list.')

    args = parser.parse_args()

    if args.command == 'add':
        add_item(args.item)
        print(f'Added "{args.item}" to the to-do list.')
    elif args.command == 'remove':
        remove_item(args.item)
        print(f'Removed "{args.item}" from the to-do list.')
    elif args.command == 'list':
        list_items()