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

**NFS**
 * mounting file systems over a network and interact with them as though they are mounted locally, Linux-Unix based only.
 * nfs-utils package ( both on the client and the server), /etc/exports is the file where you export your nfs-shares, exportfs -r
 * no_root_squash => by default the root on the client machine is treated as user nobody, if selected then root on the client machine will have the same level of access to the files on the system as root on the server.
 * open the nfs port using firewall-cmd.
 * NFS fs is concatenated with a ':' character. => mount -t nfs 10.30.199.111:/data /mnt
 * Good practice is to mount the fs after the network is initialized with 'defaults,_netdev'
 
 **SAMBA**
 * Provides file and print services to not only Linux-Unix based clients, Windows clients could  interact with it.
 * /etc/samba/smb.conf => main configuration file
 * Validation of the above file, 'testparm'
 * passdb backeind = _tdbsam => stores user and machine account data in a "TDB"(trivial database). Using this backend does not require any additional configuration. 
 
