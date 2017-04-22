# prob 8.5

def describe_city(city = 'Gilgit', country = 'Pakistan'):
    
    print(city + ' is city of ' + country)
# function is called using default arguments    
describe_city()
# function is called using one default arguments
describe_city('Berlin', 'Germany')
describe_city(city = 'Karachi')
# both arguments are changed
describe_city(country = 'USA', city = 'New York')