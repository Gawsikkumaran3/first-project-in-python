"""_summary_

- First you have to create the readme.md
    file in which you have to define yours
    logic - what you are going to do.

"""

track_products = []
water_added = 'no'
tea_added = 'no'
milk_added = 'no'
fire_added = 'no'
stove_added = 'no'
pan_added = 'no'
sugar_added = 'no'

while(True):

	if water_added == 'no' or water_added == 'No': water = input("Do you have enough water ? Yes/No ")
	if ((water=="Yes") or (water=="yes")) : 
		water_added = 'yes'
		track_products.append('1')
	if ((water_added=="Yes") or (water_added=="yes")) and ('1' in track_products):
		pass
		
		if tea_added == 'no' or tea_added == 'No': tea = input("Do you have tea bags ? Yes/No ")
		if ((tea=="Yes") or (tea=="yes")) : 
			tea_added = 'yes'
			track_products.append('2')
		if ((tea_added=="Yes") or (tea_added=="yes")) and ('2' in track_products):
			pass

			if milk_added == 'no' or milk_added == 'No': milk = input("Do you have enough milk ? Yes/No ")
			if ((milk=="Yes") or (milk=="yes")) : 
				milk_added = 'yes'
				track_products.append('3')
			if ((milk_added=="Yes") or (milk_added=="yes")) and ('3' in track_products):
				pass

				if fire_added == 'no' or fire_added == 'No' : fire=input("Do you have adequate amount of fire/gas to make tea ? Yes/No ")
				if ((fire=="Yes") or (fire=="yes")) : 
					fire_added = 'yes'
					track_products.append('4')
				if ((fire_added=="Yes") or (fire_added=="yes")) and ('4' in track_products):
					pass

					if stove_added == 'no' or stove_added == 'No': stove = input("Do you have stove to place the pan ? Yes/No ")
					if ((stove=="Yes") or (stove=="yes")) : 
						stove_added = 'yes'
						track_products.append('5')
					if ((stove_added=="Yes") or (stove_added=="yes")) and ('5' in track_products):
						pass

						if pan_added == 'no' or pan_added == 'No': pan = input("Do you have pan to boil the tea ? Yes/No ")
						if ((pan=="Yes") or (pan=="yes")) : 
							pan_added = 'yes'
							track_products.append('6')
						if ((pan_added=="Yes") or (pan_added=="yes")) and ('6' in track_products):
							pass

							if sugar_added == 'no' or sugar_added == 'No': sugar = input("Do you have sugar packets ? Yes/No ")
							if ((sugar=="Yes") or (sugar=="yes")) : 
								sugar_added = 'yes'
								track_products.append('7')
							if ((sugar_added=="Yes") or (sugar_added=="yes")) and ('7' in track_products):
								print("")
								print("Adding water...Please wait...")
								print("")
								print("Adding tea bags...Please wait...")
								print("")
								print("Adding milk...Please wait...")
								print("")
								print("Turning up the fire...Please wait...")
								print("")
								print("Heating the stove...Please wait...")
								print("")
								print("Placing the pan...Please wait...")
								print("")
								print("Adding the sugar and mixing...Please wait...")
								print("")
								print("Hurrah! Here is your tea , you can taste and enjoy it!")
								break

							elif sugar=="No" or sugar=="no":

								print("")
								print("Add sugar packets to the system!")

								while True:
									print("")
									sugar_added = input("Are the sugar packets added ? Yes/No ")
									
									if sugar_added=='No' or sugar_added=='no':
										confirmation = input("Do you want to continue making tea ? Yes/No ")
										if confirmation=='Yes' or confirmation=='yes':
											pass
										elif confirmation=='No' or confirmation=='no':
											print("Exiting tea making!")
											quit()
										else:
											print("Please enter a valid input : Yes/no")

									elif sugar_added=="Yes" or sugar_added=="yes":
										track_products.append('7')
										break

							else:
								print("Please enter a valid input : Yes/No")

						elif pan=="No" or pan=="no":

							print("")
							print("Add pan to the system!")
								
							while True:
								print("")
								pan_added = input("Is the pan added ? Yes/No ")

								if pan_added=='No' or pan_added=='no':
									confirmation = input("Do you want to continue making tea ? Yes/No ")
									if confirmation=='Yes' or confirmation=='yes':
										pass
									elif confirmation=='No' or confirmation=='no':
										print("Exiting tea making!")
										quit()
									else:
										print("Please enter a valid input : Yes/no")
								
								elif pan_added=="Yes" or pan_added=="yes":
									track_products.append('6')
									break

								else:
									print("Please enter a valid input : Yes/No")

						else:
							print("Please enter a valid input : Yes/No")

					elif stove=="No" or stove=="no":

						print("")
						print("Add stove to the system!")

						while True:
							print("")
							stove_added = input("Is the stove added ? Yes/No ")

							if stove_added=='No' or stove_added=='no':
								confirmation = input("Do you want to continue making tea ? Yes/No ")
								if confirmation=='Yes' or confirmation=='yes':
									pass
								elif confirmation=='No' or confirmation=='no':
									print("Exiting tea making!")
									quit()
								else:
									print("Please enter a valid input : Yes/no")

							elif stove_added=="Yes" or stove_added=="yes":
								track_products.append('5')
								break	

							else:
								print("Please enter a valid input : Yes/No")

					else:
						print("Please enter a valid input : Yes/No")	

				elif fire=="No" or fire=="no":

					print("")
					print("Add adequate amount of fire/gas to the system!")

					while True:
						print("")
						fire_added = input("Is the fire/gas added ? Yes/No ")

						if fire_added=='No' or fire_added=='no':
							confirmation = input("Do you want to continue making tea ? Yes/No ")
							if confirmation=='Yes' or confirmation=='yes':
								pass
							elif confirmation=='No' or confirmation=='no':
								print("Exiting tea making!")
								quit()
							else:
								print("Please enter a valid input : Yes/no")

						elif fire_added=="Yes" or fire_added=="yes":
							track_products.append('4')
							break

						else:
							print("Please enter a valid input : Yes/No")

				else:
					print("Please enter a valid input : Yes/No")

			elif milk=="No" or milk=="no":

				print("")
				print("Add adequate amount of milk to the system!")

				while True:
					print("")
					milk_added = input("Is the milk added ? Yes/No ")

					if milk_added=='No' or milk_added=='no':
						confirmation = input("Do you want to continue making tea ? Yes/No ")
						if confirmation=='Yes' or confirmation=='yes':
							pass
						elif confirmation=='No' or confirmation=='no':
							print("Exiting tea making!")
							quit()
						else:
							print("Please enter a valid input : Yes/no")

					elif milk_added=="Yes" or milk_added=="yes":
						track_products.append('3')
						break

					else:
						print("Please enter a valid input : Yes/No")	
			else:
				print("Please enter a valid input : Yes/No")

		elif tea=="No" or tea=="no":

			print("")
			print("Add adequate amount of tea bags to the system!")

			while True:
				print("")
				tea_added = input("Is the tea bag added ? Yes/No ")

				if tea_added=='No' or tea_added=='no':
					confirmation = input("Do you want to continue making tea ? Yes/No ")
					if confirmation=='Yes' or confirmation=='yes':
						pass
					elif confirmation=='No' or confirmation=='no':
						print("Exiting tea making!")
						quit()
					else:
						print("Please enter a valid input : Yes/no")

				elif tea_added=="Yes" or tea_added=="yes":
					track_products.append('2')
					break	

				else:
					print("Please enter a valid input : Yes/No")

		else:
			print("Please enter a valid input : Yes/No")		
							
	elif water=="No" or water=="no":

		print("")
		print("Add adequate amount of water to the system!")

		while True:
			print("")
			water_added = input("Is the water added ? Yes/No ")

			if water_added=='No' or water_added=='no':
				confirmation = input("Do you want to continue making tea ? Yes/No ")
				if confirmation=='Yes' or confirmation=='yes':
					pass
				elif confirmation=='No' or confirmation=='no':
					print("Exiting tea making!")
					quit()
				else:
					print("Please enter a valid input : Yes/no")

			elif water_added=="Yes" or water_added=="yes":
				track_products.append('1')
				break

			else:
				print("Please enter a valid input : Yes/No")
					
	else:
		print("Please enter a valid input : Yes/No")		

			



