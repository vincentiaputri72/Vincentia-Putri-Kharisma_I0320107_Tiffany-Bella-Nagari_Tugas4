a = 4
b = 11
print('Nilai binary a:', format(a, '08b'))
print('Nilai binary b:', format(b, '08b'))

c = a|b
print('Keluaran operator bitwise a | b =', c, ' binary:', format(c, '08b'))

c = a>>b
print('Keluaran operator bitwise a >> b =', c, ' binary:', format(c, '08b'))

c = a^b
print('Keluaran operator bitwise a ^ b =', c, ' binary:', format(c, '08b'))

c = ~a
print('Keluaran operator bitwise ~a =', c, ' binary:', format(c, '08b'))

c = b&a
print('Keluaran operator bitwise b & a =', c, ' binary:', format(c, '08b'))
