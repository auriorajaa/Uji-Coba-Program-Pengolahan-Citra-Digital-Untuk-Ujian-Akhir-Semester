import cv2
import numpy as np

# Convert various types to binary
def msg_to_bin(msg):
    if type(msg) == str:
        return ''.join([format(ord(i), "08b") for i in msg])
    elif type(msg) == bytes or type(msg) == np.ndarray:
        return [format(i, "08b") for i in msg]
    elif type(msg) == int or type(msg) == np.uint8:
        return format(msg, "08b")
    else:
        raise TypeError("Input type not supported")

# Hide secret message into the image
def hide_data(img, secret_msg):
    # Calculate the maximum bytes for encoding
    nBytes = img.shape[0] * img.shape[1] * 3 // 8
    print("Maximum Bytes for encoding:", nBytes)
    
    # Check if the number of bytes for encoding is less than the maximum bytes in the image
    if len(secret_msg) > nBytes:
        raise ValueError("Error encountered: insufficient bytes, need a bigger image or less data!!")
    
    secret_msg += '#####'  # Add delimiter to the message
    dataIndex = 0
    
    # Convert the input data to binary format
    bin_secret_msg = msg_to_bin(secret_msg)
    dataLen = len(bin_secret_msg)
    
    for values in img:
        for pixels in values:
            r, g, b = msg_to_bin(pixels)
            
            # Modify the LSB only if there is data remaining to store
            if dataIndex < dataLen:
                pixels[0] = int(r[:-1] + bin_secret_msg[dataIndex], 2)
                dataIndex += 1
            if dataIndex < dataLen:
                pixels[1] = int(g[:-1] + bin_secret_msg[dataIndex], 2)
                dataIndex += 1
            if dataIndex < dataLen:
                pixels[2] = int(b[:-1] + bin_secret_msg[dataIndex], 2)
                dataIndex += 1
            
            if dataIndex >= dataLen:
                break
        if dataIndex >= dataLen:
            break
    
    return img

# Extract hidden message from the image
def show_data(img):
    bin_data = ""
    
    for values in img:
        for pixels in values:
            r, g, b = msg_to_bin(pixels)
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]
    
    allBytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]
    decodedData = ""
    
    for bytes in allBytes:
        decodedData += chr(int(bytes, 2))
    
    if decodedData[-5:] == "#####":
        return decodedData[:-5]

# Encode data into the image
def encodeText():
    img_name = input("Enter image name (with extension): ")
    img = cv2.imread(img_name)
    print("The shape of the image is: ", img.shape)
    print("The original image is as shown below: ")
    
    resizedImg = cv2.resize(img, (500, 500))
    cv2.imshow("Original Image", resizedImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    data = input("Enter data to be encoded: ")
    if len(data) == 0:
        raise ValueError('Data is Empty')
    
    file_name = input("Enter the name of the new encoded image (with extension): ")
    encodedImage = hide_data(img, data)
    cv2.imwrite(file_name, encodedImage)

# Decode data from the image
def decodeText():
    img_name = input("Enter the name of the Steganographic image that has to be decoded (with extension): ")
    img = cv2.imread(img_name)
    print("The Steganographic image is as follows: ")
    
    resizedImg = cv2.resize(img, (500, 500))
    cv2.imshow("Steganographic Image", resizedImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    text = show_data(img)
    return text

# Steganography menu
def steganography():
    n = int(input("Image Steganography \n1. Encode the data \n2. Decode the data \nSelect the option: "))
    if n == 1:
        print("\nEncoding...")
        encodeText()
    elif n == 2:
        print("\nDecoding...")
        print("Decoded message is " + decodeText())
    else:
        raise Exception("Inserted value is incorrect!")

steganography()  # Run the steganography function
