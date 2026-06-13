from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BrykanHorrorApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20

        self.add_widget(Label(text='★ BRYKANHORROR PERSONAL AI ★', font_size='20sp', bold=True))
        
        self.ins = TextInput(multiline=True, hint_text='भाई, अपना टेक्स्ट यहाँ लिखो...')
        self.add_widget(self.ins)
        
        self.btn = Button(text='एआई चालू करें', background_color=(1, 0, 0, 1), font_size='18sp')
        self.btn.bind(on_press=self.check)
        self.add_widget(self.btn)
        
        self.lbl = Label(text='स्थिति: रेडी', font_size='16sp')
        self.add_widget(self.lbl)

    def check(self, instance):
        if self.ins.text.strip():
            self.lbl.text = "सफलता! आपका पर्सनल एआई काम कर रहा है।"
        else:
            self.lbl.text = "भाई पहले कुछ लिखो तो!"

class MainApp(App):
    def build(self):
        return BrykanHorrorApp()

if __name__ == '__main__':
    MainApp().run()
