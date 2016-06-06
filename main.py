import bicycles

if __name__ == '__main__':
    road_wheel = bicycles.Wheel('road', 10, 50)
    hybrid_wheel = bicycles.Wheel('hybrid', 13, 40)
    offroad_wheel = bicycles.Wheel('offroad', 20, 38)
    
    alum_frame = bicycles.Frame('aluminum', 20, 250)
    carbon_frame = bicycles.Frame('carbon', 10, 500)
    steel_frame = bicycles.Frame('steel', 40, 100)
    
    trek400 = bicycles.Bicycle('Trek 400', offroad_wheel, steel_frame)
    trek800 = bicycles.Bicycle('Trek 800',hybrid_wheel, alum_frame)
    trek1600 = bicycles.Bicycle('Trek 1600', road_wheel, carbon_frame)
    summit10 = bicycles.Bicycle('Summit 10', offroad_wheel, steel_frame)
    summit20 = bicycles.Bicycle('Summit 20', hybrid_wheel, alum_frame)
    summit40 = bicycles.Bicycle('Summit 40', road_wheel, carbon_frame)
    
    main_street_bike = bicycles.Bike_Shop('Main Street Bike')
    
    main_street_bike.add_bike_to_inventory(trek400, 3)
    main_street_bike.add_bike_to_inventory(trek800, 2)
    main_street_bike.add_bike_to_inventory(trek1600, 2)
    main_street_bike.add_bike_to_inventory(summit10, 2)
    main_street_bike.add_bike_to_inventory(summit20, 1)
    main_street_bike.add_bike_to_inventory(summit40, 1)
    
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