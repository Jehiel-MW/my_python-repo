value_1 = int(input("Enter a value: "))
value_2 = int(input("Enter a value: "))

add = value_1 + value_2

if value_1 or value_2 < 0:
    if add == 5:
        print("The {} Naira note in Nigeria has the image of Sir Tafawa Balewa".format(add))
    elif add == 10:
        print("The {} Naira note in Nigeria has the image of Alvan Ikoku".format(add))
    elif add == 20:
        print("The {} Naira note in Nigeria has the image of General Murtala Mohammed".format(add))
    elif add == 50:
        print("The {} Naira note in Nigeria has the image of WaZoBia".format(add))
    elif add == 100:
        print("The {} Naira note in Nigeria has the image of Chief Obafemi Awolowo".format(add))
    elif add == 200:
        print("The {} Naira note in Nigeria has the image of Alhaji Ahmadu Bello".format(add))
    elif add == 500:
        print("The {} Naira note in Nigeria has the image of Dr Nnamdi Azikwe".format(add))
    elif add == 1000:
        print("The {} Naira note in Nigeria has the image of Alhaji Aliu Maiborno and Dr Clement Isong".format(add))
    else:
        print("The {} Naira does not has a note in Nigeria".format(add))
elif value_1 and value_2 < 0:
    print("You don't own this but owe too much monetary value of {} Naira".format(add))
else:
    print("This is a complex number")
