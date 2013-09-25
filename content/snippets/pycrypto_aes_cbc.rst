AES-CBC encryption and decryption with PyCrypto
===============================================

:date: 2013-09-25 13:15
:category: Snippets
:tags: python, code

Encryption
----------

Here is how you will encrypt data with AES-CBC. Note that using 256 bits keys is recommended. The initialization vector ("iv") does not need to be secret, but it MUST NOT be reused to encrypt something else with the same key.

The decrypting side must know *key* and *mac_key* to safely get the plaintext.

A MAC has been used to authenticate the ciphertext. This makes it easy to check if the ciphertext has been modified.

.. code-include:: python/pycrypto-aes-cbc-encrypt.py
    :lexer: python

Decryption
----------

To decrypt what we just encrypted, here is how we will proceed. First, the MAC must be verified in constant time, to prevent chosen ciphertext attacks.

Then, we decrypt the ciphertext and remove the padding to get the original text

.. code-include:: python/pycrypto-aes-cbc-decrypt.py
    :lexer: python

