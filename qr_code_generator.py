# QR Code Generator
# MSCS-633-M50 Advanced Artificial Intelligence
# Hands-On Assignment 2
# University of the Cumberlands, Summer 2026
#
# This program takes a URL from the user and turns it into
# a QR code image that can be scanned with a phone.

import qrcode          # library to create QR codes
from PIL import Image  # library to work with images
import sys


def generate_qr_code(url, filename="qr_code_output.png"):
    """
    Takes a URL string and creates a QR code image from it.
    Saves the image as a PNG file.
    Returns the filename of the saved image.
    """

    # set up the QR code with these settings:
    # version 1 = smallest size (21x21 grid)
    # ERROR_CORRECT_H = highest error correction so it still
    #   works even if part of the code gets damaged
    # box_size = how big each little square is in pixels
    # border = white space around the edges (4 is the minimum)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # put the URL data into the QR code
    qr.add_data(url)

    # let the library figure out the best layout
    qr.make(fit=True)

    # create the actual image with black squares on white background
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # save it to a file
    qr_image.save(filename)
    print(f"QR Code successfully generated and saved as '{filename}'")

    return filename


def show_qr_code(filename):
    """Opens the QR code image so the user can see it."""
    img = Image.open(filename)
    img.show()


def main():
    """Main function that runs the whole program."""

    # print a header so the user knows what app they are using
    print("=" * 50)
    print("       QR Code Generator Application")
    print("=" * 50)
    print()

    # ask the user to type in a URL
    url = input("Enter the URL to generate a QR code: ")

    # make sure they actually typed something
    if not url.strip():
        print("Error: Please enter a valid URL.")
        sys.exit(1)

    # generate the QR code and save it
    output_file = generate_qr_code(url)

    # open the image so they can see it
    show_qr_code(output_file)

    # let them know everything worked
    print(f"\nThe QR code for '{url}' has been created successfully.")
    print("You can scan this QR code with any QR code reader.")


# only run the program if this file is executed directly
if __name__ == "__main__":
    main()