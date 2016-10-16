# RSA_EncruptionkGUI
This Software is designed to encrypt a Client's textfile and send it over a network socket to a Host for decrpytion and storage. It contains a Client/ Host GUI, and is an implementation of an RSA crypto-system on textfiles over a network socket.

# Usage
### Before Use
#### IP Address
Before usage, the desired Client must change the top line of code within the 'Network_Client.py'

``` Python
HOST_IP = "ENTER HOST IP HERE" # Ex:  192.168.0.19
```

#### Saving your text
To begin using this software to encrypt a message, save your desired text in:
```
./Client/Message/Message_to_encrypt.txt
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
Useful information relating to the encryption/ decryption processes and connection statuses will be printed to the screen for both the Host and Client. The Host's IP address will also be printed for self reference.

#### Disclaimer
This Software is not to be used for any important secure data transfers, or to be held responsible for any lack of security. This Software does not claim to be 100% secure, and was merely made for fun.


[socket]: https://github.com/DylanTinianov/Images/blob/master/RSA_Encryption/socket.png
[key_gen]: https://github.com/DylanTinianov/Images/blob/master/RSA_Encryption/key_gen.png
[client]: https://github.com/DylanTinianov/Images/blob/master/RSA_Encryption/client.png
