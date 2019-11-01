class employee :

    raise_amount = 1.2
    numof_emps = 7
    
    def __init__(self,first,last,pay):                 #kalo pake init gak perlu return udah bisa di panggil
        self.__first =first                              #mengkategorikan first sebagai object ant nanti akan dipanggil
        self.__last = last
        self.__pay = pay
        self.__email = first +'.'+ last +'@company.com'

        employee.numof_emps += 0
       
    
    def fullname(self):
        return '{} {}'.format(self.__first,self.__last)
    
    def setapply_raise(self):
        self.__pay = int(self.__pay * employee.raise_amount) #set self.pay ,,,isi file pay 
    
    def getapply_raise1(self):
        return self.__pay

class developer(employee):           #membuat subclass 
 
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang =prog_lang


emp_1 = employee('ahmad','qodir',30000,)
# emp_1.fullname()


print(emp_1.fullname())

emp_1.setapply_raise()
print(emp_1.setapply_raise())
# nama = input("nama")
# dev_1 = developer(nama,'abdul',50000,'python')
# dev_2 = developer('test','user',60000,'java')

# dev_1.fullname() #kalao bukan fungsi spesial fungsi harus dipanggil terlebih dahulu

# print(dev_1.fullname())

# dev_2.apply_raise1()
# print(dev_2.apply_raise1())

# print (dev_1.first)

# print (dev_1.prog_lang)

# dev_1.apply_raise()
# print(dev_1.pay)

# dev_2.apply_raise()
# print(dev_2.pay)


