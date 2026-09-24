Experiment 3: Challenge-Response Authentication and Replay Attack Handling
Aim
To implement challenge-response authentication using a random nonce and shared secret, and detect replay attacks.

Methodology
The server generates a random nonce as a challenge. The client uses the nonce and shared secret to create an HMAC-SHA256 response. The server verifies the response and rejects reused or expired challenges.

Procedure
Set a shared secret between the client and server.
Generate a random nonce as the authentication challenge.
Generate an HMAC-SHA256 response using the nonce and secret.
Verify the response on the server.
Reuse the same response to simulate a replay attack.
Use nonce tracking and timestamps to reject replayed or expired responses.
Tools and Techniques
Python 3
VS Code
HMAC-SHA256
secrets
time
Nonce generation
Replay detection
Result
The initial authentication was successful, while replayed and expired responses were rejected.

Discussion
A fresh nonce prevents an old authentication response from being reused. Timestamp checking provides additional protection against delayed replay attempts.

Improvement
One-time nonce tracking was added to detect and prevent reuse of an old challenge.

Conclusion
The experiment successfully demonstrated challenge-response authentication and protection against replay attacks.
