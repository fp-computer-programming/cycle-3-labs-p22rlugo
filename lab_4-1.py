# Ryan Lugo: RJL 9/30/21

magic_charge = int(input("What's your magic charge?: "))
shield_charge = int(input("What's your shield charge?: "))

if magic_charge <= 90 and shield_charge <= 75: 
    print ("The dragon burns you to a crisp.")
else:
    print ("You defeated the dragon! But the princess is in another castle.")