from ecdsa.numbertheory import inverse_mod
from ecdsa.ecdsa import generator_secp256k1

# Dane z transakcji
r1 = int("fbc2b9a148f7c136fd5ab60d9a1317624d90630ccdf1b65562977f370d999841", 16)
r2 = int("8ca2698b53fffcf9d064b1ca1313ff08e08e47d3bbb97a4f9d54dd0e3164af9a", 16)
s1 = int("3f598a19e8e4eefec27af6fb8765132b205f45445d4b3755235d232d6f2ee41c", 16)
s2 = int("65913d2b007ebedf451e0068b368a33ff0fdb9725370a8cecc34e2e8449f143c", 16)
z1 = int("726c33406e9d8ac5824b9ab64a252c27146c26907b23eb082ac72b324c2e1167", 16)
z2 = int("c7c58a952ca7b31ced67bfea57fd7571314f8d77a88c90f42e68bdd82c2adb4f", 16)

# Moduł porządkowy krzywej secp256k1
n = generator_secp256k1.order()

# Różnice
delta_s = (s1 - s2) % n
delta_z = (z1 - z2) % n

# Obliczanie k – tylko jeśli delta_s ≠ 0
if delta_s != 0:
    k = (delta_z * inverse_mod(delta_s, n)) % n
    print(f"✅ Wykryto liniową zależność k! k = {hex(k)}")

    # Teraz obliczamy prywatny klucz d na podstawie wzoru:
    # s = (z + r*d)/k  =>  d = (s*k - z) / r
    d = ((s1 * k - z1) * inverse_mod(r1, n)) % n
    print(f"🔑 Odzyskany klucz prywatny: d = {hex(d)}")
else:
    print("❌ Brak zależności liniowej w k – delta_s = 0")
