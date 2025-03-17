alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(encode_decode,original_text,shifted_amount):
    cipher_text=""
    if encode_decode=="encode":
        shifted_amount=shifted_amount
    elif encode_decode=="decode":
        shifted_amount=shifted_amount*(-1)
    else:
        print("You typed the wrong input.")
        return 
    # it stop exicuting when it find other thing insted of encode or decode   
        
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shifted_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_decode}result: {cipher_text}")

caesar(encode_decode=direction,original_text=text,shifted_amount=shift)

