def swap_case(s):
    # s = str(input()
    # values = s.split()
    str_to_list = list(s)
    list_length = len(str_to_list)
    for x in range(list_length):
        if(str_to_list[x].isupper()== 1):
            str_to_list[x] = str_to_list[x].lower()
        elif(str_to_list[x].islower() == 1):
            str_to_list[x] = str_to_list[x].upper()
            
    return ''.join(str_to_list)

        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)