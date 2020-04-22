def check_chars (list1, list2):
    print(list1)
    print(list2)
    for l in list1:
        print("checking", l)
        if l in list2:
            print("found",l)
            list1.remove(l)
            list2.remove(l)
            print("removed",l)
    print(list1)
    print(list2)
    chars = list1 + list2
    return chars

def game (char_count):
    print(char_count)
    f = list('FLAMES')
    print(f)
    idx = 0
    while len(f) > 1:
        for i in range(char_count):
            idx += 1
            if idx > len(f):
                idx = 1
        f.remove(f[idx-1])
        idx -= 1
    return(f)





your_name = "Ram"
partner_name = "janaki"
name1list = list(your_name.lower())
name2list = list(partner_name.lower())

chars = check_chars(name1list,name2list)
print(chars)
char_count = len(chars)
#print(char_count)
result = game(char_count)
print("result is", result)
 