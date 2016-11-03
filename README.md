<img src="https://github.com/DylanTinianov/Images/blob/master/Logo/logo_black.png"/ width="40">
# RSA Encryption (with GUI)
This Software is designed to encrypt a Client's textfile and send it over a network socket to a Host for decryption and storage

# How to use the software
Both the Host and Client must have a copy of the software
## Host
#### Port Number
Upon usage, the Host will be prompted to enter port number for the network socket

This port number, as well as the IP Address, must be provided to the Client

The Host will have their IP Address printed to the screen for self reference

For example:
```
Enter port number: 1234
```
## Client
#### IP Address and Port Number
The Client will be prompted to enter the Host's IP Address and port number

Both the IP Address and Port Number entered must match the Host's information for a connection to be established

For example:
```
Enter Host IP Address: 192.168.0.19
Enter port number: 1234   (matches the Host's port number)
```
#### Saving your data
To begin using this software to encrypt a message, the Client must save their desired data as a text file in:
```
./client/Message/Message_to_encrypt.txt
```

# How to run the software
## Host
The Host must run 'HostGUI.py'

This can be done by running the following while in the project root:
``` Bash
$ ./scripts/run_host.sh
```

The Host may now set up a network socket


<img src="https://github.com/DylanTinianov/Images/blob/master/RSA_Encryption/socket.png" width="200" height="50" />

Only after a socket is made, will generate a key pair become accessible to the host

The Host may now click 'Establish connection; send and recieve data' to wait for a Client to connect

## Client
The Client must run 'ClientGUI.py'
This can be done by running the following while in the project root:
``` bash
$ ./scripts/run_client.sh
```
The Client may then choose to encrypt and send their message to the Host to be decrypted and stored

<img src="https://github.com/DylanTinianov/Images/blob/master/RSA_Encryption/client.png" width="300" height="50" />

### Running on an IDE or Shell
Useful information relating to the encryption/ decryption processes and connection statuses will be printed to the screen for both the Host and Client
