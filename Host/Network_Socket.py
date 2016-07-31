"""
    Send the Public Key to the Client.
    Receive encrypted data.
    Decrypt and save data.
"""
import socket
import os
from RSA_EncryptionGUI.RSA_Encrpytion import PrivateKeyGen
out_decrypt = open(os.path.join(os.path.dirname(__file__), 'decrypted_text.txt'), "w")
key_private = None
s = None


def create_socket():
    global s
    # Get the local IP over LAN.
    host = socket.gethostbyname(socket.gethostname())

    print "Host IP:", host
    port = 1234  # Use port number that's not in use.

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print "Socket Created"
    s.bind((host, port))
    s.listen(0)  # Don't allow for any queued connections; only 1 at a time


def key_gen():
    global key_private
    # Create public/ private key pair for crypto-system
    print "Generating key pair..."
    key_private = PrivateKeyGen()
    while not key_private.public_exponent():
        key_private = PrivateKeyGen()
        key_private.public_exponent()

    key_private.private_exponent()
    print key_private.e, key_private.n


def send_receive_data():
    global out_decrypt, key_private, s
    # Send the public key information to the client
    print "Waiting for incoming connection..."
    data_received = False
    while not data_received:
        connection, addr = s.accept()
        print "Connection Established"
        connection.send(str(key_private.e))
        connection.send(str(key_private.n))
        # Wait to receive data from the client
        while True:
            data = connection.recv(8192)
            if not data:
                break
            data_received = True
            break

    data = data.split()
    print "Data decryption in progress..."
    # Decrypt data using the private key
    decryption = key_private.decrypt(data)
    print "Data decryption complete. Secure file transfer successful"

    # Save data
    for i in decryption:
        out_decrypt.write(i)

    out_decrypt.close()
    s.close()

if __name__ == '__main__':
    create_socket()
    key_gen()
    send_receive_data()
