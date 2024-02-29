from flet import *
import flet as ft
import requests
from time import sleep
class ChatApp(UserControl):
    def __init__(self, page):
        super(ChatApp, self).__init__()
        self.page = page
        self.image_pick = FilePicker(on_result=self.getimage)
        self.page.overlay.append(self.image_pick)
        self.image_path = Text("")
        self.heading = ft.Text(value="\nTELEBOT", size=35, color="YELLOW", weight="BOLD")
        self.offgpt = ft.Text(value=" by justsimplifiedknowledge\n", size=16, color="WHITE", weight="BOLD")
        
        self.toekn = Container(
            padding=20,
            bgcolor="WHITE",
            content=Column([
                
                Row([
                    TextField(label="Enter your Telegram token here ", width=150, multiline=True),
                    ElevatedButton("add token",icon="TOKEN", on_click=self.tokenid)
                ]), 

            ])
        )

        self.chtid = Container(
            padding=20,
            bgcolor="WHITE",
            content=Column([
                
                Row([
                    TextField(label="Enter your Chat ID here", width=150, multiline=True),
                    ElevatedButton("add chat id", on_click=self.chtid)
                ]), 

            ])
        )
        
        page.add(self.heading, self.offgpt,self.toekn, self.chtid)

        page.add(
            ft.Text("After entering the Telegram TOKEN and Chat ID,\n you can add your image and message below:", color="ORANGE", ),
        )
        self.chat_box = Container(
            padding=10,
            bgcolor="WHITE",
            content=Column([
                
                Row([
                    TextField(label="Send message ", width=150, multiline=True),
                    ElevatedButton("send",icon="TELEGRAM", on_click=self.send_message)
                ]),
                ElevatedButton("add image", on_click=lambda e: self.image_pick.pick_files())

            ])
        )
        
    
    def chtid(self, e):
        chtid=self.chtid.content.controls[0].controls[0].value
        chat_id=chtid
        print(chtid)
    def tokenid(self, e):
        tokentext=self.toekn.content.controls[0].controls[0].value
        TOKEN=tokentext
        print(TOKEN)
    def getimage(self, e: FilePickerResultEvent):
        self.image_path.value = e.files[0].path
        self.update()

    def send_message(self, e):
        message_text = self.chat_box.content.controls[0].controls[0].value
        tokentext=self.toekn.content.controls[0].controls[0].value
        TOKEN=tokentext
        chtid=self.chtid.content.controls[0].controls[0].value
        chat_id=chtid


        send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        text_format = {"chat_id": chat_id, "text": message_text}
        text_response = requests.post(send_url, data=text_format)

        if self.image_path.value:
            send_photo_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
            with open(self.image_path.value, "rb") as image_file:
                files = {"photo": image_file}
                photo_data = {"chat_id": chat_id, "caption": message_text}
                photo_response = requests.post(send_photo_url, data=photo_data, files=files)

    def build(self):
        return Column([
            self.chat_box
        ])
    
def main(page: Page):
    page.scroll=True
    page.window_width = 300
    BG = '#041955'
    page.bgcolor = BG
    page.add(ChatApp(page))
    
    #website link
    promo =ft.Text("\nWant more advanced features? Visit our website now ", size=16, color="GREEN", weight="BOLD")
    def open_web(e):
          
          url = "https://justsimplifiedknowledge.com"
          page.launch_url(url)
    promobtn=ElevatedButton("justsimplifiedknowledge.com", icon="LINK", on_click=open_web, color="GREEN")
    
    #gmail id link 
    QUERY=ft.Text(value="\nFor any queries feel free to contact us at", color="WHITE", )
    gmail=ft.Text(value="justsimplifiedknowledge@gmail.com", color="RED")
    page.add(promo, promobtn, QUERY, gmail)
    

    def Botfather(e):
          
          url = "https://t.me/BotFather"
          page.launch_url(url)

    boterbtn=ft.ElevatedButton("BotFather Link",on_click=Botfather)

    def GETURCHATID(e):
          
          url = "https://t.me/GetMyChatID_Bot"
          page.launch_url(url)

    GETURCHATID=ft.ElevatedButton("GetMyChatID Link",on_click=GETURCHATID)

    def broadcastchannel(e):
          
          url = "https://whatsapp.com/channel/0029VaJATwcDeON1pUO17n1Z"
          page.launch_url(url)

    broadcastchannel=ft.ElevatedButton("Video",icon="VIDEOCAM",on_click=GETURCHATID)

    page.add(
    ft.Text(value="\nUsing Telebot: A Step-by-Step Guide", weight="BOLD", color="WHITE", size=20),
    
    ft.Text(value="\n1. Begin by visiting the Botfather Telegram Bot to obtain the Token ID. Enter the obtained Token ID in the Telegram Token Container.", color="WHITE"),
    boterbtn,
    
    ft.Text(value="\n2. Next, visit the GetMyChatID Telegram Bot to obtain the CHAT ID. Enter the obtained CHAT ID in the ChatID Container.", color="WHITE"),
    GETURCHATID,
    
    ft.Text(value="\n3. Once you have submitted the Telegram Token and ChatID, you are ready to send messages and images using your Telegram bot.", color="WHITE"),
    
    ft.Text(value="\n4. Select an image, add the desired text, and click the submit button. Your selected image and message will be sent within seconds.", color="WHITE"),
    
)
    
    
ft.app(target=main,assets_dir="assets", view=ft.WEB_BROWSER)