class Bicycle_Industry(object):
    '''All bicycle industry objects share some characteristics,
    
    like the name property.'''
    
    def __init__(self, name):
        self.name = name
        
class Bicycle_Components(Bicycle_Industry):
    '''The bicycle and bicycle components all share some characteristics, which
    
    in the spirt of writing DRY code, we can abstract and extend with.'''
    
    def __init__(self, name, weight, cost):
        super().__init__(name)
        self.weight = weight
        self.cost = cost
        
class Wheel(Bicycle_Components):
    '''Wheels, along with frames, 
    
    belong to bicycles'''
    
    def __init__(self, name, weight, cost):
        super().__init__(name, weight, cost)

class Frame(Bicycle_Components):
    '''Frames, along with wheels,
    
    belong to bicycles'''
    
    def __init__(self, material, weight, cost):
        super().__init__('', weight, cost)
        self.material = material

class Bicycle(Bicycle_Components):
    '''This class contains bicycles.
    
    Customers may purchase bicycles from bike shops.'''
    
    def __init__(self, name, wheel, frame):
        weight = wheel.weight * 2 + frame.weight
        cost = wheel.cost * 2 + frame.cost
        super().__init__(name, weight, cost)
        self.wheel = wheel
        self.frame = frame


class Bike_Shop(Bicycle_Industry):
    '''This class contains bike shops.
    
    Bike shops sell bicycles from their stock to customers.'''
    
    _margin_percentage = 20
    
    def __init__(self, name):
        super().__init__(name)
        self.inventory = []
        self.profit = 0
        
    def add_bike_to_inventory(self, bike, stock):
        self.inventory.append({'bike': bike, 'stock': stock})
        print('Bike "{}" added to inventory.'.format(bike.name))
        
    def price(self, bike):
        return bike.cost + bike.cost * self._margin_percentage / 100

    def sell_bike(self, bike, customer):
        sales_price = self.price(bike)
        print(customer.name, 'purchased a', bike.name, 'for ${0:.2f}'.format(sales_price), end='. ')
        customer.buy_bike(bike, sales_price)
        for bike_from_inventory in self.inventory:
            if(bike_from_inventory['bike'].name == bike.name):
                bike_from_inventory['stock'] -= 1
        self.profit += sales_price - bike.cost
    
    def affordable_bikes(self, fund):
        for bike in self.inventory:
            price = self.price(bike['bike'])
            if price <= fund:
                print(bike['bike'].name, ':', '${0:.2f}'.format(price))
                
    def print_inventory(self, time_period):
        if len(self.inventory):
            print('\nThe bike shop\'s {} inventory is as follows:'.format(time_period))
            print('Bike Name : Stock : Cost : Sales Price')
            for bike in self.inventory:
                print(bike['bike'].name, ':', bike['stock'], ':', '${0:.2f}'.format(bike['bike'].cost), ':', '${0:.2f}'.format(self.price(bike['bike'])))
        else:
            print('There are no bikes in stock.')
    
class Customers(Bicycle_Industry):
    '''This class contains customers.
    
    Customers buy bicycles from bike shops.'''
    
    def __init__(self, name, fund):
        super().__init__(name)
        self.fund = fund
        self.bike = {}
    
    def buy_bike(self, bike, price):
        self.bike = bike
        self.fund -= price
        print('They have ${0:.2f} left.'.format(self.fund))
