n=input(str(("Введіть натуральне чотирьохзначне число: ")))
while len(n) < 4 or len(n) > 4 or n.isdigit() == 0:
  n=input(str(("Введіть число ще раз, так як воно не чотирьохзначне:     ")))
max_value=max(n)
print("Найбільша цифра у числі: ", max_value)