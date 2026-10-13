import hashlib

def calculate_hash(filename):
    with open(filename, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()

# Take input from user
content = input("Enter file content: ")

# Create file
with open("sample.txt", "w") as file:
    file.write(content)

# Generate original hash
original_hash = calculate_hash("sample.txt")

print("\nOriginal Hash:", original_hash)

# Save original hash in a separate file
with open("original_hash.txt", "w") as file:
    file.write(original_hash)

print("Original hash saved successfully.")

# Ask user if they want to modify the file
choice = input("\nDo you want to modify the file? (yes/no): ")

if choice.lower() == "yes":
    new_content = input("Enter new file content: ")

    with open("sample.txt", "w") as file:
        file.write(new_content)

# Generate current hash
current_hash = calculate_hash("sample.txt")

print("Current Hash:", current_hash)

# Compare hashes
if original_hash == current_hash:
    print("File integrity verified. File is unchanged.")
else:
    print("Warning! File has been modified.")
