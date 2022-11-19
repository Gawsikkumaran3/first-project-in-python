"""_summary_

- First you have to create the readme.md
    file in which you have to define yours
    logic - what you are going to do.

"""

milk_have = input("Do you have milk ? Yes/No ")
tea = input("Do you have tea ? Yes/No ")
water = input("Do you have water ? Yes/No ")
pan = input("Do you have pan ? Yes/No ")
fire = input("Do you have fire ? Yes/No ")
stove = input("Do you have stove ? Yes/No ")
sugar = input("Do you have sugar ? Yes/No ")

things_need_to_buy = ""



if milk_have == "No" or milk_have == "no":
	things_need_to_buy = things_need_to_buy + "," + "milk packets"
if tea == "No" or tea == "no":
	things_need_to_buy = things_need_to_buy + "," + "tea bags"
if water == "No" or water == "no":
	things_need_to_buy = things_need_to_buy + "," + "water bottle"
if pan == "No" or pan == "no":
	things_need_to_buy = things_need_to_buy + "," + "milk pan"
if fire == "No" or fire == "no":
	things_need_to_buy = things_need_to_buy + "," + "gas lighter"
if stove == "No" or stove == "no":
	things_need_to_buy = things_need_to_buy + "," + "gas stove"
if sugar == "No" or sugar == "no":
	things_need_to_buy = things_need_to_buy + "," + "sugar packet"


if things_need_to_buy == "":
	print ("You can make tea and enjoy")
else:
	print("You should buy" + things_need_to_buy)

