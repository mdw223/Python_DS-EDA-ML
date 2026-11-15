"""
Author: Malik Wensman
Email: mdwensma@ncsu.edu
Class: CSC 251-001 Fall 2026
Program: NETPBM IMAGE PROCESSING
Purpose: Blends two P3 color images and can convert the result to grayscale or sepia
Bugs: None
Acknowledgements: None
Date: 11/15/2026
"""

import pnmimage


def blend_P3_images(image1, image2):
    """Blends two P3 images using a weight entered by the user.
    Parameters:
    image1 (PPMimage): first color image
    image2 (PPMimage): second color image
    Returns:
    blended_image (PPMimage): P3 image using the smaller width and smaller height
    """
    while True:
        try:
            weight1 = float(input("Enter blending weight of first image as a percent (0-100): "))
        except ValueError:
            print("Invalid input. Please enter a value between 0 and 100.")
            continue
        if 0 <= weight1 <= 100:
            break
        print("Invalid input. Please enter a value between 0 and 100.")

    weight2 = 100 - weight1
    # Tenths keep weights such as 85 exact. 0.85 is not exact in binary floating point.
    weight1_tenths = round(weight1 * 10)
    weight2_tenths = 1000 - weight1_tenths
    min_width = min(image1.width, image2.width)
    min_height = min(image1.height, image2.height)
    comment = f"# blended image {weight1:.1f}%/{weight2:.1f}%"

    output_image = pnmimage.PPMimage(type='P3', comment=comment, width=min_width, height=min_height, max=image1.max)
    for i in range(min_height):
        blended_row = []
        for j in range(min_width):
            red1, green1, blue1 = image1.pixels[i][j]
            red2, green2, blue2 = image2.pixels[i][j]
            red = (weight1_tenths * red1 + weight2_tenths * red2) // 1000
            green = (weight1_tenths * green1 + weight2_tenths * green2) // 1000
            blue = (weight1_tenths * blue1 + weight2_tenths * blue2) // 1000
            blended_row.append((red, green, blue))
        output_image.pixels.append(blended_row)
    return output_image


def main():
    """Loads two P3 images, blends them, and writes the chosen result.
    Parameters:
    None
    Returns:
    None
    """
    image1 = pnmimage.PPMimage()
    image2 = pnmimage.PPMimage()
    image1.load_P3_image()
    image2.load_P3_image()

    blended_image = blend_P3_images(image1, image2)

    print("\nImage processing options:")
    print("1: Convert to grayscale")
    print("2: Convert to sepia")
    print("3: No further processing")

    while True:
        choice = input("Enter processing option: ").strip()
        if choice in ('1', '2', '3'):
            break
        print("Invalid choice. Please try again.")

    if choice == '1':
        blended_image = blended_image.convert_to_BW()
        blended_image.comment += ", converted to grayscale"
        extension = ".pgm"
        kind = "grayscale"
    elif choice == '2':
        blended_image = blended_image.convert_to_sepia()
        blended_image.comment += ", converted to sepia"
        extension = ".ppm"
        kind = "sepia"
    else:
        extension = ".ppm"
        kind = "color"

    output_filename = input("Enter output filename: ")
    while not output_filename.endswith(extension):
        output_filename = input(f"Enter output filename with a {extension} extension: ")

    blended_image.output_image(output_filename)
    
    print()
    print(f"Output file for {kind} blended image: {output_filename}")
    print(blended_image)


if __name__ == "__main__":
    main()
