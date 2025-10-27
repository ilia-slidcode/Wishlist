import data


def add (wishitem):
    data.wishlist.append(wishitem) 
    
def remove (wishitem):
    data.wishlist.remove(wishitem)
    
def show ():
    print(data.wishlist)