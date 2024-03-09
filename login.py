from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from mydatabase import Database
from styles import Styles

Builder.load_string("""
#: import CButton custom_widget
#: import CTextInput custom_widget
#: import SignupText custom_widget

<Login>:
    name: "Login"
    BoxLayout:
        padding: 10
        orientation: "vertical"
        BoxLayout:
            size_hint: 1, 0.35
            Image:
                source: "background.jpg"
        
        AnchorLayout:
            size_hint: 1, 0.55
            anchor_y: "top"
        
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                padding: dp(30)
                
                
                Label:
                    text: "Login to your Account"
                    font_size: "16sp"
                    halign: "left"
                    font_name: "robotoblack.ttf"
                    text_size: self.size
                    size_hint_y:None
                    size: self.texture_size
                    color: root.secondary_color
                
                CTextInput:
                    id: email
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "E-mail"
                    
                CTextInput:
                    id: password
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "Password"
                CButton:
                    text: "Login"
                    size_hint_y: None
                    height: dp(50)
                    on_press: root.login()
                    
        
        AnchorLayout:
            size_hint: 1, 0.1
            anchor_x: "center"
                              
           
            BoxLayout:
                size_hint_x: None
                width: self.minimum_width
                
                Label:
                    text: "Don't have an account? "
                    color: root.secondary_color
                    size_hint_x: None
                    size: self.texture_size
                    
                    
                SignupText:
                    text: "Signup"
                    size_hint_x: None
                    size: self.texture_size
                    on_press: root.switchToSignup()
                    
              

""")
class Login(Screen):
    secondary_color=Styles.secondary_color
    email=None
    @staticmethod
    def getEmail():
        return Login.email


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.email.text="takacs-g@outlook.hu"
        self.ids.password.text="takacsg"

    def login(self):
        Login.email=self.ids.email.text
        password=self.ids.password.text
        if(Database.isExist(Login.email,password)):
            self.manager.current="Home"
        else:
            print("Login Failed!")
    def switchToSignup(self):
        self.manager.current="signup"
