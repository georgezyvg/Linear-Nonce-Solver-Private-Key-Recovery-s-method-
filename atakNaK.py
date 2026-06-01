from ecdsa.numbertheory import inverse_mod
from ecdsa.ecdsa import generator_secp256k1

# Dane z transakcji
r1 = int("ced8474e7cbb2c9ade8b4a6474c3fa8ea4036718d844f3105dde155a6583a134", 16)
r2 = int("ceda0e7cfe7e6da20b3e1b08877e722eceba96574f50b78c8b03618e4c6ce18c", 16)
s1 = int("1c9e070de661d5913d457c6f075641ec28c8c8f4fe336070710787e471ebd558", 16)
s2 = int("034a6987bc4e6cfac6a8a5ed767ccbbf47cfb15323b3ebb44f3e72ee6148e255", 16)
z1 = int("beb21d89f2ebdc645094135d999aa79d386711a6a5f0289eba893c5515a4856f", 16)
z2 = int("beb21d89f2ebdc645094135d999aa79d386711a6a5f0289eba893c5515a4856f", 16)

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
