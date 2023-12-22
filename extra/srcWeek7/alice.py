from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives import hashes
import socket

def read_keys():
    with open('pw', 'rb') as file:
        encryption_key = file.read(16)  # Read 128-bit encryption key
        auth_key = file.read(32)  # Read 256-bit authentication key
    return encryption_key, auth_key

def aes_ctr_encrypt(message, key):
    cipher = Cipher(algorithms.AES(key), modes.CTR(b'\x00' * 16), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    return ciphertext

def aes_ctr_decrypt(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.CTR(b'\x00' * 16), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext


def generate_hmac(message, auth_key):
    h = hmac.HMAC(auth_key, hashes.SHA256(), backend=default_backend())
    h.update(message)
    return h.finalize()

def verify_hmac(message, received_hmac, auth_key):
    h = hmac.HMAC(auth_key, hashes.SHA256(), backend=default_backend())
    h.update(message)
    try:
        h.verify(received_hmac)
        return True  # Message authentication successful
    except InvalidSignature:
        return False  # Message authentication failed


if __name__ == "__main__":
    encryption_key, auth_key = read_keys()
    # Estabelecer conexão com Bob
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))  # Exemplo de endereço e porta
        
        while True:
            # Alice lê a entrada do usuário
            message_to_send = input("Alice: ")
            
            # Criptografar a mensagem
            ciphertext = aes_ctr_encrypt(message_to_send.encode(), encryption_key)
            hmac = generate_hmac(ciphertext, auth_key)
            
            # Enviar mensagem para Bob
            s.sendall(ciphertext + hmac)
            
            # Bob recebe a resposta de Alice
            received_data = s.recv(1024)
            received_ciphertext = received_data[:-32]  # Assume que os últimos 32 bytes são o HMAC
            received_hmac = received_data[-32:]  # Últimos 32 bytes são o HMAC
            
            # Verificar o HMAC
            if verify_hmac(received_ciphertext, received_hmac, auth_key):
                # Se o HMAC estiver correto, descriptografar a mensagem
                decrypted_message = aes_ctr_decrypt(received_ciphertext, encryption_key)
                print("Bob:", decrypted_message.decode())
            else:
                print("HMAC verification failed! Message might be tampered.")