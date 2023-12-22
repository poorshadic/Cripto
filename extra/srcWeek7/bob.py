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
    
    # Configurar servidor para receber conexão
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12345))  # Exemplo de endereço e porta
        s.listen()
        conn, addr = s.accept()
        
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                # Processar mensagem recebida
                received_ciphertext = data[:-32]  # Assume que os últimos 32 bytes são o HMAC
                received_hmac = data[-32:]  # Últimos 32 bytes são o HMAC
                
                # Verificar HMAC, descriptografar
                if verify_hmac(received_ciphertext, received_hmac, auth_key):
                    # Se o HMAC estiver correto, descriptografar a mensagem
                    decrypted_message = aes_ctr_decrypt(received_ciphertext, encryption_key)
                    print("Received message from Alice:", decrypted_message.decode())
                else:
                    print("HMAC verification failed! Message might be tampered.")
