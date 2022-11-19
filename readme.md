###Logic

---

You are going to make the tea system in python using if-else statement with the following inputs
    
- Milk
- Tea
- Water
- Pan
- Fire
- Stove
- Sugar

---

###Pseudo code

- Taking inputs

---

    milk_have = input("Do you have milk ? Yes/No)
    tea = input("Do you have tea ? Yes/No)
    water = input("Do you have water ? Yes/No)
    pan = input("Do you have pan ? Yes/No)
    fire = input("Do you have fire ? Yes/No)
    stove = input("Do you have stove ? Yes/No)
    sugar = input("Do you have sugae ? Yes/No)

---


- Logic of the code

---

 Declaring a variable "things_need_to_buy" to add the list of products which the tea maker doesn't have!

    if milk_have == "No" or "no":
        adds the milk packet product to the things to buy list
    if tea == "No" or "no":
        adds the tea bags product to the things to buy list
    if water == "No" or "no":
        adds the water bottle product to the things to buy list
    if pan == "No" or "no":
        adds the milk pan product to the things to buy list
    if fire == "No" or "no":
        adds the gas lighter product to the things to buy list
    if stove == "No" or "no":
        adds the gas stove product to the things to buy list
    if sugar == "No" or "no":
        adds the sugar packet product to the things to buy list

    if things_need_to_buy has no string :
        print("You can make tea and enjoy")
    else :
        print(things_need_to_buy)

---

