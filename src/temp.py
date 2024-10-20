# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm

# # PDF faylni yaratish
# pdf_file = "test_form.pdf"
# c = canvas.Canvas(pdf_file, pagesize=A4)

# # Sahifa o'lchamlari
# width, height = A4

# # QR kod va imzo maydonlarini chizish
# def draw_qr_and_signature_boxes():
#     # QR kod maydoni
#     c.rect(10 * mm, height - 40 * mm, 25 * mm, 25 * mm)
    
#     # Talaba va Nazoratchi imzo maydonlari
#     c.drawString(150 * mm, height - 20 * mm, "Talaba ______________________")
#     c.drawString(150 * mm, height - 30 * mm, "Nazoratchi __________________")

# # Fan, FIO, variant maydonlari
# def draw_labels():
#     c.setFont("Helvetica", 10)
#     x_center = 50*mm
#     c.drawCentredString(10 * mm, height - 50 * mm, "Fan: Matematika")
#     c.drawCentredString(10 * mm, height - 55 * mm, "FIO: Ergashev Abdulaziz Davron o'g'li")
#     c.drawCentredString(10 * mm, height - 60 * mm, "Variant №: 136")
#     c.drawCentredString(10 * mm, height - 80 * mm, "Sana: _______________")
#     c.drawCentredString(10 * mm, height - 85 * mm, "Vaqt: _______________")

# # Javob doiralarini joylashtirish
# def draw_answer_circles():
#     x_start = 35 * mm
#     y_start = height - 70 * mm

#     # Birinchi qator (1-25)
#     for i in range(25):
#         for j in range(4):
#             c.circle(x_start + i * 10 * mm, y_start - j * 7 * mm, 3)
#         # Har 5ta ustunda qora kvadrat
#         if i % 5 == 0:
#             c.rect(x_start + i * 10 * mm - 5, y_start + 5 * mm, 10, 10, stroke=1, fill=1)

#     # Ikkinchi qator (26-50)
#     y_start -= 35 * mm
#     for i in range(25):
#         for j in range(4):
#             c.circle(x_start + i * 10 * mm, y_start - j * 7 * mm, 3)
#         if i % 5 == 0:
#             c.rect(x_start + i * 10 * mm - 5, y_start + 5 * mm, 10, 10, stroke=1, fill=1)

# # Funksiyalarni chaqiramiz
# draw_qr_and_signature_boxes()
# draw_labels()
# draw_answer_circles()

# # PDFni saqlash
# c.save()

# print(f"{pdf_file} muvaffaqiyatli yaratildi!")

import pandas as pd
atletikachilar = {
    "T/R":[i for i in range(1,14)],
    "Joyidan turib balandlikka sakrash sm":[57,60,58,61,63,58,55,64,65,64,66,61],
    "Siltab ko'tarish natijasi kg":[107.5,110,110,115,107.5,107.5,120,122.5,122.5,120,110]
}

def urtacha_qiymat(array):
    return round(sum(array) / len(array), 2)

def urtachaMinusqiymat(array):
    result = [round(urtacha_qiymat(array)-array[i],2) for i in range(len(array))]
    return result

def mosyigindi(array1, array2):
    summa = round(sum([urtachaMinusqiymat(array1)[i]*urtachaMinusqiymat(array2)[i] for i in range(11)]),2)
    return summa
X_=atletikachilar["Joyidan turib balandlikka sakrash sm"]
Y_=atletikachilar["Siltab ko'tarish natijasi kg"]

print(mosyigindi(X_,Y_))
