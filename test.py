for x in range(3):
    info = input("")
    age = [int(s) for s in info.split() if s.isdigit()]
    age = age[0]
    age = str(age)
    print(age)
    print(info.replace(age, ""))
