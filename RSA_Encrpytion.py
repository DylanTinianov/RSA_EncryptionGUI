import Used_Functions
import Prime_Generator


class PrivateKeyGen:
    """
        Class contains methods public_exponent, private_exponent, and decrypt. The initiation method creates
        primes p and q and calculates the value of 'n' and its phi function. Public_exponent method calculates a secure
        public exponent (e) value to encrypt the messages with; check if any secure values for e work with n % e
        and phi(n) % e. The private_exponent method calculates the private exponent value (d) through using a modulo
        inverse function. The decrypt method decrypts the previously encrypted message using the private key.
    """
    def __init__(self):
        prime_bit_length = 512  # Prime lengths for a 1024 bit key
        self.p = Prime_Generator.generate_large_prime(prime_bit_length)     # F'kn huge prime numbers
        self.q = Prime_Generator.generate_large_prime(prime_bit_length)
        while self.p == "Failed":   # In case there is a failed attempt
            self.p = Prime_Generator.generate_large_prime(prime_bit_length)
        while self.q == "Failed":
            self.p = Prime_Generator.generate_large_prime(prime_bit_length)

        self.n = self.p * self.q
        self.phi_func = (self.p-1) * (self.q-1)
        self.e = int()
        self.d = int()

    def public_exponent(self):
        secure_e_values = [3, 5, 17, 257, 65537]    # Officially secure e values
        for i in secure_e_values:
            if self.n % i != 0 and self.phi_func % i != 0:
                self.e = i
                return True

        return False

    def private_exponent(self):
        self.d = Used_Functions.modInv(self.e, self.phi_func)

    def decrypt(self, encrypted_message):
        decrypted_text = list()

        for letter in encrypted_message:
            try:
                decrypted_text.append(chr(pow(long(letter), self.d, self.n)))
            except (OverflowError, ValueError):  # Ignore any errors
                pass

        for i in range(2):  # pop out the additional space and new line added at the end of the data
            decrypted_text.pop(len(decrypted_text)-1)

        return decrypted_text


class PublicKey:
    """
        Class contains methods print_key and encrypt. The initiation sets the public exponent (e) and the value of
        multiplied primes (n); p*q. The print_key method prints the public exponent and n value. The encrypt method
        reads through a plain text file, and encrypts the data with the public key using: ((a^e) % n), where a is
        a numerical value based off each character in the data.
    """
    def __init__(self, e, n):
        self.e = e
        self.n = n

    def print_key(self):
        print "Public Key:", self.e, self.n
        return self.e, self.n

    def encrypt(self, message):
        plain_text = list()
        number_text = list()
        number_text_encrypted = list()

        for line in message:
            for word in line:
                for letter in word:
                    plain_text.append(letter)
            plain_text.append("\n")

        for character in plain_text:
            number = ord(character)
            number_text.append(number)

        for num in number_text:
            number_text_encrypted.append(pow(num, self.e, self.n))

        return number_text_encrypted
