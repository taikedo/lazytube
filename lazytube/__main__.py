from . import parser, image

slides = parser.parsefile("data/example.txt")

for slide in slides:
    image.createslide(1280, 720, "data/images/", str(slides.index(slide)), slide)
