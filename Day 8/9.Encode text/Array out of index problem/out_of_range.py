alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code? 


def encrypt(original_text,shift_amount):
    cipher_text= ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position=shifted_position % len(alphabet)
        # we know len(alphabate) = 26
        # alphabet.index("z") = 25
        # if shifted ammount = 4
        # shifted_position = 25 + 4 = 29
        # shifted_position = 29 % 26 = 3
        # alphabet[3] = d
        # Z becomes d

        cipher_text+=alphabet[shifted_position]
    print(f"Here is the encoded result {cipher_text}")



encrypt(original_text=text,shift_amount=shift)



