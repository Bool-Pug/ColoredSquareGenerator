from PIL import Image
from datetime import datetime


im = Image.open("brown-Guernsey-cow.webp")
pixels = im.load()

width, height = im.size
old_pixels = pixels

starttime = datetime.now()

for i in range(20):
    for x in range(width-1):
        for y in range(height):

            pixels[x, y] = (
                round((pixels[x,y][0] + pixels[x+1,y][0]) * 0.5),
                round((pixels[x,y][1] + pixels[x+1,y][1]) * 0.5),
                round((pixels[x,y][2] + pixels[x+1,y][2]) * 0.5))
    print(f"Iteration # {i} complete!")
    print(f"Time Spent: + {datetime.now()-starttime}")

im.show()

