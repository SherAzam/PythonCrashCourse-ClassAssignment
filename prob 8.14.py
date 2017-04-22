# prob 8.14
# Name: Sher Azam Hussain
def car_profile(manufacturer,model,**features):
    """this function takes the manufacturer and model name of car as positional arguments.
        there is also a dictionary argument which accept arbitrary key-value arguments"""    
    print('your provided data is as follow:')
    profile = {}
    profile['Manufacturer'] = manufacturer
    profile['model'] = model
    for key, value in features.items():
        profile[key] = value
    print(profile)
car_profile('SpaceX','Falcon 8',speed = '200miles/h',colour = 'blue')


