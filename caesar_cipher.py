def shift_cipher(msg, key, action):
    new_text = "" #Empty string

    if action == "decrypt":
        key = -key  # Reverse shift for decryption change to negative

    for letter in msg: #Loop through each character
        if letter.isalpha(): #checking of alphabet characters
            base = ord('A') if letter.isupper() else ord('a') #checking for letter is in upper or lower case
            new_text += chr((ord(letter) - base + key) % 26 + base) #shift the letters
        else:
            new_text += letter  # Keep non-alphabet characters unchanged
            
    return new_text 

# Get user input from user
msg = input("Enter text: ")
key = int(input("Shift number: "))
act = input("Encrypt or Decrypt? ").strip().lower()

if act in ["encrypt", "decrypt"]:
    print("Output: " + shift_cipher(msg, key, act))
else:
    print("Invalid choice. Try again.")
