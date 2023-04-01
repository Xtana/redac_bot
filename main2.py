from PIL import Image, ImageDraw, ImageFont
import sys
#from screen_options import screan1, screan2, screan3

screan1 = {
    "name_background": [784, 186, 866, 210],
    "name": [864, 193],
    # "balance_background": ,
    # "balance": ,
    "num_chenge": 2,
    "path": "redactor_bot\T1.png",
    "opions": ["name","balance"]
}
screan2 = {}
screan3 = {}

def choose_img():
    print("Выберите фото: ")       # должны вылезти сообщения с фотками и их нумерациями
    item = int(input(""))
    if (item==1):
        return screan1
    if (item==1):
        return screan2
    if (item==1):
        return screan3
    else:
        sys.exit("Вы ввели что-то не то")


def img_funk(img,str,coord):
    for i in range(str[1],str[3]):
        pix = img.getpixel((1, i))
        for j in range(str[0],str[2]):
            if (img.getpixel((j, i))!=pix):
                img.putpixel((j,i), pix) 

    # pix = img.getpixel((1, 1))
    # img.putpixel((863, 230), pix)

    font = ImageFont.truetype('redactor_bot\ZenKakuGothicNew-Medium.ttf', size=(int((str[3]-str[1]) * 0.75281249999999))+3)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (coord[0],coord[1]),
        'Anna',
        fill=('#1B994C'),
        align = "center",
        font=font
        )
    img.show() 
    f = open("redactor_bot\Tmp.png", "wb")
    img.save(f, "BMP")           # Передаем файловый объект
    f.close()

def get_pil_text_size(text, font_size, font_name):
    font = ImageFont.truetype(font_name, font_size)
    size = font.getsize(text)
    return size

def num_of_change(screan):
    return int(input("Выберите количество изменений: 1 - %i: " %screan["num_chenge"]))

def what_to_change(screan):
    print("Выберите строки изменения")
    for i in range(len(screan["opions"])):
        print("%i) %s" %(i+1, screan["opions"][i]))

    return input()

def list_of_control_coord(screan, change):
    text_size = get_pil_text_size("Anna", (int((screan1["name_background"][3]-screan1["name_background"][1]) * 0.75281249999999))+3, 'redactor_bot\ZenKakuGothicNew-Medium.ttf')
    coord = screan["name_background"].copy()
    coord[0]  = screan[change][0] - text_size[0] 
    coord[1]  = screan[change][1] - int(text_size[1]/2)
    return coord


def main():
    screan = choose_img()
    #num = num_of_change(screan)
    change = what_to_change(screan)
    coord = list_of_control_coord(screan, change)
    open_img = Image.open(screan["path"])
    img_funk(open_img, screan1["name_background"], coord)
    
    
if __name__ == "__main__":
    main()
