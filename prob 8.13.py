# prob 8.13
# Name: Sher Azam Hussain
def my_profile(first_name,last_name,**data):
    """this function takes the first and last name of useer as positional arguments.
        there is also a dictionary argument which accept arbitrary key-value arguments"""    
    print('your provided data is as follow:')
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in data.items():
        profile[key] = value
    print(profile)
my_profile('Azam','hussain',nationality = 'pakistani',profession = 'student')

