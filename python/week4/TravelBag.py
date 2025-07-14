# Create a list of items in your room you can potentially pack.
# Create an empty list to represent your travel bag 
# Repeatedly prompt the user for the index of an item to put in their travel bag by removing it from the the list of items in your room to your travel bag list.
# Once the list is complete, finalize it by creating a tuple representing your luggage. It should have every item in your travel bag. Empty the travel bag list as you do this.
# Print the contents of your luggage for the trip, as well as the number of items you decided to bring

bedroom = ["hat", "shoes", "sunscreen", "socks"]

travlebag = []


print("pack your bags")
print("Enter the index of an item you'd like to move from your room to your bag.")
print("type '100' done when you are done packing.\n")
print("your bedroom:")
print(bedroom)

item = int(input("item index: "))


while item != 100:
    travlebag.append(bedroom[item])
    bedroom.remove(bedroom[item])
    print("\nyour bedroom:")
    print(bedroom)
    print("\nyour travle bag:")
    print(travlebag)
    item = int(input("item index: "))

    print("your finished luggage: ")
    for item in travlebag:
        print(item)


