alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encrypt_caesar(text,offest):
    new_text = ""
    global alpha
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            if len(alpha) > alpha.index(letter) + offest:
                new_text += alpha[alpha.index(letter) + offest]
            else:
                new_text += alpha[alpha.index(letter) + offest - len(alpha)]
        else:
            new_text += letter
    return new_text


def decrypt_caesar(text,offest):
    new_text = ""
    global alpha
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            new_text += alpha[alpha.index(letter) - offest]
        else:
            new_text += letter
    return new_text

def cipher_fence_rail(text):
    split_text = text.split(" ")
    new_text = ""
    for word in split_text:
        new_text += word
    even_letters = ""
    odd_letters =""
    for letters in new_text:
        if new_text.index(letters) % 2 == 0:
            even_letters += letters
        else:
            odd_letters += letters
    return even_letters+odd_letters

def decrypt_cipher_fence_rail(text):
    half_text = len(text) // 2
    even_letters = text[:half_text+1]
    odd_letters = text[half_text+1:]
    decrypt_text = ""
    for i in range(half_text + 1):
        if len(even_letters)-1 >= i:
            decrypt_text += even_letters[i]
            print(decrypt_text)
        if len(odd_letters)-1 >= i:
            decrypt_text += odd_letters[i]
            print(decrypt_text)
    return decrypt_text

