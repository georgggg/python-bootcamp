alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet_length = len(alphabet)

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction):
    shifted_string = ""
    if direction == "encode" or direction == "decode":
        if direction == "decode":
            shift = shift * -1
        for letter in text:
            char_position = alphabet.index(letter)
            new_position = (char_position + shift) % (alphabet_length)
            shifted_string += alphabet[new_position]
         
        print(f"The {direction}d string is {shifted_string}")
    else:
        print("You entered an invalid value other than 'encode' or 'decode'. Please try again.")
        
caesar(text, shift, direction)