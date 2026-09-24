import hashlib
import secrets

# Shared secret
shared_key = "mysecret"

# Set to store previously used challenges
used_challenges = set()

# Create a random challenge
server_challenge = secrets.token_hex(8)

print("Server Challenge:", server_challenge)

# Client creates authentication response
client_response = hashlib.sha256(
    (server_challenge + shared_key).encode()
).hexdigest()

print("Client Response:", client_response)

# Server creates expected response
server_response = hashlib.sha256(
    (server_challenge + shared_key).encode()
).hexdigest()

# Verify authentication
if client_response == server_response:
    print("Authentication Successful")

    # Check if challenge was already used
    if server_challenge in used_challenges:
        print("Replay Attack Detected")
    else:
        used_challenges.add(server_challenge)
        print("Challenge accepted.")

else:
    print("Authentication Failed")

# Replay attack test
print("\nReplay Attack Simulation")

if server_challenge in used_challenges:
    print("Replay Attack Detected")
else:
    used_challenges.add(server_challenge)
    print("Response Accepted")
