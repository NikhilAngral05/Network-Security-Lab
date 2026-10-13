# Experiment 4: Generate, Inspect and Verify a Self-Signed X.509 Digital Certificate Using OpenSSL

## Aim

To create a self-signed X.509 digital certificate, examine its information, and verify it using OpenSSL.

## Theory

An X.509 certificate contains information about an entity and its public key. A self-signed certificate is created and signed using its own private key and is commonly used for testing and local development.

## Methodology

OpenSSL is used in Kali Linux to generate an RSA private key and create a self-signed certificate. The certificate is then examined, verified, and its SHA-256 fingerprint is obtained. A Subject Alternative Name is also added for localhost and 127.0.0.1.

## Procedure

1. Check the installed OpenSSL version.
2. Generate a 2048-bit RSA private key.
3. Create a self-signed X.509 certificate.
4. Add localhost and 127.0.0.1 as Subject Alternative Names.
5. Inspect the certificate information.
6. Verify the generated certificate.
7. Generate its SHA-256 fingerprint.
8. Save the generated information as output files.

## Result

A self-signed X.509 certificate was successfully generated, inspected and verified using OpenSSL. The SHA-256 fingerprint and Subject Alternative Name were also obtained successfully.

## Discussion

The experiment demonstrated the basic use of OpenSSL for creating and examining digital certificates. The certificate contains information such as the issuer, subject, validity period, public key and certificate extensions.

## Improvement

Added a Subject Alternative Name for `localhost` and `127.0.0.1` to make the certificate suitable for local testing.

## Conclusion

The experiment successfully demonstrated the generation, inspection and verification of a self-signed X.509 certificate using OpenSSL in Kali Linux.
