import requests
import pyautogui
while True:
    r=requests.get('http://[your ip]:8080/get?gyrX&gyrY&gyrZ&gyr')
    d=r.json()
    x=d["buffer"]["gyrX"]["buffer"][0]
    z=d["buffer"]["gyrZ"]["buffer"][0]
    if abs(z)>0.009 and abs(x)>0.009:
        pyautogui.move(-400*z,-400*x)
