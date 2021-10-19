import sys, getopt
import time
import pyautogui
import clipboard
import subprocess

def kakao_automation(message):
    subprocess.run(['pkill', '-x', 'KakaoTalk'])
    kakao_talk = subprocess.run(['open', '/Applications/KakaoTalk.app'])
    time.sleep(10)
    pyautogui.hotkey('command', '2')
    pyautogui.hotkey('command', '2')
    pyautogui.hotkey('command', '2')
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    pyautogui.typewrite(message, interval=0.01)
    pyautogui.hotkey('command', 'v')
    pyautogui.hotkey('enter')

def main(argv):
    FILE_NAME = argv[0]

    try:
        opts, etc_args = getopt.getopt(argv[1:], "h:m:", ["help", "message="])
    except getopt.GetoptError:
        print(FILE_NAME, '-m <message>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(FILE_NAME, '-m <type message you want to send>')
        elif opt in ("-m", "--message"):
            message = arg
            kakao_automation(message)



if __name__=='__main__':
    main(sys.argv)
    