class class_item:

    discount = 0.2 # 20% discount

    list_class_instances = []

    def __init__(self, l_name: str, l_price: float, l_quantity=0):
        #validation
        assert l_price >= 0 , f"price {l_price} is less than ZERO"
        assert l_quantity >= 0 , f"quantity {l_quantity} is less than ZERO"
        #variable initialization
        self.name = l_name
        self.price = l_price
        self.quantity = l_quantity

        class_item.list_class_instances.append(self)

    def total_price(self):
        return self.price * self.quantity
    
    def discounted_price(self):
        return self.price * ( 1 - self.discount)
    
    def __repr__(self):
        return f"{self.name} - {self.price} - {self.quantity} - {self.discount}"
    
class_item_1 = class_item("Apple",50, 10)

class_item_2 = class_item("Mango",40)

class_item_3 = class_item("Orange",10)

print(class_item_1.total_price())
print(class_item_2.total_price())

print(class_item.discount)
print(class_item_1.discount)


print(class_item_1.discounted_price())

class_item_2.discount = 0.3
print(class_item_2.discounted_price())

print(class_item.__dict__)
print(class_item_1.__dict__)

print(class_item.list_class_instances)

for instance in class_item.list_class_instances:
    print(instance.name)
    