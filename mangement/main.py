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

        def data_table_set(self):
            data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                        size_hint=(0.9, 0.6),
                                        check=True,
                                        rows_num=10,
                                        column_data=[
                                            ("No.", dp(18)),
                                            ("Food", dp(20)),
                                            ("Calories", dp(20))
                                        ],
                                        row_data=[
                                            ("1", "Burger", "300"),
                                            ("2", "Oats", "200"),
                                            ("3", "Oats", "200"),
                                            ("4", "Oats", "200"),
                                            ("5", "Oats", "200"),
                                            ("6", "Oats", "200"),
                                            ("7", "Oats", "200"),
                                            ("8", "Oats", "200")

                                        ]
                                        )
            data_table.bind(on_row_press=DemoApp.on_row_press)
            data_table.bind(on_check_press=DemoApp.on_check_press)
            

    
   


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

        
        

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        print(instance_table, current_row)
        


   



    


DemoApp().run()