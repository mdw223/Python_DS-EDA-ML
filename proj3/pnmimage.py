"""
Author: Malik Wensman
Email: mdwensma@ncsu.edu
Class: CSC 251-001 Fall 2026
Program: PNMimage and PPMimage classes
Purpose: Stores P2 and P3 image data and converts P3 images to grayscale or sepia
Bugs: None
Acknowledgements: None
Date: 11/15/2026
"""


class PNMimage:
    def __init__(self, type: str = '', comment: str = "", width: int = 0, height: int = 0, max: int = 0):
        """Stores the header values and pixel data for a P2 or P3 image.
        Parameters:
        self (PNMimage): the image object being created
        type (str): magic number, such as P2 or P3
        comment (str): comment line from the image file
        width (int): image width in pixels
        height (int): image height in pixels
        max (int): maximum color value
        Returns:
        None
        """
        self.type = type
        self.comment = comment
        self.width = width
        self.height = height
        self.max = max
        self.pixels = []

    def output_image(self, filename: str):
        """Writes this image to a file in P2 or P3 format.
        Parameters:
        self (PNMimage): the image to write
        filename (str): name of the output file
        Returns:
        None
        """
        try:
            with open(filename, 'w') as file:
                file.write(f"{self.type}\n")
                file.write(f"{self.comment}\n")
                file.write(f"{self.width} {self.height}\n")
                file.write(f"{self.max}\n")
                if self.type == 'P2':
                    for row in self.pixels:
                        for pixel in row:
                            file.write(f"{pixel}\n")
                else:
                    for row in self.pixels:
                        for pixel in row:
                            file.write(f"{pixel[0]}\n{pixel[1]}\n{pixel[2]}\n")
        except OSError as error:
            print(error)

    def __str__(self):
        """Builds a text summary of this image.
        Parameters:
        self (PNMimage): the image to describe
        Returns:
        text (str): comment, magic number, width, and height
        """
        return f"{self.comment}\nType: {self.type}\nWidth: {self.width} Height: {self.height}"


class PPMimage(PNMimage):
    def __init__(self, type: str = '', comment: str = "", width: int = 0, height: int = 0, max: int = 0):
        """Creates a P3 image object by calling the superclass constructor.
        Parameters:
        self (PPMimage): the image object being created
        type (str): magic number, normally P3
        comment (str): comment line from the image file
        width (int): image width in pixels
        height (int): image height in pixels
        max (int): maximum color value
        Returns:
        None
        """
        super().__init__(type, comment, width, height, max)

    def load_P3_image(self):
        """Prompts for a P3 file and stores its pixels in this object.
        Parameters:
        self (PPMimage): the image object to fill
        Returns:
        None
        """
        prompt = "Enter input filename for image: "
        while True:
            filename = input(prompt)
            try:
                with open(filename, 'r') as file:
                    tokens = []
                    comment = ''
                    for line in file:
                        stripped = line.strip()
                        if stripped.startswith('#'):
                            if comment == '':
                                comment = stripped
                            continue
                        tokens.extend(stripped.split())

                if len(tokens) < 4 or tokens[0] != 'P3':
                    raise ValueError("This file is not in PPM P3 format.")

                width = int(tokens[1])
                height = int(tokens[2])
                maximum = int(tokens[3])
                needed = width * height * 3
                values = tokens[4:]
                if len(values) < needed:
                    raise ValueError("This file is not in PPM P3 format.")

                pixels = []
                index = 0
                for _ in range(height):
                    row = []
                    for _ in range(width):
                        red = int(values[index])
                        green = int(values[index + 1])
                        blue = int(values[index + 2])
                        row.append((red, green, blue))
                        index += 3
                    pixels.append(row)

                self.type = 'P3'
                self.comment = comment
                self.width = width
                self.height = height
                self.max = maximum
                self.pixels = pixels
                return
            except ValueError:
                print("This file is not in PPM P3 format.")
            except OSError as error:
                print(error)
            prompt = "Enter input filename again: "

    def convert_to_BW(self):
        """Converts this P3 image to grayscale.
        Parameters:
        self (PPMimage): the color image to convert
        Returns:
        grayscale_image (PNMimage): P2 image using 30% red, 60% green, and 10% blue
        """
        grayscale_image = PNMimage(type='P2', comment=self.comment, width=self.width, height=self.height, max=self.max)
        for row in self.pixels:
            grayscale_row = []
            for pixel in row:
                red, green, blue = pixel
                gray_value = int(0.3 * red + 0.6 * green + 0.1 * blue)
                grayscale_row.append(gray_value)
            grayscale_image.pixels.append(grayscale_row)
        return grayscale_image

    def convert_to_sepia(self):
        """Converts this P3 image to sepia tones.
        Parameters:
        self (PPMimage): the color image to convert
        Returns:
        sepia_image (PPMimage): P3 sepia image, with each channel capped at 255
        """
        sepia_image = PPMimage(type='P3', comment=self.comment, width=self.width, height=self.height, max=self.max)
        for row in self.pixels:
            sepia_row = []
            for pixel in row:
                red, green, blue = pixel
                sepia_red = min(int(0.393 * red + 0.769 * green + 0.189 * blue), 255)
                sepia_green = min(int(0.349 * red + 0.686 * green + 0.168 * blue), 255)
                sepia_blue = min(int(0.272 * red + 0.534 * green + 0.131 * blue), 255)
                sepia_row.append((sepia_red, sepia_green, sepia_blue))
            sepia_image.pixels.append(sepia_row)
        return sepia_image
