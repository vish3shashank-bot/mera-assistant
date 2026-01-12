from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform
from jnius import autoclass

class MyAssistantApp(App):
    def build(self):
        return Label(text="Dost Assistant: ON\nMain background mein kaam kar raha hoon.")

    def on_start(self):
        if platform == 'android':
            # Background service ko start karne ka logic
            service = autoclass('org.test.myassistant.ServiceAssistant')
            mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
            service.start(mActivity, "")

if __name__ == '__main__':
    MyAssistantApp().run()