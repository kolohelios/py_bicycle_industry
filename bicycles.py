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

road_wheel = Wheel('road', 10, 50)
hybrid_wheel = Wheel('hybrid', 13, 40)
offroad_wheel = Wheel('offroad', 20, 38)

alum_frame = Frame('aluminum', 20, 250)
carbon_frame = Frame('carbon', 10, 500)
steel_frame = Frame('steel', 40, 100)

trek400 = Bicycle('Trek 400', offroad_wheel, steel_frame)
trek800 = Bicycle('Trek 800',hybrid_wheel, alum_frame)
trek1600 = Bicycle('Trek 1600', road_wheel, carbon_frame)
summit10 = Bicycle('Summit 10', offroad_wheel, steel_frame)
summit20 = Bicycle('Summit 20', hybrid_wheel, alum_frame)
summit40 = Bicycle('Summit 40', road_wheel, carbon_frame)

main_street_bike = Bike_Shop('Main Street Bike')

main_street_bike.add_bike_to_inventory(trek400, 3)
main_street_bike.add_bike_to_inventory(trek800, 2)
main_street_bike.add_bike_to_inventory(trek1600, 2)
main_street_bike.add_bike_to_inventory(summit10, 2)
main_street_bike.add_bike_to_inventory(summit20, 1)
main_street_bike.add_bike_to_inventory(summit40, 1)

customers = []
customers.append(Customers('Sam', 250))
customers.append(Customers('Bill', 500))
customers.append(Customers('George', 1000))

def find_customer(name):
    for customer in customers:
        if customer.name == name:
            return customer
    print('Customer was not found.')

for customer in customers:
    print('\nIntoducing customer', customer.name, 'who can afford the following bicycles:')
    main_street_bike.affordable_bikes(customer.fund)
    
main_street_bike.print_inventory('beginning')

main_street_bike.sell_bike(trek400, find_customer('Sam'))
main_street_bike.sell_bike(trek800, find_customer('Bill'))
main_street_bike.sell_bike(summit40, find_customer('George'))

main_street_bike.print_inventory('ending')

print('\nProfit was ${0:.2f}'.format(main_street_bike.profit))
