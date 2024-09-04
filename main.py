import pyautogui
import time
import pyperclip
import openAiChat

def is_last_message_from_sender(chat_log:str,sender_name='rejaulkariam766'):
    messages = chat_log.strip().split('/2024')[-1]
    if sender_name in messages:
        return True
    
    return False;

if __name__ == '__main__':
    cursorLocation = pyautogui.position();
    print(cursorLocation)

    #  1251,1061
    #  239,11
    #  191,426
    #  723,226
    #  1797,905
    #  1390,863
    #  845,171

    pyautogui.click(1251,1061);
    time.sleep(1);
    while True:
        pyautogui.click(239,11);
        time.sleep(1);
        pyautogui.click(191,426);
        time.sleep(1);
        print(cursorLocation)
        pyautogui.moveTo(723,226)
        pyautogui.dragTo(1797,905,duration=1.0,button='left')

        pyautogui.hotkey('ctrl','c');
        time.sleep(3);
        pyautogui.click(1390,863)
        text = pyperclip.paste();
        print(text)
        if is_last_message_from_sender(text):
            res = openAiChat.chatWithGPT(text)
            print(res)
            pyperclip.copy(res);
            pyautogui.click(845,971);
            time.sleep(1);
            pyautogui.hotkey('ctrl','v');
            time.sleep(1);
            pyautogui.press('enter')





    