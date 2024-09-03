import pyautogui
import time
import pyperclip
if __name__ == '__main__':
    cursorLocation = pyautogui.position();
    print(cursorLocation)

    #  1251,1061
    #  239,11
    #  191,426
    #  669,224
    #  1797,905

    pyautogui.click(1251,1061);
    time.sleep(1);
    pyautogui.click(239,11);
    time.sleep(1);
    pyautogui.click(191,426);
    time.sleep(1);
    print(cursorLocation)
    pyautogui.moveTo(669,224)
    pyautogui.dragTo(1797,905,duration=1.0,button='left')

    pyautogui.hotkey('ctrl','c');
    time.sleep(1);
    text = pyperclip.paste();
    print(text)



    