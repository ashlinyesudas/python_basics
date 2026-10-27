#shopping card
foods=[]
prices=[]
amount=0

while True:
    food=input("enter the food (q to quit) ")
    if food.lower()=="q":
        break
    else:
        foods.append(food)
        
        price=int(input("enter the price of the food :"))
        prices.append(price)
        
for i in foods:
  print(i,end="_")
        
for j in prices:
            amount=amount+j
print(f"the total amount of food is {amount}")
        
        
        
        
    