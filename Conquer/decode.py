
def DeROL(bits, N):
    for _ in range(N):
        bits = (bits >> 1)|(((bits << (length -1)) & (2**length - 1)) & ~((2**length - 2) << (length - 1)))
    return bits

key = 364765105385226228888267246885507128079813677318333502635464281930855331056070734926401965510936356014326979260977790597194503012948
cipher = 92499232109251162138344223189844914420326826743556872876639400853892198641955596900058352490329330224967987380962193017044830636379
# key = 260207627290566165245289
# cipher = 548615360791046550492340
length = len(bin(key)) -1

print(cipher, length)

# print(len(bin(cipher)) -2, len(bin(key)) -2)
cipher ^= key
# print(cipher)

for _ in range(32):
    key = DeROL(key, pow(cipher, 3, length))
    cipher ^= key
    # print(cipher)


print("flag = ", hex(cipher))
print("flag = ", bytearray.fromhex(hex(cipher)[2:]).decode())

# 28b4b0025efd055591810aa050c6b93a1f2254a876061620cd4b0f437aec64ad5866e3b70baa709088865d90582b7a4b24e6676be80b0f
# print(bin(4 >> 1  | ((4 << 2)& ~((2**3 - 2) << 2))))/