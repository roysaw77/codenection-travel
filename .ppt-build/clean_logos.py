from pathlib import Path
from PIL import Image, ImageChops

base = Path(__file__).parent / "logos"

def trim(image, background):
    rgb = image.convert("RGB")
    bg = Image.new("RGB", rgb.size, background)
    box = ImageChops.difference(rgb, bg).getbbox()
    return image.crop(box) if box else image

tourradar = trim(Image.open(base / "tourradar.png").convert("RGBA"), (255, 255, 255))
pixels = []
for red, green, blue, _ in tourradar.getdata():
    distance = max(255 - red, 255 - green, 255 - blue)
    alpha = 0 if distance < 8 else min(255, distance * 4)
    pixels.append((red, green, blue, alpha))
tourradar.putdata(pixels)
tourradar.save(base / "tourradar.png")

tripit = trim(Image.open(base / "tripit-clean.png").convert("RGB"), (247, 248, 243))
tripit.save(base / "tripit-clean.png")

life360 = Image.open(base / "life360.png").convert("RGBA")
alpha_box = life360.getchannel("A").getbbox()
if alpha_box:
    life360 = life360.crop(alpha_box)
life360.save(base / "life360.png")
