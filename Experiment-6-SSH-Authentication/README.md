# Experiment 6: Password Authentication and SSH Security

## Aim
To demonstrate remote system access through SSH using password-based and public-key authentication methods.

## Theory

- **SSH (Secure Shell):** A protocol that provides encrypted communication between two systems over a network.
- **Password Authentication:** Allows access after the server verifies the supplied username and password.
- **Public-Key Authentication:** Uses a private key on the client and a corresponding public key on the server to verify the client.
- **Port 22:** The default TCP port used by SSH.
- **Authorized Keys:** The file `~/.ssh/authorized_keys` stores public keys permitted to authenticate to a user account.

## Tools Required

- Kali Linux
- Windows PowerShell or another SSH client
- OpenSSH server and client
- Two reachable systems or virtual machines

## Procedure

### Step 1: Prepare the SSH Server

Install the OpenSSH server on the server machine if required, then start the SSH service.

```bash
sudo apt update
sudo apt install openssh-server
sudo systemctl enable --now ssh
```

### Step 2: Test Password Authentication

From the client machine, connect using the server's username and IP address.

```bash
ssh username@server_ip
```

Enter the account password when prompted and verify whether the connection succeeds.

### Step 3: Generate an SSH Key Pair

On the client, generate an RSA key pair.

```bash
ssh-keygen -t rsa -b 4096
```

The command creates a private key and a corresponding public key.

### Step 4: Install the Public Key

Copy the public key to the server and add it to the target user's authorized keys file. For example, if the public key is transferred manually:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
cat id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

Run the file commands for the **target user's account on the server**. Transfer the public key securely from the client first.

### Step 5: Verify Key-Based Login

From the client, reconnect to the server:

```bash
ssh -i id_rsa username@server_ip
```

Verify that authentication succeeds using the private key. A passphrase may still be requested if one was configured for the key.

### Step 6: Test Authentication Failure

Attempt a login with an incorrect password or an unapproved key in the authorized lab environment. Record the authentication failure and compare it with the successful connection.

## Visualization

```text
      ┌───────────────────────┐
      │ SSH Client             │
      └───────────┬───────────┘
                  │
                  ▼
      ┌───────────────────────┐
      │ Connect to Server     │
      │ TCP Port 22           │
      └───────────┬───────────┘
                  │
                  ▼
      ┌───────────────────────┐
      │ Choose Authentication │
      └───────────┬───────────┘
                  │
           ┌──────┴──────┐
           ▼             ▼
   ┌──────────────┐ ┌──────────────┐
   │ Password     │ │ SSH Key      │
   │ Verification │ │ Verification │
   └──────┬───────┘ └──────┬───────┘
          │                │
          └───────┬────────┘
                  ▼
      ┌───────────────────────┐
      │ Authentication Check  │
      └───────────┬───────────┘
                  │
             ┌────┴────┐
             ▼         ▼
      ┌───────────┐ ┌───────────┐
      │ Accepted  │ │ Rejected  │
      │ Access    │ │ No Access │
      └───────────┘ └───────────┘
```

## Results

1. Password-based SSH authentication was tested.
2. An SSH key pair was generated and public-key authentication was configured.
3. Successful and unsuccessful login attempts were compared.

## Discussion

SSH encrypts remote login traffic, while public-key authentication reduces dependence on passwords. Proper permissions on SSH key files help prevent unauthorized use.

## Improvement

Security can be strengthened by disabling password login after verifying key-based access, restricting SSH access, and monitoring failed login attempts.

## Conclusion

The experiment demonstrated how SSH provides encrypted remote access and how password-based and public-key authentication can be used to verify users.
