PLAYFAIR CIPHER
 - معالجة النص
 - مصفوفة المفتاح

 --- معالجة_النص ---
def playfair_preprocess(text):
    text = "".join([c for c in text.upper() if c.isalpha()]).replace("J", "I")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                pairs.append((a, "X"))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        else:
            pairs.append((a, "X"))
            i += 1
    return pairs


  --- مصفوفة_المفتاح ---
def playfair_matrix(key):
    key = "".join([c for c in key.upper() if c.isalpha()]).replace("J", "I")
    letters = []
    for c in key:
        if c not in letters:
            letters.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in letters:
            letters.append(c)
    return [letters[i*5:(i+1)*5] for i in range(5)]
