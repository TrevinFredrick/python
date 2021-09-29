class product:
    productname="puma"
    mfd="2021-09-12"
    weight="950 grams"
    price=200
    def display(self):
        print(self.productname,self.mfd,self.weight,self.price)
obj=product()
obj.display()

