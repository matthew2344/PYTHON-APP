from kivy.app import App
from kivy.uix.button import Button

class FunkyButton(Button):
    def __init__(self, **kwargs):
        super(FunkyButton, self).__init__(**kwargs)
        self.text="Funky Button"
        self.post=(100,100)
        self.size_hint=(.5,.5)

class TestApp(App):
    def build(self):
        return FunkyButton()

if __name__ == '__main__':
    TestApp().run()