from PIL import ImageFilter
from PIL import Image
from ahk import AHK
import requests
import math
import time

class Canvas:
    start: tuple = (881, 236) # coordinates of the first pixel
    color: tuple = (1454, 1117) # coordinates of the change color button
    color_input: tuple = (1445, 996) # coordinates of the change color text input
    color_hide: tuple = (1777, 623) # coordinates of the hide change color modal button
    pixel_size: int = 26 # roughly the distance between the centers of 2 pixels

    @classmethod
    def rgb_to_hex(self, rgb: str) -> str:
        r, g, b = rgb
        r, g, b = int(r), int(g), int(b)
        hex_color = f"#{r:02X}{g:02X}{b:02X}"
        return hex_color

    @classmethod
    def fetch_image(self, url: str=None, blur_thresold: float=0.75) -> Image:
        # fetch only if url is supplied, else default to 'image.png'
        if url:
            with open('input.png', 'wb') as file:
                file.write(requests.get(url).content)
        img = Image.open('input.png')
        img = img.resize((32, 32))
        img = img.filter(ImageFilter.GaussianBlur(blur_thresold))
        img.save('output.png')
        return img

    @classmethod
    def euclidean_distance(self, rgb1: tuple, rgb2: tuple) -> float:
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        distance = math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)
        return distance

    @classmethod
    def get_pixels(self, img: Image, threshold: int=10) -> dict[str, list[tuple]]:
        pixels = {}
        pix = img.load()
        x, y = img.size
        for y_ in range(y):
            for x_ in range(x):
                px = pix[x_, y_]
                px = (px[0], px[1], px[2])

                found_pixel = False
                for ky in pixels:
                    if Canvas.euclidean_distance(px, ky) < threshold:
                        pixels[ky].append((x_, y_))
                        found_pixel = True
                        break

                if not found_pixel:
                    pixels[px] = [[x_, y_]]
        return pixels

    def __init__(self, ahk: AHK, width: int, height: int):
        # width and height are not used yet
        self.width: int = width
        self.height: int = height
        self.ahk: AHK = ahk

    def paint(self, x: int, y: int):
        target_x = self.start[0]+(Canvas.pixel_size*x)
        target_y = self.start[1]+(Canvas.pixel_size*y)
        self.ahk.click(target_x, target_y)

    def change_color(self, hex_color: str, pause_interval: float=0.05):
        self.ahk.click(self.color[0], self.color[1])
        time.sleep(pause_interval)
        self.ahk.click(self.color_input[0], self.color_input[1])
        time.sleep(pause_interval)
        self.ahk.type(hex_color)
        time.sleep(pause_interval)
        self.ahk.click(self.color_hide[0], self.color_hide[1])
        time.sleep(pause_interval)
