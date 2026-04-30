from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)

    # Simple encryption: add key value to each pixel
    encrypted_pixels = (pixels + key) % 256

    encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_img.save("encrypted.png")

    print("✅ Encrypted image saved as encrypted.png")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)

    # Reverse operation
    decrypted_pixels = (pixels - key) % 256

    decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_img.save("decrypted.png")

    print("✅ Decrypted image saved as decrypted.png")


# --- User Input ---
print("=== Image Encryption Tool ===")

choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()
path = input("Enter image path: ")
key = int(input("Enter key (0-255): "))

if choice == 'e':
    encrypt_image(path, key)

elif choice == 'd':
    decrypt_image(path, key)

else:
    print("❌ Invalid choice")