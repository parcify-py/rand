import random
sell = ['car','apple','samsung','sheep','plain','watermelon']
for i in range(10):
    person1 = random.choice(sell)
    person2 = random.choice(sell)
    if person1 == person2:
        print(f"Buy {person1} \n No.Buy a diferent {person2}")
    else:
        print(f"Buy {person1} \n No.Buy a {person2}")
