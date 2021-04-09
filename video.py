import cv2
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils.cell import get_column_letter
import xlwings as xl
import win32com.client

excel = win32com.client.Dispatch("Excel.Application")

wb = Workbook()
ws = wb.active

pixel = 5

def _from_rgb(rgb):
    return "%02x%02x%02x" % rgb

CAM_ID = 0

def capture(camid=CAM_ID):
    # 윈도우 사용자는 마지막에 cv2.CAP_DSHOW 추가
    cam = cv2.VideoCapture(camid, cv2.CAP_DSHOW)
    cam.set(3, 1920)
    cam.set(4, 1080)
    if cam.isOpened() == False:
        print('cant open the cam (%d)' % camid)
        return None

    ret, frame = cam.read()
    if frame is None:
        print('frame is not exist')
        return None

    # png로 압축 없이 영상 저장
    cv2.imwrite('save_video.png', frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
    cam.release()


while True:
    capture()

    image = cv2.imread("save_video.png")

    istrue = False

    for y in range(1, int(image.shape[0] / pixel)):
        for x in range(1, int(image.shape[1] / pixel)):
            if(istrue == False):
                cell = get_column_letter(x)
                ws.column_dimensions[cell].width = 3
            (B, G, R) = image[y * pixel][x * pixel]
            ws.cell(row=y, column=x).fill = PatternFill(fgColor=_from_rgb((R, G, B)), fill_type='solid')
        istrue = True

    wb.save("print-picture.xlsx")
    break

open("print-picture.xlsx")
print("SUCESS")
