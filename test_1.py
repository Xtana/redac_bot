from PIL import Image, ImageDraw, ImageFont

img = Image.open("redactor_bot\qw.jpg")

print(img.size)
for i in range(620,800):
    pix = img.getpixel((1, i))
    for j in range(1,1000):
        if (img.getpixel((j, i))!=pix):
            img.putpixel((j,i), pix) # Изменяем цвет пикселя

font = ImageFont.truetype('redactor_bot\ZenKakuGothicNew-Medium.ttf', size=60)
draw_text = ImageDraw.Draw(img)
draw_text.text(
    (415,650),
    '500 ₽',
    fill=('#FFFFFF'),
    align = "center",
    font=font
    )
img.show()                            # Просматриваем изображение

f = open("tmp.png", "wb")
img.save(f, "BMP")           # Передаем файловый объект
f.close()