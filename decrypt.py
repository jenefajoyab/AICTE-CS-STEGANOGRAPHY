import cv2

# Load encrypted image
img = cv2.imread("encryptedImage.jpg")

if img is None:
    print("Error: Encrypted image not found or cannot be loaded.")
    exit()

# ASCII dictionary for decoding
c = {i: chr(i) for i in range(256)}

# Get password for verification
pas = input("Enter passcode for decryption: ")
password = input("Re-enter the passcode: ")

if password == pas:
    n, m, z = 0, 0, 0  # Pixel positions
    message_chars = []  # Use list for better performance

    while n < img.shape[0]:
        char = c[img[n, m, z]]  # Retrieve character
        message_chars.append(char)

        # Stop when end marker ("###") is found
        if len(message_chars) >= 3 and message_chars[-3:] == ["#", "#", "#"]:
            break

        z = (z + 1) % 3  # Move to next color channel
        if z == 0:
            m += 1
            if m == img.shape[1]:
                m = 0
                n += 1
                if n == img.shape[0]:  # Prevent out-of-bounds error
                    break

    # Convert list to string and remove "###" marker
    decrypted_message = "".join(message_chars[:-3])

    # Print output with proper formatting
    print("\nDecryption successful! Hidden message:\n")


    print('hello')

else:
    print("YOU ARE NOT authorized")
