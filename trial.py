from cryptography.fernet import Fernet

# Gerar uma chave e escrever em um arquivo
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Carregar a chave de um arquivo
def load_key():
    return open("secret.key", "rb").read()

# Função para criptografar a senha
def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Função para descriptografar a senha
def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Gerar e salvar uma chave (execute isso apenas uma vez)
generate_key()

# Exemplo de uso
senha = "minha_senha_secreta"
senha_criptografada = encrypt_password(senha)
print(f"Senha criptografada: {senha_criptografada}")

senha_descriptografada = decrypt_password(senha_criptografada)
print(f"Senha descriptografada: {senha_descriptografada}")
