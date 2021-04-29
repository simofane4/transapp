from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.list import MDList,OneLineIconListItem
from kivymd.theming import ThemableBehavior 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.datatables import MDDataTable


class LoginScreen(Screen):
    pass
    



class StockScreen(Screen):
    pass
   


class UploadScreen(Screen):
    pass
class ContentNavigationDrawer(BoxLayout):
    pass




class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))






# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(StockScreen(name='stock'))
sm.add_widget(UploadScreen(name='upload'))






class DemoApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        
        super().__init__(**kwargs)


    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_file('main.kv')
        return screen

        
        


        


   



    def shek_user(self, email, password):
        if email == "simo@simo.com" and password == "123456":
            self.manager.current = 'profile'


DemoApp().run()