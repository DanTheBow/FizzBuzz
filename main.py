# FizzBuzz:
# Hier werden die Zahlen von 1 bis 100 in der Konsole ausgegeben.
# Ist die Zahl durch 3 teilbar, wird "Fizz" statt der Zahl ausgegeben.
# Ist die Zahl durch 5 teilbar, wird "Buzz" statt der Zahl ausgegeben.
# Ist die Zahl durch 3 und 5 teilbar, wird "FizzBuzz" statt der Zahl ausgegeben.


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:  # Alternativ: if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
