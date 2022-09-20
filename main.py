import time
import _ctypes
import pyautogui
import pywinauto, subprocess, pywinauto.keyboard
from pywinauto.application import Application

build = 1924

FileZilla = 'C:\\Program Files\\FileZilla FTP Client\\filezilla.exe'
HOST = 'ftp.yourdolphin.com'
USERNAME = 'guide_services'
PASSWORD = 'gu1d3@Ser'
UPDATE_FOLDER = f'Update_{build}'
GUIDE_DIRECTORY = 'GuideConnect'
BUILD = '\\\\dev\\\\betareg\\\\guide\\\\'


def filezilla_sign_in():
    subprocess.Popen(FileZilla)

    global app
    app = Application(backend="uia").connect(path=FileZilla)

    global main_dlg
    main_dlg = app.window(title='FileZilla')
    main_dlg.wait('visible', timeout=30, retry_interval=5)

    main_dlg.child_window(title="Host:", auto_id="-31829", control_type="Edit").type_keys(HOST)
    main_dlg.child_window(title="Username:", auto_id="-31827", control_type="Edit").type_keys(USERNAME)
    main_dlg.child_window(title="Password:", auto_id="-31825", control_type="Edit").type_keys(PASSWORD)
    main_dlg.child_window(title="Quickconnect", auto_id="-31944", control_type="Button").click_input()


filezilla_sign_in()


def add_update_folder():
    global signed_in
    signed_in = app.window(title='guide_services@ftp.yourdolphin.com - FileZilla')
    signed_in.wait('visible', timeout=30, retry_interval=5)

    signed_in.child_window(title="/", control_type="TreeItem").click_input('right')
    time.sleep(3), pyautogui.press('down', presses=4), pyautogui.press('enter')

    signed_in.child_window(title="Please enter the name of the directory which should\nbe created:",
                           auto_id="-31773", control_type="Edit").type_keys(UPDATE_FOLDER)
    signed_in.child_window(title="OK", auto_id="5100", control_type="Button").click_input()

    signed_in.child_window(title=f"Update_{build}", control_type="TreeItem").click_input('right')
    time.sleep(3), pyautogui.press('c'), time.sleep(3)

    signed_in.child_window(title="Please enter the name of the directory which should\nbe created:",
                           auto_id="-31769", control_type="Edit").type_keys(GUIDE_DIRECTORY)
    signed_in.child_window(title="OK", auto_id="5100", control_type="Button").click_input()


add_update_folder()


def add_msi_files():
    signed_in.child_window(auto_id="1001", control_type="Edit", found_index=0).type_keys(BUILD)
    pyautogui.press('enter', interval=2)
    signed_in.child_window(best_match="..", control_type="ListItem", found_index=0).click_input()
    time.sleep(3), pyautogui.hotkey('ctrlleft', 'f'), time.sleep(3)
    signed_in.child_window(title="Quick Search:", auto_id="-31888", control_type="Edit").type_keys(f'{build}')
    signed_in.child_window(best_match=f"{build }", control_type="ListItem").double_click_input()
    signed_in.child_window(title="Quick Search:", auto_id="-31888", control_type="Edit").set_edit_text(u'')
    signed_in.child_window(title="Quick Search:", auto_id="-31888", control_type="Edit").type_keys('msi')
    signed_in.child_window(best_match=f"msi", control_type="ListItem").double_click_input()
    signed_in.child_window(best_match=f"{GUIDE_DIRECTORY}", control_type="ListItem").double_click_input()
    signed_in.child_window(title=f"GuideConnect.msi", control_type="ListItem").double_click_input()

    try:
        signed_in.child_window(best_match=f"Update", control_type="ListItem").double_click_input()

    except pywinauto.findbestmatch.MatchError:
        pass


add_msi_files()

#
# def add_guide_up():
#     signed_in.child_window(auto_id="1001", control_type="Edit", found_index=0).type_keys(BUILD)
#     pyautogui.press('enter', interval=2)
#     signed_in.child_window(best_match=f"{build}", control_type="ListItem").double_click_input()
#     signed_in.child_window(title="core", control_type="ListItem").double_click_input()
#     signed_in.child_window(title="win32", control_type="ListItem").double_click_input()
#     signed_in.child_window(best_match="amd64", control_type="ListItem").select()
#     time.sleep(3), pyautogui.hotkey('ctrlleft', 'f'), time.sleep(3)
#     signed_in.child_window(title="Quick Search:", auto_id="-31888", control_type="Edit").type_keys('GuideUp.exe')
#
#     try:
#         signed_in.child_window(best_match="GuideUp.exe", control_type="ListItem").double_click_input()
#
#     except _ctypes.COMError:
#         pass
#
#
# add_guide_up()
