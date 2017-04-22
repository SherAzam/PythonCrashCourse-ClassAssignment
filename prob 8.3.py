# prob 8.3

def make_shirt(size = 'XL', text = 'i love python'):
    message = 'the size of shirt is '
    message1 = ' is printed on the shirt'
    print(message + size + '.'+ ' ' + text + message1)
# function is called using default arguments    
make_shirt()
# function is called using one default arguments
make_shirt(text = '\"python geek\"')
# both arguments are changed
make_shirt('small', '\"Tech geek\"')