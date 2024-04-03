from PIL import Image
import sys

def read_image(file_path):
    with Image.open(file_path) as img:
        return img.load()

def encrypt_image(image):
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = image[x, y]
            image[x, y] = (b, g, r)

def decrypt_image(image):
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = image[x, y]
            image[x, y] = (b, g, r)

def save_encrypted_image(image, file_path):
    image.save(file_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: python image_encrypt.py <input_file> <output_file> [encrypt|decrypt]")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    image = read_image(input_file)

    if len(sys.argv) < 4 or sys.argv[3] == "encrypt":
        encrypt_image(image)
        save_encrypted_image(image, output_file)
    else:
        decrypt_image(image)
        save_encrypted_image(image, output_file)

if __name__ == "__main__":
    main()