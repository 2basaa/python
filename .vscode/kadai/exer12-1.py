def resistance(r1, r2):
    r0 = (r1 * r2) / (r1 + r2)
    return r0

r1 = float(input('R1 = '))
r2 = float(input('R2 = '))
r0 = resistance(r1, r2)
print('合成抵抗の値:', str(r0))