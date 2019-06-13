from PIL import Image, ImageFont, ImageDraw
import textwrap

def createslide(width, height, path, name, slide):
    font1 = ImageFont.truetype("Arial.ttf", 72)
    font2 = ImageFont.truetype("Arial.ttf", 42)

    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    offset = 25
    for line in textwrap.wrap(slide[0], width = 18):
        draw.text((25, offset), line, (255, 255, 255), font=font1)
        draw = ImageDraw.Draw(img)
        offset += 82

    offset += 20
    for line in textwrap.wrap(slide[1], width = 23):
        draw.text((25, offset), line, (255, 255, 255), font=font2)
        draw = ImageDraw.Draw(img)
        offset += 52

    img.save(path + name + ".png")
