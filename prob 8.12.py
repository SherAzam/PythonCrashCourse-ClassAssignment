# prob 8.12
# Name: Sher Azam Hussain
def sandwiches(*ingredients):
    ""'this function takes the ingredients as arguments save them in a tuple and dispplay the ingredients"""'
    print('your ordered sandwich contain following ingredients:')
    for ingredient in ingredients:
        print('- ' + inggredient)
sandwiches('bread')
sandwiches('bread','onion')
sandwiches('onion','bread','chees','butter')
