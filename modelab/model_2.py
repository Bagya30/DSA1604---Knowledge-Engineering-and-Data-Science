from itertools import product
print("SMART GREENHOUSE TRUTH TABLE")
print("L E H V R1 R2 KB")
models = []
for L, E, H, V in product([False, True], repeat=4):
    R1 = (not (L and E)) or V
    R2 = (not H) or L
    KB = E and H and R1 and R2
    print(
        int(L), int(E), int(H), int(V),
        int(R1), int(R2), int(KB)
    )
    if KB:
        models.append(V)
print("\nKB entails V:", all(models))
print("KB entails NOT V:", all(not v for v in models))
