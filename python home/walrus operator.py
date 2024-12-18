#walrus operator se code ek line me likh skteb hai
# syntax ":=" --> "is equal to" , bas yhi hai walrus operator

# without walrus operator
foods = list()
while True:
  food = input("What food do you like?: ")
  if food == "quit":
      break
  foods.append(food)

  #withn walrus operator
  foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)