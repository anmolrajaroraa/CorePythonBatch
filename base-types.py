'''
Base Types (immutables)

integer, float, boolean, string, bytes

int -> 783, 0, -192, 0b010 (binary), 0o642 (octal), 0xF3 (hexadecimal)

float -> 9.23, 0.0, -1.7e-6 = -1.7 x 10⁻⁶ = -0.0000017
-1.7e+6 = -1.7 x 10⁶ = -1700000.0

bool -> True, False

str -> "One\nTwo", 'I\'m'
print("""X\tY\tZ
1\t2\t3""")

bytes -> b"toto\xfe\775"
file1 = open("img.png", "rb")
print(file1.read())
'''
