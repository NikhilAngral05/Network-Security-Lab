
import hashlib

def get_sha256(file_name):
    with open(file_name, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

text = input("Enter file content: ")

file_name = "sample.txt"

with open(file_name, "w") as f:
    f.write(text)

old_hash = get_sha256(file_name)

print("\nOriginal Hash:", old_hash)

hash_file = "original_hash.txt"

with open(hash_file, "w") as f:
    f.write(old_hash)

print("Original hash saved successfully.")

answer = input("\nDo you want to modify the file? (yes/no): ")

if answer.strip().lower() == "yes":
    updated_text = input("Enter new file content: ")

    with open(file_name, "w") as f:
        f.write(updated_text)

new_hash = get_sha256(file_name)

print("Current Hash:", new_hash)

if old_hash == new_hash:
    print("File integrity verified. File is unchanged.")
else:
    print("Warning! File has been modified.")
