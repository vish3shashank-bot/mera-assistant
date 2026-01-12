import time
from jnius import autoclass
from plyer import tts

# Android API Classes
PythonService = autoclass('org.kivy.android.PythonService')
Context = autoclass('android.content.Context')

# Payment Apps List
PAYMENT_APPS = [
    "com.google.android.apps.nbu.paisa.user", # GPay
    "com.phonepe.app", 
    "com.paytm",
    "com.bhimmobi"
]

def speak_hindi(text):
    # Mobile ki default language ko use karke Hindi bolega
    try:
        tts.speak(text)
    except:
        pass

def monitor():
    service = PythonService.mService
    power_manager = service.getSystemService(Context.POWER_SERVICE)
    activity_manager = service.getSystemService(Context.ACTIVITY_MANAGER)
    
    last_state = False # Screen state track karne ke liye

    while True:
        is_screen_on = power_manager.isInteractive()
        
        # Jab screen ON ho
        if is_screen_on and not last_state:
            speak_hindi("Namaste! Screen on ho gayi hai. Main taiyar hoon.")
            last_state = True
            
        # Jab screen OFF ho
        elif not is_screen_on and last_state:
            last_state = False
            # Screen band hone par assistant chup rahega

        # Security Check: Payment App Detection
        if is_screen_on:
            # Android 21+ ke liye task detection thoda restricted hai, 
            # par hum basic check run karte hain
            tasks = activity_manager.getRunningAppProcesses()
            for task in tasks:
                if task.importance == 100: # 100 means Foreground (screen par hai)
                    if task.processName in PAYMENT_APPS:
                        print("Security: Payment App Detected")
                        # Yahan assistant pause ho jayega
                        time.sleep(5) 

        time.sleep(2) # Battery bachane ke liye

if __name__ == '__main__':
    monitor()