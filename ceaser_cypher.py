from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rerun = "yes"

#Function called ceaser() function to encode or decode the text
def ceaser(original_text, shift_amount, direction):
    if direction == "encode":
        encrypted_text = ""
        for letter in original_text:
            if letter in alphabet:
                index_of_letter = alphabet.index(letter)
                new_index = (index_of_letter + shift_amount) % 26
                encrypted_text += alphabet[new_index]
            else:
                encrypted_text += letter
        print(f"Here's your encrypted text:{encrypted_text}")
    
    elif direction == "decode":
        decoded_text = ""
        for letter in original_text:
            if letter in alphabet:
                index_of_letter = alphabet.index(letter)
                new_index = (index_of_letter - shift_amount) % 26
                decoded_text += alphabet[new_index]
            else:
                decoded_text += letter
        print(f"Here's the decoded text: {decoded_text}")
    else:
        print("Please select either 'encode' or 'decode'")

while rerun == "yes":
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(original_text = text, shift_amount = shift, direction = encode_or_decode)
    rerun = (input("Do you want to go again?(type in 'yes' if you do and 'no' id you don't):")).lower()
    if rerun == "no":
        print("****************************************************[({Goodbye Comrade})]****************************************************")