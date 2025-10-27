import data
import reposetory
import validation



while True:
    
    print("1: add ")
    print("2: remove ")
    print("3: show the list ")
    print("4: exit the list ")
    operation=input("what would you like to do to ? ")
    
    if operation=="1":
        choice=input("what would you like to add ?")
        addvlad=validation.addver(choice)
        if addvlad==False:
            continue
        reposetory.add(choice)
        
    elif operation=="2":
        choice=input("what would you like to remove ?")
        removevlad=validation.removever(choice)
        if removevlad==False:
            continue
        reposetory.remove(choice)
        
    elif operation=="3":
        reposetory.show()
        
    else:
        exit()
        
    
    

