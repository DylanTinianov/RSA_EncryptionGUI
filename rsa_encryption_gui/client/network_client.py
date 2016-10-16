"""
    Receive public key
    Encrypt data
    Send secure data to network socket
"""
import socket
import os
from rsa_encryption_gui.rsa_encryption import PublicKey


def run(host_ip=raw_input('Enter Host IP Address: '), port=raw_input('Enter port number: ')):
    data_file = open(os.path.join(os.path.dirname(__file__), 'Message/Message_to_encrypt.txt'), "r")
    out = open(os.path.join(os.path.dirname(__file__), 'Message/encrypted_text.txt'), "r+")
    data = list()

    # Retrieve the data you want to encrypt

    for line in data_file:
        data.append(line.split())
    for i in range(len(data)):
        for n in range(len(data[i])):
            data[i][n] += " "

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Use the same port number as the host
    port = port
    s.connect((host_ip, port))
    print "Connected to socket"

    # Wait to receive the public key from the host
    received_key = [False, False]
    public_e = int()
    public_n = int()
    while received_key != [True, True]:
        reply = s.recv(1024)
        if reply:
            if not received_key[0]:
                public_e = int(reply)
                received_key[0] = True
            else:
                public_n = int(reply)
                received_key[1] = True

    key_public = PublicKey(public_e, public_n)
    key_public.print_key()

    # Encrypt the data
    encryption = key_public.encrypt(data)
    print "Data encryption complete"
    for i in encryption:
        out.write(str(i))
        out.write(" ")
    out.close()

    # Send the encrypted data to the host to be decrypted/ stored

    f = open(os.path.join(os.path.dirname(__file__), 'Message/encrypted_text.txt'), 'rb')
    print 'Sending...'
    encrypted_data = f.read(8192)
    s.send(encrypted_data)
    print "Encrypted file transfer complete"

    f.close()
    s.close()

if __name__ == '__main__':
    run()
