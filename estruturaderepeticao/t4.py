a = 80000
b = 200000
anos = 0

while a <= b:
    a *= 1.03
    b *= 1.015
    anos += 1

print(f"Em {anos} anos o país A iguala ou supera o país B.")
