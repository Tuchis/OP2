from polynomial import Polynomial

poly1 = Polynomial()
poly2 = Polynomial()

data_file = open("data1.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly1.append_term(float(degree), float(coefficient))

data_file = open("data2.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly2.append_term(float(degree), float(coefficient))

#print(poly1)
#print(poly2)


print(poly1.degree())
print(poly2.degree())

print(poly1[2.0])
print(poly1)
print(poly2)

# print("Addition:")
# new_p = poly1 + poly2
# print(new_p[3.0], new_p[2.0],new_p[1.0],new_p[0.0])
#
# print("Substraction:")
# new_p = poly1 - poly2
# print(new_p[3.0], new_p[2.0],new_p[1.0],new_p[0.0])
# print(new_p)

print("Multiplication:")
new_p = poly1 * poly2
print(new_p[3.0], new_p[2.0],new_p[1.0],new_p[0.0])
print(new_p)
print(new_p.evaluate(2))

