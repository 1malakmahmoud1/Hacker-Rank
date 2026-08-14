if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
       
        command = input().split()
        cmd_type = command[0]

        
        if cmd_type == 'insert':
            my_list.insert(int(command[1]), int(command[2]))
        elif cmd_type == 'print':
            print(my_list)
        elif cmd_type == 'remove':
            my_list.remove(int(command[1]))
        elif cmd_type == 'append':
            my_list.append(int(command[1]))
        elif cmd_type == 'sort':
            my_list.sort()
        elif cmd_type == 'pop':
            my_list.pop()
        elif cmd_type == 'reverse':
            my_list.reverse()