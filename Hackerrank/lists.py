# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

if __name__ == '__main__':
    list1 = []
    n = int(input())
    for _ in range(n):
        command,*line = input().split()
        # values = line
        if(command == "insert"):
            list1.insert(int(line[0]), int(line[1]))
    # print(list1)
        elif(command == "print"):
            print(list1)
        elif(command == "remove"):
            list1.remove(int(line[0]))
        elif(command == "append"):
            list1.append(int(line[0]))
        elif(command == "sort"):
            list1.sort()
        elif(command == "pop"):
            list1.pop()
        elif(command == "reverse"):
            list1.reverse()
        

        
