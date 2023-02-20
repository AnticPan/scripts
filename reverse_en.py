import sys

if __name__ == "__main__":
    inp = sys.argv[1]
    reverse=['⇂', 'ᄅ', 'Ɛ', 'ᔭ', 'ಽ', '9', 'ㄥ', '8', '6', '0', 'ɐ', 'q', 'ɔ', 'p', 'ǝ', 'ɟ', 'ƃ', 'ɥ', 'ı̣', 'ɾ̣', 'ʞ', 'ן', 'ɯ', 'u', 'o', 'd', 'b', 'ɹ', 's', 'ʇ', 'n', 'ʌ', 'ʍ', 'x', 'ʎ', 'z', 'Ɐ', 'ꓭ', 'Ɔ', 'ꓷ', 'Ǝ', 'Ⅎ', 'ꓨ', 'H', 'I', 'ſ', 'ꓘ', 'ꓶ', 'W', 'N', 'O', 'Ԁ', 'Ò', 'ꓤ', 'S', 'ꓕ', 'ꓵ', 'ꓥ', 'M', 'X', '⅄', 'Z']
    normal=list("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    mapper = {n:r for n,r in zip(normal, reverse)}
    out = "".join(mapper[c] if c in mapper else c for c in inp)
    print(out[::-1])
