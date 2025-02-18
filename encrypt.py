import cv2

# Load input image
img = cv2.imread("input.jpg")

if img is None:
    print("Error: Could not load the input image.")
    exit()

msg = input("Enter secret message: ") + "###"  # Append end marker
password = input("Enter a passcode: ")

# ASCII dictionary for encoding
d = {chr(i): i for i in range(256)}

n, m, z = 0, 0, 0  # Pixel positions

for char in msg:
    img[n, m, z] = d[char]  # Hide character in pixel
    z = (z + 1) % 3  # Move to next color channel
    if z == 0:  # If all 3 channels are used, move to next pixel
        m += 1
        if m == img.shape[1]:  # If column limit reached, move to next row
            m = 0
            n += 1
            if n == img.shape[0]:  # Prevent out-of-bounds error
                print("Error: Message too long for this image!")
                exit()

cv2.imwrite("encryptedImage.jpg", img)
print("Encryption successful! Message hidden in 'encryptedImage.jpg'.")
