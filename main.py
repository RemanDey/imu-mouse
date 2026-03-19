import requests
import pyautogui

r=requests.get('http://172.31.193.127:8080/get?gyrX&gyrY&gyrZ&gyr')
print(r.json())
d=r.json()
while True:
    r=requests.get('http://172.31.193.127:8080/get?gyrX&gyrY&gyrZ&gyr')
    d=r.json()
    x=d["buffer"]["gyrX"]["buffer"][0]
    y=d["buffer"]["gyrY"]["buffer"][0]
    z=d["buffer"]["gyrZ"]["buffer"][0]
    if abs(z)>0.009 and abs(x)>0.009:
        pyautogui.move(-400*z,-400*x)
