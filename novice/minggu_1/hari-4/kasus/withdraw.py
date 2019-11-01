class Withdraw:
    __withdraw=0
    def setwithdraw(self,withdraw):  #fungsinya buat ngeset nilai yang akan di panggil
        self.__withdraw =withdraw
        return self.__withdraw
    
    def setbalance(self,balance,median):
        self.__balance = balance
        self.median = median
    
    def getwithdraw(self):              #untuk manggil nilai yang udah diset
        return self.__withdraw 
    def getbalance(self):
        return self.__balance
   

a =Withdraw()                         #bikin object namanya a
input1 =int(input("masukan withdraw"))
input2 = int(input("masukan balance"))
a.setwithdraw(input1)                 #memanggil fungsi methode withdraw
a.setbalance(input2,8)                # ngasih nilai ke metode /fungsi set balan
print (a.median)                      # memanggil tanpa menggunakan return
angka1 =a.getwithdraw()               #mereturn nilai a dari get
angka2 =a.getbalance()



print(angka1)
print(angka2)


