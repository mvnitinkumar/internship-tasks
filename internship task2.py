import cv2
import numpy as np

def encrypt_image(image_path, key):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or invalid image format.")
    
    encrypted_image = (image ^ key) % 256  
    cv2.imwrite("encrypted_image.png", encrypted_image)
    print("Image encrypted and saved as 'encrypted_image.png'")

def decrypt_image(encrypted_path, key):
    encrypted_image = cv2.imread(encrypted_path)
    if encrypted_image is None:
        raise ValueError("Encrypted image not found.")
    
    decrypted_image = (encrypted_image ^ key) % 256  
    cv2.imwrite("decrypted_image.png", decrypted_image)
    print("Image decrypted and saved as 'decrypted_image.png'")

if __name__ == "__main__":
    choice = input("Do you want to encrypt or decrypt? (e/d): ")
    image_path = input("Enter image path: ")
    key = int(input("Enter encryption key (0-255): "))
    
    if choice.lower() == 'e':
        encrypt_image(image_path, key)
    elif choice.lower() == 'd':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice.")
