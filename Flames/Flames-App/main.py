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
        print(char_count)
        self.game(char_count)

    def game(self, char_count):
        f = list('FLAMES')
        #starting the FLAMES counter at zero so we can increment it by one and start counting from 'F'
        flames_counter = 0
        #Running a While loop till we have only one item in the list f i.e., F, L, A, M, E, S
        while len(f) > 1:
            #run a for loop to run for char_count number of times where it will be going through FLAMES.
            for i in range(char_count):
                #increasing the count on FLAMES by one until we reach 'S'
                flames_counter += 1
                print(flames_counter)
                #Run this if loop to reset the counter to 'F' when it reach 'S'.
                if flames_counter > len(f):
                    flames_counter = 1
            print(f[flames_counter-1])
            #Remove the letter that meets the char_count number. Doing counter -1 to meet the python indexing which starts at '0'
            f.remove(f[flames_counter-1])

            flames_counter -= 1
        f = str(f) # Need to make this as a string
        print(f)
        self.result(f)
    
    def result(self,char):
        self.
        if char == 'F':
            print("The relationship between names is Friends")
        elif char == 'L'
            print("The relationship between names is Love")
        elif char == 'A'
            print("The relationship between names is Affection")
        elif char == 'M'
            print("The relationship between names is Affection")


your_name = "a"
partner_name = "b"
F = Flames()
F.check_chars(your_name,partner_name)
