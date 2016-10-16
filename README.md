# RSA Encryption (with GUI)
This Software is designed to encrypt a Client's textfile and send it over a network socket to a Host for decryption and storage

# Usage
#### Saving your data
To begin using this software to encrypt a message, save your desired data as a text file in:
```
./client/Message/Message_to_encrypt.txt
```
#### IP Address
Upon usage, the Client will be prompted to enter the Host's IP Address

The Host will have their IP Address printed to the screen for self reference

For example:
```
Enter Host IP Address: 192.168.0.19
```

### Host
The Host must run 'HostGUI.py'

This can be done by running the following while in the project root:
``` bash
$ ./scripts/run_host.sh
```

The Host may now set up a network socket

![alt text][socket]

Only after a socket is made, may a host generate a key pair for encryption

![alt text][key_gen]

The Host may now click 'Establish connection; send and recieve data' to wait for a Client to connect

### Client
The Client must run 'ClientGUI.py'
This can be done by running the following while in the project root:
``` bash
$ ./scripts/run_client.sh
```
The Client may then choose to encrypt and send their message to the Host to be decrypted and stored

![alt text][client]

### Running on an IDE or Shell
Useful information relating to the encryption/ decryption processes and connection statuses will be printed to the screen for both the Host and Client


[socket]: https://github.com/DylanTinianov/Images/blob/master/RSA_Encryption/socket.png
[key_gen]: https://github.com/DylanTinianov/Images/blob/master/RSA_Encryption/key_gen.png
[client]: https://github.com/DylanTinianov/Images/blob/master/RSA_Encryption/client.png
