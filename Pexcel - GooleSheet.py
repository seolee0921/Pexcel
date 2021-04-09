import gspread
from oauth2client.service_account import ServiceAccountCredentials
import cv2
from openpyxl.styles import PatternFill

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = 'pexcel.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)

gc = gspread.authorize(credentials)
spreadsheet_url = '{https://docs.google.com/spreadsheets/d/1p3OonSqr_3wtTNb0AMIcPp3wMWl57YI6wcip79E5VwY/edit#gid=0}'
doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet('display')

pixel = 10

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

    cv2.imwrite('save_video.png', frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
    cam.release()

worksheet.resize(int(1080 / pixel), int(1920 / pixel))

def transform(number):
    if number > 26:
        first = int(number / 26)
        second = int(number % 26)

        if second == 0:
            first = first - 1
            second = 26
        if first > 26:
            index = transform(first) + chr(second + 64)
            return index

        index = chr(first + 64) + chr(second + 64)
        return index
    else:
        return chr(number + 64)
n = 1

for y in range(1,int(1080 / pixel + 1)):
    for x in range(1, int(1920 / pixel + 1)):
        get_index = transform(x) + f'{y}'
        print(get_index)
        worksheet.update_acell(get_index, n)
        n = n + 1

# while True:
#     # capture()
#     #
#     # image = cv2.imread("save_video.png")
#
#     for y in range(1, int(1080 / pixel + 1)):
#         for x in range(1, int(1920 / pixel + 1)):
#             index = transform(x) + f'{y}'
#             worksheet.update_acell(index, 'hi')
#
#     break;