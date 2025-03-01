A = {"a", "b", "c", "d", "f", "g"}
B = {"b", "c", "h", "l", "m", "o"}
C = {"c", "d", "f", "h", "i", "j", "k"}

print("a. Number of elements in Set A and Set B:", len(A | B))
print("b. Number of elements in Set B that is not part of Set A and Set C:", len(B - (A | C)))
print("i.", ((C & B) - A) | C - (B | A))
print("ii.", A & C)
print("iii.", ((A & B) - C) | (C & B))
print("iv.", (A & C) - B)
print("v.", A & B & C)
print("vi.", B - (A | C))