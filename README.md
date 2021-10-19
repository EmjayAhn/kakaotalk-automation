# Macro for message using kakaotalk
스터디 모임 중 메시지를 자동으로 보내주길 바라는 매크로를 설정하고 싶어 만든
간단한 코드입니다.
원하는 날짜와 시간 매크로 기능은 Shell Script 의 crontab을 사용합니다.
## Requirements
- pyautogui
- Install Kakaotalk

## OS
- MAC

## Usage
- 채팅창 중 가장 상단에 있는 채팅창에 메시지를 보내게 됩니다.
- 따라서 카카오톡 내 기능중 '채팅창 상단 고정'을 사용하시면 가장 상단 채팅방이
고정됩니다.
- 아직, 영어로 보내는 것 밖에 되지 않습니다.
```bash
$ python3 main.py -m "Write your message you want to send"
```
