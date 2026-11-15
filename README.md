# QR Code Generator

A Python-based desktop application that allows users to generate customized QR codes with different colors, optional logos, and a live preview. Built using **Tkinter**, **qrcode**, and **Pillow**, the application provides a simple graphical interface with light and dark mode support.

## ✨ Features

- **QR Code Generation:** Generate QR codes from text, URLs, or other data.
- **Custom Colors:** Choose custom foreground and background colors using a color picker.
- **Logo Integration:** Add your own PNG or JPG logo to the center of the QR code.
- **Live Preview:** Preview the generated QR code directly within the application.
- **Save as PNG:** Export generated QR codes as PNG images to your preferred location.
- **Dark Mode:** Switch between light and dark themes.
- **High Error Correction:** Uses the highest QR error correction level (Level H) to improve readability when adding a logo.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical User Interface |
| qrcode | QR code generation |
| Pillow (PIL) | Image processing and logo integration |

## 📋 Requirements

- Python 3.8 or higher
- pip package manager

## 🚀 Installation

**1. Clone the repository**

```bash
git clone https://github.com/Albert-006/Advanced-QR-Code-Generator.git
```

**2. Navigate to the project directory**

```bash
cd Advanced-QR-Code-Generator
```

**3. Install the required dependencies**

```bash
pip install qrcode[pil] Pillow
```

**4. Run the application**

```bash
python main.py
```

## 📖 How to Use

1. Launch the application.
2. Enter the text, URL, or data you want to encode.
3. Enter a filename for your QR code.
4. Customize the QR code's foreground and background colors.
5. Optionally, select an image to add as a logo.
6. Click **Generate QR Code**.
7. Choose the destination to save your QR code.
8. View the generated QR code in the preview section.

You can also switch between light and dark modes using the theme toggle button.

## 📂 Project Structure

```text
Code-Generator/
│
├── main.py          # Main application
├── README.md        # Project documentation
└── requirements.txt # Python dependencies
```

## 📦 Dependencies

```text
qrcode[pil]
Pillow
```

## 🖼️ Application Highlights

- Customizable QR code appearance.
- Optional center logo integration.
- Interactive graphical interface.
- Instant QR code preview.
- PNG image export.
