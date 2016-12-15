#Choose your own adventure - Amelia can choose

#Introduction - Choose a gift
print("Choose your own adventure - Amelia can choose!\n")

print("It is Christmas and there is a box for you! What is inside?")
print("1. A puppy \n2. A kitty \n3. A bunny \n4. A rock")

gift_choice = raw_input("Enter a number from the list above: ")

#Body - You choose a puppy
if gift_choice == str(1):
	print("You open the box and out pops a puppy! He jumps on you and covers you in kisses. Then he runs off and he pees in the corner!\n")
	print("You see the pee. How do you respond?")
	print("1. You kick the puppy and throw him outside in the subzero air.\
		\n2. You pretend not to see the puppy excrement and go off to play with something else. 		\n3. You clean up the puppy excrement with a towel and shout 'No!' \n")
	
	pee_choice = raw_input("Enter a number from the list above: ")

	if pee_choice == str(1):
		print("Your parents see how mean you are to the puppy and give him away to a nicer family. You are given a homemade sweater instead. \nThe End!")
	elif pee_choice == str(2):
		print("The puppy pee dries and no one notices. It is only a matter of seconds before he pees again. It is not long before a previously nice house becomes full of puppy pee. \nThe End!")
	else:
		print("The puppy learns that the corner is no place to pee. Later on with more training he learns that the right place to pee is outside, creating patches of yellow snow and dead grass all over the yard. \n The End!")

#Body - You choose a kitty
elif gift_choice == str(2):
	print("You open the box and out pops a kitty! She is angry and walks off to the corner.\n")
	print("Kitty is angry. What do you do?")
	print("1. Pummel the kitty with hardened Christmas Cookies until she changes her tune. \
		\n2. Ignore the kitty. You didn't really want her anyway. \
		\n3. Go after the kitty and touch her fur until she bites you.")
	
	kitty_choice = raw_input("Enter a number from the list above: ")

	if kitty_choice == str(1):
		print("Your meanness to the kitty causes her to become permanently mean, and eventually she bites and scratches so many people that your parents have to surrender her to a shelter. \nThe End!")
	elif kitty_choice == str(2):
		print("The kitty doesn't do much or say much. As you grow up she just sort of exists until you go off to college and leave her with your parents. \nThe End!")
	else:
		print("You learn that you don't choose when to love the kitty, but rather that the kitty chooses when to love you. She loves you so much that she leaves you dead birds as gifts in your bed. \nThe End!")

#Body - You choose a bunny
elif gift_choice == str(3):
	print("You open the box and out pops a bunny! Her fur is soft and she sniffs you until she hops away.\n")
	print("The bunny comes back. What do you offer her?")
	print("1. A nice juicy carrot \
		\n2. A noogie \
		\n3. A one way ticket to the snowbank outside.")
	bunny_choice = raw_input("Enter a number from the list above: ")
	if bunny_choice == str(1):
		print("Bunnies usually love carrots. This one does not. This bunny likes to eat clothes and homework. You learn to put both in high places for the rest of the bunny's 20 years. \nThe End!")
	elif bunny_choice == str(2):
		print("Bunny likes noogies. This is the start of a beautiful friendship. \nThe End!")
	else:
		print("Bunny hops away after getting thrown out in the cold. She eventually gets trapped in an iceblock and remains there until spring. \nThe End!")

#Body - You choose a rock
else:
	print("You open the box and inside is a rock. It doesn't do much.\n")
	print("You look at the rock. How do you feel?")
	print("1. Alright. Rocks are cool! \
		\n2. You wonder what you did in your life to make your parents do this to you. \
		\n3. You feel very angry. You want to yell at the rock.")
	rock_choice = raw_input("Enter a number from the list above: ")
	if rock_choice == str(1):
		print("Yes, indeed you have a cool rock. This is the beginning of a fascination with geology that extends into your adult life. \nThe End!")
	elif rock_choice == str(2):
		print("You harbor unspoken hostility toward your parents that never really resolves. But, you did find ways to play with the rock. Take that! \nThe End!")
	else:
		print("You yell at the rock. Your parents tell you to stop being weird. \nThe End!")
