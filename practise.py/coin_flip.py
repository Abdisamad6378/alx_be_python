import random
names = input("Enter Everybodies name separated by comma:")
names_split=names.split(" ")
print(names_split)
choose=random.randint(1,4)
if choose == 1:
    print(" Osama will pay the bill")
elif choose == 2:
    print("hassan will pay the bill")
elif choose == 3:
    print("Fowzia will pay the bill")
else:
    print("Halima will pay the bill")
