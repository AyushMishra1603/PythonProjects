import CeasarCipherArt

print(CeasarCipherArt.logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z',
]
ask_user = "yes"
while ask_user == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift% 26

  def caesar(user_text, user_shift, cipher_direction):
    cypher_text = ""
    if direction == 'decode':
      user_shift *= -1
    for letter in user_text:
      if letter in alphabet:
        indexnumber = alphabet.index(letter)
        cypher_text += alphabet[indexnumber + user_shift]
      else:
        cypher_text += letter
    print(f"{cipher_direction}d text is: {cypher_text}")


  caesar(user_text=text, user_shift=shift, cipher_direction=direction)
  ask_user = input("Do you want to try again? Type 'yes' or 'no':\n")
  if ask_user == "no":
    print("Goodbye!")
