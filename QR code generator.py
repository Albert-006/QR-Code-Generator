import qrcode
from tkinter import *
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk

logo_path = None
qr_fg = "black"
qr_bg = "white"
dark_mode = False


def choose_logo():
    global logo_path
    logo_path = filedialog.askopenfilename(
        title="Select Logo",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )
    if logo_path:
        messagebox.showinfo("Logo Selected", f"Logo selected:\n{logo_path}")


def choose_fg_color():
    global qr_fg
    color = colorchooser.askcolor()[1]
    if color:
        qr_fg = color
        fg_btn.config(bg=qr_fg)


def choose_bg_color():
    global qr_bg
    color = colorchooser.askcolor()[1]
    if color:
        qr_bg = color
        bg_btn.config(bg=qr_bg)


def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        root.config(bg="#1e1e1e")
        frame.config(bg="#2d2d2d")
        title_label.config(bg="#1e1e1e", fg="white")
        labels = frame.pack_slaves()
        for widget in labels:
            if isinstance(widget, Label):
                widget.config(bg="#2d2d2d", fg="white")
        mode_btn.config(text="Switch to Light Mode")
    else:
        root.config(bg="#f8f8f8")
        frame.config(bg="white")
        title_label.config(bg="#f8f8f8", fg="black")
        labels = frame.pack_slaves()
        for widget in labels:
            if isinstance(widget, Label):
                widget.config(bg="white", fg="black")
        mode_btn.config(text="Switch to Dark Mode")


def generate_qr():
    data = entry_data.get()
    filename = entry_name.get()

    if not data.strip():
        messagebox.showwarning("Input Error", "Please enter text or link!")
        return

    if not filename.strip():
        messagebox.showwarning("Input Error", "Please enter a file name!")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        initialfile=filename,
        filetypes=[("PNG Image", "*.png")]
    )

    if not save_path:
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=qr_fg, back_color=qr_bg).convert("RGB")

    # Add logo
    if logo_path:
        try:
            logo = Image.open(logo_path)
            qr_width, qr_height = qr_img.size
            logo_size = qr_width // 5
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            qr_img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)
        except Exception as e:
            messagebox.showerror("Logo Error", f"Failed to add logo:\n{e}")

    qr_img.save(save_path)

    # Preview
    global preview_img
    preview = qr_img.resize((220, 220))
    preview_img = ImageTk.PhotoImage(preview)
    qr_label.config(image=preview_img)

    messagebox.showinfo("Success", f"QR Code saved:\n{save_path}")


# ---------------- UI ----------------

root = Tk()
root.title("Advanced QR Code Generator")
root.geometry("550x720")
root.config(bg="#f8f8f8")

title_label = Label(root, text="QR CODE GENERATOR", font=("Arial", 20, "bold"), bg="#f8f8f8")
title_label.pack(pady=20)

mode_btn = Button(root, text="Switch to Dark Mode", font=("Arial", 10, "bold"),
                  command=toggle_dark_mode)
mode_btn.pack()

frame = Frame(root, bg="white", bd=3, relief=RIDGE)
frame.pack(padx=20, pady=10, fill=X)

Label(frame, text="Enter Text / Link:", font=("Arial", 12, "bold"), bg="white").pack(pady=8)
entry_data = Entry(frame, font=("Arial", 12), width=40, bd=2, relief="solid")
entry_data.pack(pady=6)

Label(frame, text="Enter File Name:", font=("Arial", 12, "bold"), bg="white").pack(pady=8)
entry_name = Entry(frame, font=("Arial", 12), width=40, bd=2, relief="solid")
entry_name.pack(pady=6)

# Color pickers
Label(frame, text="QR Foreground Color:", font=("Arial", 12, "bold"), bg="white").pack(pady=6)
fg_btn = Button(frame, bg=qr_fg, width=10, command=choose_fg_color)
fg_btn.pack()

Label(frame, text="QR Background Color:", font=("Arial", 12, "bold"), bg="white").pack(pady=6)
bg_btn = Button(frame, bg=qr_bg, width=10, command=choose_bg_color)
bg_btn.pack()

Button(frame, text="Choose Logo (Optional)", bg="#444", fg="white",
       font=("Arial", 12, "bold"), command=choose_logo).pack(pady=12)

Button(frame, text="Generate QR Code", bg="#0078ff", fg="white",
       font=("Arial", 14, "bold"), command=generate_qr).pack(pady=20)

Label(root, text="QR Preview:", bg="#f8f8f8", font=("Arial", 14, "bold")).pack(pady=10)
qr_label = Label(root, bg="#f8f8f8")
qr_label.pack()

root.mainloop()
