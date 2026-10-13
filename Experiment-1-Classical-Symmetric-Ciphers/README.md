# Experiment 1: Implement and Analyze Classical Symmetric Cipher

## Aim

To implement and understand the working of the Caesar Cipher and Vigenère Cipher symmetric encryption algorithms used for encryption and decryption.

## Methodology

### 1. Caesar Cipher

1. Take the plaintext and a numerical key as input.
2. Shift each alphabetic character according to the given key.
3. Use modulo 26 to handle the wrapping of alphabets.
4. During decryption, shift the characters backward using the same key.
5. Verify that the decrypted text matches the original plaintext.

### Example

- **Plaintext:** HELLO
- **Key:** 3
- **Encryption:** KHOOR

---

### 2. Vigenère Cipher

1. Take the plaintext and an alphabetic keyword as input.
2. Repeat the keyword until it matches the length of the plaintext.
3. Convert the letters into numerical values where A = 0 and Z = 25.
4. Add the plaintext and key values and apply modulo 26 for encryption.
5. Use the same key to perform the decryption.

### Example

- **Plaintext:** HELLO
- **Key:** KEY

**Encryption:**

```text
Plaintext : H E L L O
Key       : K E Y K E
Ciphertext: R I J V S
```

## Result

The Caesar Cipher and Vigenère Cipher were successfully implemented. The encryption and decryption processes were tested using user-provided text and keys, and the original message was correctly recovered after decryption.

## Discussion

The Caesar Cipher uses a fixed shift value to encrypt each character, making it simple and easy to understand. However, it provides limited security because the possible shift values are small and can be easily tested.

The Vigenère Cipher uses a keyword to apply different shifts to the characters of the plaintext. This makes it more secure than the Caesar Cipher and reduces the effectiveness of simple frequency analysis.

Both algorithms demonstrate the basic working principle of symmetric encryption, where a key is used to encrypt and decrypt the message.

## Improvement – Caesar Cipher

Made the program accept the plaintext and shift value from the user.

## Improvement – Vigenère Cipher

Made the program accept the text and key from the user and support encryption and decryption.

## Conclusion

Both ciphers were successfully implemented and tested for secure encryption and decryption of messages.
