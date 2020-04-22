class Flames:
    def check_chars(self, name1, name2):
        name1 = name1.lower()
        name1 = name1.replace(" ","")
        list1 = list(name1)
        name2 = name2.lower()
        name2 = name2.replace(" ","")
        list2 = list(name2)
        for l in list1:
            if l in list2:
                list1.remove(l)
                list2.remove(l)
        chars = list1 + list2
        char_count = len(chars)
        self.game(char_count)

    def game(self, char_count):
        f = list('FLAMES')
        idx = 0
        while len(f) > 1:
            for i in range(char_count):
                idx += 1
                if idx > len(f):
                    idx = 1
            f.remove(f[idx-1])
            idx -= 1
        f = str(f) # Need to make this as a string
        self.result(f)
    
    def result(self,char):
        if char == 'F':
            print("The relationship between names is Friends")
        else:
            print("other")



your_name = "Ram"
partner_name = "janaki"
F = Flames()
F.check_chars(your_name,partner_name)
 