prompts = ["name:", "number:", "adjective:", "noun:", "food (plural):", "noun (plural):", "verb endinging in -ed:"]

# use a for loop to iterate through each prompt
# create an empty list to store response inputs

answers = []
for i in range(len(prompts)):
  answer = input(prompts[i])
  answers.append(answer)

# use the index of each answers list item to replace relevant answers
# use .lower() and .capitalize() to catch any grammar errors
# use int for the number response to only accept numbers
# add \n to create new lines

print(f"Come on over to {answers[0].capitalize()}'s' Pizza Parlor where you can enjoy your favorite {answers[2].lower()}-dish pizza.\nYou can try our famous {answers[4].lower()}-lovers pizza,\nor select from our list of {int(answers[1].lower())} dry toppings, \nincluding delicious {answers[3].lower()}, {answers[4].lower()}, and many more. \nOur crusts are hand-{answers[6].lower()} and basted in {answers[3].lower()} to make \nthem seem more Hand-made.")
