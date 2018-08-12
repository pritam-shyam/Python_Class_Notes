
class inventoryItem:
    itemCount = 0

    def __init__(self, sku, cost, category):
        self.sku = sku
        self.cost = cost
        self.cat = category
        inventoryItem.itemCount += 1

    def getCost(self):
        print("Our cost is ", self.cost)

    def printPrice(self):
        print("Our price is ", self.cost * 1.5)

class washer(inventoryItem):
    def __init__(self, sku, cost, frontLoad):
        inventoryItem.__init__(self, sku, cost, "Washer")
        self.fl = frontLoad
    def printType(self):
        if frontLoad:
            print("Frontload")
        else:
            print("Sideload")
    def printPrice(self):
        print("Our price is ", self.cost * 1.7)


class dryer(inventoryItem):
    def __init__(self, sku, cost, btu):
        inventoryItem.__init__(self, sku, cost, "Washer")
        self.btus = btu
    def printBtus(self):
        print(self.btu)
    def printPrice(self):
        print("Our price is ", self.cost * 1.3)



def printCost(inItem): # "polymorphism" example, that is, all inventoryItems have a cost
    print(inItem.getCost())

w = washer(123, 600, True)
d = dryer(124, 500, 25000)

w.printPrice()
d.printPrice()
