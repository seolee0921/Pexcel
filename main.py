import cv2
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils.cell import get_column_letter

wb = Workbook()
ws = wb.active

image = cv2.imread("DOUDA LOGO.png")

pixel = 10


def _from_rgb(rgb):
    return "%02x%02x%02x" % rgb


for y in range(1, int(image.shape[0] / pixel)):
    for x in range(1, int(image.shape[1] / pixel)):
        cell = get_column_letter(x)
        ws.column_dimensions[cell].width = 3
        (B, G, R) = image[y * pixel][x * pixel]
        ws.cell(row=y, column=x).fill = PatternFill(fgColor=_from_rgb((R, G, B)), fill_type='solid')

wb.save("print-picture.xlsx")
print("SUCESS")
