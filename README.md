# FABEO: Fast Attribute-based Encryption with Optimal Security
 
This is the code repository accompanying our CCS '22 paper "FABEO: Fast Attribute-based Encryption with Optimal Security" by Doreen Riepel and Hoeteck Wee.


> Attribute-based encryption (ABE) enables fine-grained access control on encrypted data and has a large number of practical applications. This paper presents FABEO: fasterpairing-based ciphertext-policy and key-policy ABE schemes that support expressive policies and put no restriction on policy type or attributes, and the first to achieve optimal, adaptive security with multiple challenge ciphertexts. 


## Quick Install & Test

The schemes have been tested with Charm 0.50 and Python 3.9.17 on Ubuntu 22.04. (Note that Charm may not compile on newer Linux systems due to the incompatibility of OpenSSL versions 1.0 and 1.1.).

## Manual Installation

Once you have Charm, run
```sh
make && pip install . && python samples/run_cp_schemes.py
```