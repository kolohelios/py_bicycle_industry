class Bicycle_Industry(object):
    '''All bicycle industry objects share some characteristics,
    
    like the name property.'''
    
    def __init__(self, name):
        self.name = name
        
class Manufacturer(Bicycle_Industry):
    '''This class represents bicycle manufacturers, which
    
    sell bicycles at a certain margin to bike shops.'''
    
    _margin_percentage = 0
    
    def __init__(self, name, margin):
        super().__init__(name)
        self._margin_percentage = margin
        
    def get_margin(self):
        return self._margin_percentage
        
    def sell_bike_to_bike_shop(self, bike):
        # TODO should do something more than just return the bike here
        return bike

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
    
    def __init__(self, name, manufacturer, wheel, frame):
        weight = wheel.weight * 2 + frame.weight
        cost = (wheel.cost * 2 + frame.cost)
        self.price = cost + cost * manufacturer.get_margin() / 100
        super().__init__(name, weight, cost)
        self.wheel = wheel
        self.frame = frame
        self.manufacturer = manufacturer

class Bike_Shop(Bicycle_Industry):
    '''This class contains bike shops.
    
    Bike shops sell bicycles from their stock to customers.'''
    
    _margin_percentage = 20
    
    def __init__(self, name):
        super().__init__(name)
        self.inventory = []
        self.profit = 0
    
    def buy_bike_from_manufacturer(self, bike, qty):
        if bike.manufacturer.sell_bike_to_bike_shop(bike) == bike:
            self.inventory.append({'bike': bike, 'stock': qty})
            print('{} "{}" bikes purchased from {}.'.format(qty, bike.name, bike.manufacturer.name))
        
    def price(self, bike):
        return bike.price + bike.price * self._margin_percentage / 100

    def sell_bike(self, bike, customer):
        sales_price = self.price(bike)
        print(customer.name, 'purchased a', bike.name, 'for ${0:.2f}'.format(sales_price), end='. ')
        customer.buy_bike(bike, sales_price)
        for bike_from_inventory in self.inventory:
            if(bike_from_inventory['bike'].name == bike.name):
                bike_from_inventory['stock'] -= 1
        self.profit += sales_price - bike.price
    
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
