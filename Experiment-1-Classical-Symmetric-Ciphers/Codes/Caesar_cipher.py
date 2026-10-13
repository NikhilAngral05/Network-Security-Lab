def caesar_encrypt(message: str, key: int) -> str:

    output = []
    for letter in message:
        if letter.isalpha():
            start = ord('A') if letter.isupper() else ord('a')
            position = (ord(letter) - start + key) % 26
            output.append(chr(position + start))
        else:
            output.append(letter)

    return "".join(output)

message = input()
key = int(input())

print(caesar_encrypt(message, key))

