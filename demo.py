from blowfish.core import BlowfishCBC
import os


def main():
    key = input("Enter key (4-56 chars): ").encode()
    if not 4 <= len(key) <= 56:
        print("Invalid key length!")
        return

    iv = os.urandom(8)
    bf = BlowfishCBC(key, iv)

    message = input("Enter message to encrypt: ").encode()

    # Шифрование
    ciphertext = bf.encrypt(message)
    print(f"\nEncrypted (hex): {ciphertext.hex()}")

    # Дешифрование
    decrypted = bf.decrypt(ciphertext)
    print(f"Decrypted: {decrypted.decode()}\n")


if __name__ == "__main__":
    main()
