import data



def addver (wishitem):
    if wishitem in data.wishlist:
        print("this item already exists in the wishlist")
        return False
    else:
        print("item was added to the wishlist ")
        return True
    
    
def removever (wishitem):
    if wishitem not in data.wishlist:
        print("this item does not exist in the wishlist ")
        return False
    else:
        print("item was removed from the wishlist ")
        return True