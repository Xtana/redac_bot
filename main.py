from PIL import Image, ImageDraw, ImageFont
import easyocr
import cv2


img1 = cv2.imread('sign_board.jpg')

def text_recognition():
    img1 = cv2.imread('redactor_bot\qw.jpg')
    img = 'redactor_bot\qw.jpg'
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(img)

    for (coord, text, prob) in result:

        (topleft, topright, bottomright, bottomleft) = coord
        tx,ty = (int(topleft[0]), int(topleft[1]))
        bx,by = (int(bottomright[0]), int(bottomright[1]))
        cv2.rectangle(img1, (tx,ty), (bx,by), (0, 255, 0), 2)

    cv2.imwrite('redactor_bot\qw2.jpg',img1)
    
    return result

def img_funk(img, item, result):
    if (item == 1):
        tx = result[5][0][0][0]
        ty = result[5][0][0][1]
        bx = result[5][0][2][0]
        by = result[5][0][2][1]
        print(tx,ty,bx,by)

    for i in range(ty,by):
        pix = img.getpixel((1, i))
        for j in range(tx,bx):
            if (img.getpixel((j, i))!=pix):
                img.putpixel((j,i), pix) # Изменяем цвет пикселя

    font = ImageFont.truetype('redactor_bot\ZenKakuGothicNew-Medium.ttf', size=60)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (tx,ty),
        'Самохин Роман А.',
        fill=('#FFFFFF'),
        align = "center",
        font=font
        )
    img.show()  

    f = open("tmp.png", "wb")
    img.save(f, "BMP")           # Передаем файловый объект
    f.close()


def main():
    a = text_recognition()
    print(a)
    print(a[4][0],a[4][1])
    img_funk(Image.open("redactor_bot\qw.jpg"), 1, a)
    
    
if __name__ == "__main__":
    main()
