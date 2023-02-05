from PIL import Image, ImageDraw, ImageFont
import pandas as pd

df = pd.read_excel('nama.xlsx')

for i in range(len(df['Nama'])):
    nama = df['Nama'][i]
    img = Image.open('sertif.jpg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype(
        r'C:\Users\alghi\Downloads\Inter\static\Inter-Bold.ttf', 144)
    d1.text((130, 649), nama, font=myFont, fill=(106, 171, 195))
    im1 = img.convert('RGB')
    im1.save(nama + '.pdf')
print("Done Boss")
