items=[("Burger",80),("Pizza",100),("Pasta",60),("Salad",90),("Sushi",130)]
def get_price(item):
    return item[1]
sorted_items=sorted(items,key=get_price,reverse=True)
print(sorted_items)
