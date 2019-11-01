class Product:
    __vendor_message = "Ini adalah rahasia"
    name = ""
    price = ""
    size = ""
    unit = ""

    def __init__(self, name):
        print ("Ini adalah constructor")
        self.name = name
        self.unit = "ml"
        self.size = 250

    def get_vendor_message(self):
        print (self.__vendor_message)

    def set_price(self, price):
        self.price = price

p = Product("Ultora Milek")
p.set_price(5500)

print ("%s dengan ukuran %s %s harganya Rp. %d" % (p.name, p.size, p.unit, p.price))
# print p.__vendor_message

p.get_vendor_message()

p1 = Product("Indomilek")
p1.set_price(5000)

print ("%s dengan ukuran %s %s harganya Rp. %d" % (p.name, p.size, p.unit, p.price))

print (p == p)
print (p1 == p1)
print (p == p1)