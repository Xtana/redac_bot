from PIL import Image, ImageDraw, ImageFont
import easyocr
import cv2

def text_recognition(path):
    img1 = cv2.imread(path)
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(path)

    for (coord, text, prob) in result:

        (topleft, topright, bottomright, bottomleft) = coord
        tx,ty = (int(topleft[0]), int(topleft[1]))
        bx,by = (int(bottomright[0]), int(bottomright[1]))
        cv2.rectangle(img1, (tx,ty), (bx,by), (0, 255, 0), 2)

    cv2.imwrite('redactor_bot\qw2.jpg',img1)
    
    return result

def find_str(result):
    item = int(input("Введите строку: "))
    str_of_coord = []
    if (item >= 1):
        tx = result[item-1][0][0][0]
        ty = result[item-1][0][0][1]
        bx = result[item-1][0][2][0]
        by = result[item-1][0][2][1]
    str_of_coord.extend([tx,ty,bx,by]) 
    return str_of_coord
    

def img_funk(img,str):
    width = img.size[0]
    height = img.size[1]
    size = int(height / 5)

    for i in range(str[1],str[3]):
        pix = img.getpixel((1, i))
        for j in range(str[0],str[2]):
            if (img.getpixel((j, i))!=pix):
                img.putpixel((j,i), pix) # Изменяем цвет пикселя
    print(str[1]-str[3])

    font = ImageFont.truetype('redactor_bot\ZenKakuGothicNew-Medium.ttf', size=(int((str[3]-str[1]) * 0.75281249999999)))
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (str[0],str[1]),
        'Сохранить чееек',
        fill=('#FFF'),
        align = "center",
        font=font
        )
    img.show()  

    f = open("redactor_bot\Tmp.png", "wb")
    img.save(f, "BMP")           # Передаем файловый объект
    f.close()


def main():
    path = "redactor_bot\est.jpg"
    open_img = Image.open(path)
    a = text_recognition(path)
    str_coord = find_str(a)
    img_funk(open_img, str_coord)
    
    
if __name__ == "__main__":
    main()
