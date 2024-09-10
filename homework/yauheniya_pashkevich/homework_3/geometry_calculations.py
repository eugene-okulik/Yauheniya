cathetus1 = float(input('Please give the length of the 1st cathetus of a right triangle: '))
cathetus2 = float(input('Please give the length of the 2nd cathetus of a right triangle: '))

hypotenuse = (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
area = 0.5 * cathetus1 * cathetus2

print(f'Hypotenuse = {hypotenuse}')
print(f'Triangle area = {area}')