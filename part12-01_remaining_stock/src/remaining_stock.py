def sort_by_quantity(item: tuple):
    return item[2] #return quantity

def sort_by_remaining_stock(items: list):
    return sorted(items, key=sort_by_quantity) #using func sorted to pass items list to func sort by quantity



if __name__ == "__main__":
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)] #initial declaration

    for product in sort_by_remaining_stock(products): #passing the list
        print(f"{product[0]} {product[2]} pcs")
