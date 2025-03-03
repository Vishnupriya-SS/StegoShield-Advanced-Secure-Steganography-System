# StegoShield – Advanced Secure Steganography

StegoShield is a high-security steganography system that embeds sensitive text into images using **LSB Steganography**, while integrating **AES-256 and RSA encryption** for enhanced data protection. This project ensures secure communication with **minimal impact on image quality and high retrieval accuracy**.

## 🚀 Features
- **LSB Steganography** – Efficiently hides text in images while preserving quality.
- **AES-256 Encryption** – Ensures strong encryption for embedded data.
- **RSA Key Management** – Secures encryption keys for better access control.
- **Graphical User Interface (GUI)** – User-friendly Tkinter-based UI for encoding and decoding messages.
- **Error Detection & Correction** – Reduces retrieval errors and enhances accuracy.
- **Cross-Platform Support** – Works seamlessly across Windows, macOS, and Linux.

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Libraries:** OpenCV, Cryptography, NumPy, Tkinter
- **Encryption:** AES-256, RSA
- **Image Processing:** LSB Steganography

## 📂 Installation
```bash
# Clone the repository
git clone https://github.com/Vishnupriya-SS/StegoShield.git
cd StegoShield

# Install dependencies
pip install -r requirements.txt
```

## 🖥️ Usage
### Encoding a Message
1. Run `python stegoshield.py`
2. Upload an image
3. Enter the secret message
4. Encrypt with AES-256 and RSA (optional)
5. Save the stego-image

### Decoding a Message
1. Load the encoded image
2. Enter the decryption key (if encryption was used)
3. Extract the hidden message


## 🔐 Security Enhancements
- Strong **AES-256 encryption** for securing hidden messages
- **RSA key management** for secure access
- **Minimal image distortion** for stealthy data embedding
