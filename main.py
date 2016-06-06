import bicycles

if __name__ == '__main__':
    road_wheel = bicycles.Wheel('road', 10, 50)
    hybrid_wheel = bicycles.Wheel('hybrid', 13, 40)
    offroad_wheel = bicycles.Wheel('offroad', 20, 38)
    
    alum_frame = bicycles.Frame('aluminum', 20, 250)
    carbon_frame = bicycles.Frame('carbon', 10, 500)
    steel_frame = bicycles.Frame('steel', 40, 88)
    
    trek = bicycles.Manufacturer('Trek', 25)
    summit = bicycles.Manufacturer('Summit', 20)
    
    trek400 = bicycles.Bicycle('Trek 400', trek, offroad_wheel, steel_frame)
    trek800 = bicycles.Bicycle('Trek 800', trek, hybrid_wheel, alum_frame)
    trek1600 = bicycles.Bicycle('Trek 1600', trek, road_wheel, carbon_frame)
    summit10 = bicycles.Bicycle('Summit 10', summit, offroad_wheel, steel_frame)
    summit20 = bicycles.Bicycle('Summit 20', summit, hybrid_wheel, alum_frame)
    summit40 = bicycles.Bicycle('Summit 40', summit, road_wheel, carbon_frame)
    
    main_street_bike = bicycles.Bike_Shop('Main Street Bike')
    
    main_street_bike.buy_bike_from_manufacturer(trek400, 3)
    main_street_bike.buy_bike_from_manufacturer(trek800, 2)
    main_street_bike.buy_bike_from_manufacturer(trek1600, 2)
    main_street_bike.buy_bike_from_manufacturer(summit10, 2)
    main_street_bike.buy_bike_from_manufacturer(summit20, 1)
    main_street_bike.buy_bike_from_manufacturer(summit40, 1)
    
    customers = []
    customers.append(bicycles.Customers('Sam', 250))
    customers.append(bicycles.Customers('Bill', 500))
    customers.append(bicycles.Customers('George', 1000))
    
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