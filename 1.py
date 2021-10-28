def cel2fah(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit;

celsius = 0;

for i in range(celsius, 51, 10):
    print(i)
    print(cel2fah(i))

