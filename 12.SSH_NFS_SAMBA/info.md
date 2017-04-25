**Secure Shell** aka SSH
 * securely run a shell on a remote system.
 * SSH uses public-key cryptography ( it means that we have 2 keys, 1 private and 1 public ). Do not share your private key with anybody.

**SSH login workflow**
 * Client connects to an SSH server, before the client logs in, the server sends it a copy of its public key. This is used to
 set up the secure encryption for the communication channel and to authenticat the server to the client. SSH stores the 
 server's public key in the users ~/.ssh/known_hosts
 
 * The client sends its public key and then the server sends back a decrypted message, that could be encrypted only with the clients private key.
 
 * Once the message has been encrypted, the server lets the client in.
 
**PermitRootLogin**
 * the 'root' username exists on every Linux system, so an attacker only need to guess the password, instead of a password and username.
 * prohibit password authentication, additional layer of security after the SSH public key has been distributed. No password logins.
 * change ssh to listen on different port
