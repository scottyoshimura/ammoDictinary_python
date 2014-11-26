#creating a dictionary

ammoDictionary ={".223":"a varmint round that can not go into a 5.56 caliber chambered barrel.",
                 "5.56": "a common round for AR-15 rifles.",
                 ".357": " a powerful handgun round. Lots of gunpowder behind the projectile.",
                 ".22":"a commoon low power pistol and rifle round",
                 "9mm": "close in calibre a 357, but not as powerful",
                 ".45":"america's favorite pistol round",
                 ".50 BMG":"a big ass round initially used in the Browning Machine Gun"}

choice = None
while choice != "0":

    print(
    """

    0-Quit
    1-look up a calibre defintion
    2-add a term
    3-redifine a term
    4-delete a term
    5-show the whole dictionary

    """
    )

    choice = input("choice:")
    print()

    #exit
    if choice=="0":
        print("Closing the ammo Dictionary.")

    #
    elif choice =="1":
        calibre=input("what calibre are you looking to find information: ")
        if calibre in ammoDictionary:
            value=ammoDictionary[calibre]
            print("\n", calibre, "is", value)
        else:
            print("\nThat Calibre is not in this dictionary. Use '.' if it is in the calibre")

    #add a calibre
    elif choice == "2":
        newCalibre = input("what Calibre do you want me to add?: ")
        if newCalibre not in ammoDictionary:
            newDefinition=input("\nWhat what is the description of this calibre?: ")
            ammoDictionary[newCalibre] = newDefinition
            print("\n", newCalibre, "has been added.")
        else:
            print("\nThat Calibre is already in this DB.")

    #change a calibre definition (value)
    elif choice == "3":
        calibre = input("what calibre do you want to change?: ")
        if calibre in ammoDictionary:
            newDefinition = input("what is the new definition?: ")
            ammoDictionary[calibre]=newDefinition
            print("\n", calibre, "has been redifined.")
        else:
            print("\nThat calibre isn't in this dictionary, try adding it if you wnat.")


    #change a calibre definition (value)
    elif choice == "4":
        calibre = input("what do you want me to delete?: ")
        if calibre in ammoDictionary:
            del ammoDictionary[calibre]
            print(calibre, " has been deleted.")
        else:
            print(calibre, " is not in the dictinary")


    #show all items
    elif choice == "5":
        for keys,values in ammoDictionary.items():
            print("\n")
            print(keys)
            print(values)
            
    #some other choice
    else:
        print("\nSorry, but ", choice, "is not a valid choice.")

input("\n\nSelect enter to exit this program")
                        
                        

            


