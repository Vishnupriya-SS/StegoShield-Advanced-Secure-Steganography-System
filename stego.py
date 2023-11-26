import tkinter as tk
from tkinter import filedialog
from PIL import Image

def encode_lsb(image_path, secret_message, output_path, pin):
    
    img = Image.open(image_path)
    img = img.convert("RGB")
    binary_secret_message = ''.join(format(ord(c), "08b") for c in secret_message)
    pin = ''.join(format(ord(c), "08b") for c in pin)
    binary_secret_message += pin
    if len(binary_secret_message) > img.size[0] * img.size[1] * 3:
        raise ValueError("Image too small to hold the message. Try using a larger image or a shorter message.")
    
    binary_secret_message += "00000000"
    print(binary_secret_message)
    message_index = 0
    message_bytes = bytes([int(binary_secret_message[i:i + 8], 2) for i in range(0, len(binary_secret_message), 8)])

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = list(img.getpixel((x, y)))
            for c in range(3):
                if message_index < len(binary_secret_message):
                    
                    pixel[c] = pixel[c] & ~1 | int(binary_secret_message[message_index])
                    message_index += 1
            img.putpixel((x, y), tuple(pixel))
    img.save(output_path)
    print("Message encoded successfully in the image.")

def decode_lsb(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")

    binary_message = ""
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = img.getpixel((x, y))
            for c in range(3):
                binary_message += format(pixel[c], "08b")[-1]  
    binary_list = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    
    end_index = binary_list.index("00000000") * 8 
    combined_binary = binary_message[:end_index]
    extracted_pin = combined_binary[-32:]
    binary_message = combined_binary[:len(combined_binary)-len(extracted_pin)]
    print("binary_message:",binary_message)
    print("orginal_pin:",extracted_pin)
    
    padded_length = (len(binary_message) + 7) // 8 * 8
    binary_message = binary_message.ljust(padded_length, "0")
    
    return binary_message, extracted_pin

def Binary_to_text(binary_string):
    text = ""
    padded_binary = binary_string.ljust((len(binary_string) + 7) // 8 * 8, "0")  
    for i in range(0, len(padded_binary), 8):
        byte = padded_binary[i:i + 8]
        text += chr(int(byte, 2))
    return text

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_path_var.set(file_path)




def encode_message():
    image_path = image_path_var.get()
    secret_message = secret_message_entry.get()
    pin = encode_Pin_entry.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if output_path:
        try:
            encode_lsb(image_path, secret_message, output_path, pin)
            status_var.set("Message encoded successfully!")
        except Exception as e:
            status_var.set(f"Error: {e}")

def decode_message():
    image_path = image_path_var.get()
    try:
        decoded_message, orginal_pin = decode_lsb(image_path)
        entered_pin = Decode_pin_entry.get()
        entered_pin = ''.join(format(ord(c), "08b") for c in entered_pin)
        print("ENTERED:", entered_pin)
        if entered_pin == orginal_pin:
            decoded_text = Binary_to_text(decoded_message)
            decoded_message_var.set(decoded_text)
            status_var.set("Message decoded successfully!")
            print("Decoded message:", decoded_message)  # Print the decoded message in the terminal
        else:
            decoded_message_var.set("")
            status_var.set("Error: Incorrect PIN")
    except Exception as e:
        status_var.set(f"Error: {e}")

root = tk.Tk()
root.title("LSB Steganography Application")

image_path_var = tk.StringVar()
tk.Label(root, text="Image Path:").grid(row=0, column=0)
tk.Entry(root, textvariable=image_path_var, state="readonly").grid(row=0, column=1)
tk.Button(root, text="Open Image", command=open_image).grid(row=0, column=2)

tk.Label(root, text="Secret Message:").grid(row=1, column=0)
secret_message_entry = tk.Entry(root)
secret_message_entry.grid(row=1, column=1)

tk.Label(root, text="PIN(4-digit):").grid(row=2, column=0)
encode_Pin_entry = tk.Entry(root, show='*')
encode_Pin_entry.grid(row=2, column=1)

tk.Button(root, text="Encode", command=encode_message).grid(row=3, column=0)

tk.Button(root, text="Decode", command=decode_message).grid(row=3, column=1)

decoded_message_var = tk.StringVar()
tk.Label(root, text="Decoded Message:").grid(row=4, column=0)
tk.Label(root, textvariable=decoded_message_var, wraplength=300, anchor="w", justify="left").grid(row=4, column=1)

tk.Label(root, text="Enter PIN For Decoding:").grid(row=5, column=0)
Decode_pin_entry = tk.Entry(root)
Decode_pin_entry.grid(row=5, column=1)

status_var = tk.StringVar()
status_label = tk.Label(root, textvariable=status_var, fg="red")
status_label.grid(row=6, column=0, columnspan=3)

root.mainloop()
