RC4
    - سلسلة المفتاح
    - مشتق ثنائي
    - نقطة التغير

 --- سلسلة_المفتاح ---
def rc4_stream(key, n):
    key = key.encode()
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    out = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(S[(S[i] + S[j]) % 256])
    return out


 --- مشتق_ثنائي ---
def rc4_binary_derivative(stream):
    bits = []
    for b in stream:
        for i in range(7, -1, -1):
            bits.append((b >> i) & 1)

    layers = [bits]
    curr = bits

    while len(curr) > 1:
        nxt = [(curr[i] ^ curr[i+1]) for i in range(len(curr)-1)]
        layers.append(nxt)
        curr = nxt
    
    return layers


 --- نقطة_التغير ---
def rc4_change_point(stream):
    bits = []
    for b in stream:
        for i in range(7, -1, -1):
            bits.append((b >> i) & 1)

    flips = [0] + [1 if bits[i] != bits[i-1] else 0 for i in range(1, len(bits))]
    mean = sum(flips) / len(flips)

    cusum = 0
    arr = []
    for f in flips:
        cusum += (f - mean)
        arr.append(cusum)

    idx = max(range(len(arr)), key=lambda i: abs(arr[i]))
    return idx, arr[idx]
