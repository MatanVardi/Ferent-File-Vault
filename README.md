
A Python-based utility that allows you to securely encrypt and decrypt files using a password-protected master key.

## How to Setup and Use

Since `Key.json` is kept private and excluded from this repository for security, you will need to generate your own master key on your first run.

### Step 1: Initialize Your Master Key
1. Run the script: `python main.py`
2. When asked *""Do you want to Sign in or create a new key?""*, type **`ck`** (Create Key).
3. Choose a strong password. This will automatically generate a local `Key.json` file encrypted with your password.

### Step 2: Encrypting or Decrypting Files
On any future run, you can now sign in using your existing key:
1. Run the script: `python main.py`
2. Type **`si`** (Sign In) and enter the password you created in Step 1.
3. Choose **`e`** to encrypt a file or **`d`** to decrypt a file.

## Requirements
This project requires the `cryptography` library. You can install it via pip:
```bash
pip install cryptography
