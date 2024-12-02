import pyautogui
import time
import keyboard
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--size", dest = "size", default = 0, help="Size data")

args = parser.parse_args()

# Durasi jeda agar setiap langkah tidak terlalu cepat
pyautogui.PAUSE = 0.3


def run():
    # Pindah dari vscode menuju excel
    pyautogui.hotkey("alt", "tab")  
    
    for i in range(int(args.size)):
      # copy nama jurnal
      pyautogui.hotkey("ctrl", "c")

      # ke window sistem
      if(i == 0):
        pyautogui.keyDown('alt')
        pyautogui.press('tab')      # Press Tab once
        time.sleep(0.1)  
        pyautogui.press('tab')      # Press Tab again
        pyautogui.keyUp('alt')      # Release the 'Alt' key
      else:
        pyautogui.hotkey("alt", "tab")  

      # pindah ke tombol tambah
      pyautogui.moveTo(180 , 75) 
      
      # klik tombol tambah
      pyautogui.click()
      
      # pindah ke form keterangan
      pyautogui.press('tab') 

      # paste nama jurnal
      pyautogui.hotkey("ctrl", "v")
      # enter pertama pindah ke bawah
      pyautogui.hotkey("enter")
      
      # copy nominal
      pyautogui.hotkey("alt", "tab")  
      pyautogui.hotkey("tab")  
      pyautogui.hotkey("ctrl", "c")
      pyautogui.hotkey("alt", "tab")  

      # enter ke dua
      pyautogui.hotkey("enter")
      # enter ke tiga
      pyautogui.hotkey("enter")
      # tulis kws
      pyautogui.write("1011303")
      # enter search
      pyautogui.hotkey("enter")
      # tab pilih kws
      pyautogui.hotkey("tab")
      # enter selesai
      pyautogui.hotkey("enter")

      # pindah ke kredit colom lalu paste
      pyautogui.press('right')
      pyautogui.hotkey("enter")
      pyautogui.hotkey("ctrl", "v")
      pyautogui.hotkey("enter")

      # colom 2
      pyautogui.hotkey("enter")
      pyautogui.hotkey("enter")
      pyautogui.write("3010171")

      # enter search
      pyautogui.hotkey("enter")
      # tab pilih kws
      pyautogui.hotkey("tab")
      # enter selesai
      pyautogui.hotkey("enter")


      # pindah ke kredit colom lalu paste
      pyautogui.press('left')
      pyautogui.hotkey("enter")
      pyautogui.hotkey("ctrl", "v")
      pyautogui.hotkey("enter")

      # save jurnal
      pyautogui.moveTo(580, 75)  
      pyautogui.click()  
      time.sleep(0.5)  
      pyautogui.hotkey("enter")
      time.sleep(0.5)  
      pyautogui.hotkey("enter")
      time.sleep(0.5)  
      pyautogui.press('left')
      time.sleep(0.5)  
      pyautogui.hotkey("enter")

      pyautogui.hotkey("alt", "tab")  
      pyautogui.press('down')
      pyautogui.press('left')  

try:
  run()
except KeyboardInterrupt:
   print("Program stopped by user")

