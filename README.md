# Caesar Cipher Encryption and Decryption in Python

## Description
This project demonstrates a basic Caesar cipher, a simple text encryption technique.
It is for educational purposes only and is not secure for real-world use.

## How It Works
- The program shifts alphabetic characters forward (encryption) or backward (decryption) by a user-specified number.
- Uppercase and lowercase letters are preserved.
- Non-letter characters (spaces, punctuation) remain unchanged.
- Decryption is handled by reversing the shift.

## Testing Examples
- Encrypt "abcd" with shift 3 → Output: "defg"
- Decrypt "defg" with shift 3 → Output: "abcd"
- Encrypt "Hello, World!" with shift 5 → Output: "Mjqqt, Btwqi!"

## Security Note
The Caesar cipher is outdated and vulnerable to brute force attacks.  
This project is a learning tool for understanding encryption basics.

## User Guide
1. Run `caesar_cipher.py` in VS Code or terminal.
2. Input your message.
3. Input the shift value.
4. Type 'encrypt' or 'decrypt'.
5. View the result printed on the screen.

