import certifi
import requests
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from mydatabase import Database
from login import Login

from styles import Styles

Builder.load_string("""
#: import CButton custom_widget
#: import CTextInput custom_widget
<Home>:
    name: "Home"
    FloatLayout:
        Image:
            source: "background.jpg"
            opacity: 0.3
            fit_mode: "contain"
            pos_hint: {"center_x": 0.5, "top":1.2}
            
        
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                canvas.before:
                    Color:
                        rgba: root.bg_color
                    Rectangle:
                        pos: self.pos
                        size: self.size
                size_hint_y:None
                height: dp(60)
                Label:
                    text: "Interesting Fact"
                    font_name: "robotoblack.ttf"
                    font_size: '20sp'
                    
                 
                
                AnchorLayout:
                    anchor_x: "right"
                    padding: 10
                    Button:
                        canvas.before:
                            Rectangle:
                                pos: self.pos
                                size: self.size
                                source: "pngegg.png"
                                
                        
                        size_hint: None, None
                        size: dp(35), dp(35)
                        
                        background_normal: ""
                        background_color: 0,0,0,0
                        on_press: root.switchToHistory()
                
            BoxLayout:
                orientation: "vertical"
                Label:
                    text_size: self.width, None
                    font_size: 24
                    id: display
                    padding: [dp(20), dp(20)]
                    color: 0,0,0,1
                    pos_hint: {"center_x": 0.5, "top":0.9}
                Label:
                    text_size: self.width, None
                    font_size: 24
                    id: display_hun
                    padding: [dp(20), dp(20)]
                    color: 0,0,0,1
                    pos_hint: {"center_x": 0.5, "top":0.5}
            AnchorLayout:
                anchor_x: "center"
                anchor_y: "center"
                size_hint: 1, 0.30
            
                BoxLayout:
                    orientation: "vertical"
                    height: self.minimum_height
                    size_hint_y: None
                    padding: 30
                    spacing: dp(10)
                    BoxLayout:
                        size_hint: 1, 0.65
                        spacing: 5
                        BoxLayout:
                            orientation: "vertical"
                            spacing: dp(10)
                            Label:
                                
                                text: "Day"
                                color: 0,0,0,1
                                size_hint_y:None
                                size: self. texture_size
                                font_name: "robotomedium.ttf"
                                font_size: "18sp"
                                halign: "left"
                                text_size: self.size
                                
                            CTextInput:
                                id: day
                                size_hint_y: None
                                height: dp(50)
                            
                        BoxLayout:
                            orientation: "vertical"
                            spacing: 15
                            Label:
                                
                                text: "Month"
                                color: 0,0,0,1
                                size_hint_y:None
                                size: self. texture_size
                                font_name: "robotomedium.ttf"
                                font_size: "18sp"
                                halign: "left"
                                text_size: self.size
                            CTextInput:
                                id: month
                                size_hint_y: None
                                height: dp(50)
                            
                    CButton:
                        
                        text: "Display Fact"
                        font_name: "robotomedium.ttf"
                        font_size: '18sp'
                        height: dp(60)
                        size_hint_y:None
                        on_press: root.getFact()
                    
          

""")

class Home(Screen):
    bg_color=Styles.primary_color

    def response(self, req_body, result):
        self.ids.display.text = result
        Database.insertFact(Login.getEmail(), result)

        url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

        payload = {
            "from": "en",
            "to": "hu",
            "q": f"{result}"
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "7b4d07df1cmsh77019569982fc6ap13e9acjsn8d76474b4a78",
            "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        self.ids.display_hun.text = str(response.json())

    def getFact(self):
        day = self.ids.day.text
        month = self.ids.month.text
        url = f"https://numbersapi.p.rapidapi.com/{month}/{day}/date"

        headers = {
            "X-RapidAPI-Key": "7b4d07df1cmsh77019569982fc6ap13e9acjsn8d76474b4a78",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
        }

        UrlRequest(url, req_headers=headers, on_success=self.response, ca_file=certifi.where(), verify=True)

    def switchToHistory(self):
        self.manager.current="History"
