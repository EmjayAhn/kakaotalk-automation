import pyautogui
import subprocess

subprocess.run(['pkill', '-x', 'KakaoTalk'])
kakao_talk = subprocess.run(['open', '/Applications/KakaoTalk.app'])
print(kakao_talk)
