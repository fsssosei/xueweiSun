from pathlib import Path

print('This a')
print('You can use ')
print('You can use ')
print('You can use ')
print('You can use ')

while True:
    print('Please enter your command:')
    print('(read, write, rename, delete)')
    in_str = input()
    if in_str == 'read':
        print('Please enter the file name whit file extension:')
        filename = input()
        with open(filename) as f:
            for line in f:
                print(line, end = '')
    elif in_str == 'write':
        print('Please enter the file name whit file extension:')
        filename = input()
        with open(filename, 'a') as f:
            while True:
                in_line = input("Please input the contents of this file (input ':q' to quit):")
                if in_line == ':q':
                    print('Successfully rewrite')
                    break
                else:
                    print(in_line, file = f)
    elif in_str == 'rename':
        print('Please enter the file name whit file extension:')
        oldname = input()
        print('Please enter the new name whit file extension:')
        newname = input()
        Path(oldname).rename(Path(newname))
        print('The rename successfully.')
    elif in_str == 'delete':
        print('Please enter the file name whit file extension:')
        filename = input()
        Path(filename).unlink()
        print('The deletion is successfully.')
    else:
        print('Sorry, the command can only be read, write, delete and rename.')
    in_chr = input('Do you want to command again?: (y/n)')
    if in_chr == 'n':
        print('Bye Bye')
        break
