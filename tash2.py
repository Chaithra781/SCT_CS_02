import numpy as np
from PIL import Image
import random

def load_image(path):
    image = Image.open(path)
    return np.array(image)

def save_image(data, path):
    img = Image.fromarray(data.astype(np.uint8))
    img.save(path)

def encrypt_image(image_array, method="swap", value=50):
    img = image_array.copy()

    if method == "swap":
        h, w, _ = img.shape
        for _ in range(10000):  # swap 10k random pixels
            x1, y1 = random.randint(0, h-1), random.randint(0, w-1)
            x2, y2 = random.randint(0, h-1), random.randint(0, w-1)
            img[x1, y1], img[x2, y2] = img[x2, y2].copy(), img[x1, y1].copy()

    elif method == "math":
        img = (img + value) % 256  # shift brightness (basic math encryption)

    return img

def decrypt_image(image_array, method="swap", value=50):
    img = image_array.copy()

    if method == "math":
        img = (img - value) % 256  # reverse brightness shift

    else:
        print("Swap decryption requires stored swap operations (not supported in simple mode).")
    
    return img

def main():
    input_path = r"C:\Users\chait\OneDrive\Desktop\internship\flower.jpg"
    encrypted_path = "encrypted.jpg"
    decrypted_path = "decrypted.jpg"

    image = load_image(input_path)

    # Encrypt
    encrypted_img = encrypt_image(image, method="math", value=50)
    save_image(encrypted_img, encrypted_path)
    print(f"Encrypted image saved as {encrypted_path}")

    # Decrypt
    decrypted_img = decrypt_image(encrypted_img, method="math", value=50)
    save_image(decrypted_img, decrypted_path)
    print(f"Decrypted image saved as {decrypted_path}")

if __name__ == "__main__":
    main()
