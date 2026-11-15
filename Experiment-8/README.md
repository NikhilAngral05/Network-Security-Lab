# Experiment 8: OpenPGP Secure Email

## Aim

Create and exchange OpenPGP keys, verify a recipient's public-key fingerprint, and send an encrypted, digitally signed email using Thunderbird.

## Requirements

- Mozilla Thunderbird with OpenPGP support
- Two test email accounts or a second participant
- A trusted, separate way to compare key fingerprints

## Background

OpenPGP uses a public/private key pair. Keep the private key secret; share the public key with correspondents. A sender can encrypt a message with the recipient's public key, and the recipient decrypts it with their private key. A sender can also sign a message with their private key so the recipient can check the signature using the sender's public key.

## Procedure

1. Configure a test email account in Thunderbird and open its account security settings.
2. Create an OpenPGP key pair for the account. Protect the private key and do not send or publish it.
3. Export or attach the public key and exchange it with the other participant.
4. Import the received public key. Compare its fingerprint with the key owner's fingerprint using a trusted channel separate from the email exchange.
5. Compose a test message to the participant. Enable both encryption and digital signing in the message's security options, then send it.
6. On the receiving account, open the message. Confirm that Thunderbird decrypts it and reports a valid signature. If the key is missing or the signature is untrusted, verify the key exchange and fingerprint before relying on the message.

Menu names can vary by Thunderbird version. Use test accounts and non-sensitive sample text for the exercise.

## Result

The exercise demonstrates public-key exchange and fingerprint verification, followed by encrypted email delivery and digital-signature verification.

## Security Notes

- Never share a private key.
- Verify public-key fingerprints through a trusted, independent channel before using a key.
- Do not treat an unverified key or invalid signature as proof of identity.
- Redact account addresses and message details from any screenshots.

## Reference

Exercise topic: [4316sushil39/Network-Security-Lab, Exp-8](https://github.com/4316sushil39/Network-Security-Lab/tree/main/Exp-8)
