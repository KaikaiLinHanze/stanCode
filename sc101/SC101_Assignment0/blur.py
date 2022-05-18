"""
File: blur.py
Name: Kai
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:file for smiley-face
    :return:The blur algorithm uses the average RGB values of a pixel's nearest neighbors.
    """
    img_blank = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            red_sum = 0
            green_sum = 0
            blue_sum = 0
            point = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x <= (img.width - 1):
                        if 0 <= pixel_y <= (img.height - 1):
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            red_sum += pixel.red
                            green_sum += pixel.green
                            blue_sum += pixel.blue
                            point += 1
            img_show = img_blank.get_pixel(x, y)
            img_show.red = (red_sum/point)
            img_show.green = (green_sum/point)
            img_show.blue = (blue_sum/point)
    return img_blank

def main():
    """
    The uses the average RGB values of a pixel's nearest neighbors to make an effect of blur to smiley face
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
