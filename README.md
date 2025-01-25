# Caesar Cipher

A simple Python implementation of the Caesar Cipher algorithm, which allows you to encrypt and decrypt messages by shifting letters in the alphabet.

## Features

- **Encode**: Encrypt your message by shifting letters forward in the alphabet.
- **Decode**: Decrypt your message by shifting letters backward.
- **Supports non-alphabet characters**: Any non-alphabet characters (like spaces or punctuation) are retained as they are.

## How It Works

The Caesar cipher shifts the letters in the alphabet by a given number (shift). When encoding, each letter in the input text is shifted forward by the specified number. When decoding, the letters are shifted backward by the same number.

## Usage

1. Run the program.
2. Type `encode` to encrypt a message or `decode` to decrypt one.
3. Enter the message you'd like to encode or decode.
4. Provide the shift value (e.g., 3).
5. The program will output the encrypted or decrypted text.

## Example

### Example 1: Encoding

Type 'encode' to encrypt, type 'decode' to decrypt: encode Type your message: hello world Type the shift number: 3 Here's your encrypted text: khoor zruog

shell
Copy
Edit

### Example 2: Decoding

Type 'encode' to encrypt, type 'decode' to decrypt: decode Type your message: khoor zruog Type the shift number: 3 Here's the decoded text: hello world

bash
Copy
Edit

## Installation

Clone this repository to your local machine:

git clone https://github.com/AvneeshYadav/caesar-cipher.git

arduino
Copy
Edit

Then, run the script with Python:

python caesar_cipher.py
