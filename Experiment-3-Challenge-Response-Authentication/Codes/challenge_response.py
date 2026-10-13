import hashlib
import secrets

# Shared secret key
secret_key = "mysecret"

# Store used challenges
used_challenges = set()

# Generate a random challenge
challenge = secrets.token_hex(8)

print("Server Challenge:", challenge)

# Client generates response
response = hashlib.sha256(
    (challenge + secret_key).encode()
).hexdigest()

print("Client Response:", response)

# Server verifies response
expected_response = hashlib.sha256(
    (challenge + secret_key).encode()
).hexdigest()

if response == expected_response:
    print("Authentication Successful")

    # Check whether challenge was already used
    if challenge in used_challenges:
        print("Replay Attack Detected")
    else:
        used_challenges.add(challenge)
        print("Challenge accepted.")

else:
    print("Authentication Failed")

# Replay attack simulation
print("\nReplay Attack Simulation")

if challenge in used_challenges:
    print("Replay Attack Detected")
else:
    used_challenges.add(challenge)
    print("Response Accepted")
