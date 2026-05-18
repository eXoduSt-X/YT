import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.utils import platform
import yt_dlp

class YTHome(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        from kivy.core.window import Window
        Window.clearcolor = (0.07, 0.07, 0.07, 1)

        # ---- BARRA SUPERIOR ----
        top_bar = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height='60dp',
            padding=['12dp', '8dp', '12dp', '8dp'],
            spacing='8dp'
        )
        
        self.btn_paste = Button(
            text='📋', 
            size_hint_x=None, 
            width='45dp',
            background_color=(0.15, 0.15, 0.15, 1)
        )
        self.btn_paste.bind(on_press=self.pegar_link)
        
        self.btn_settings = Button(
            text='🎛️', 
            size_hint_x=None, 
            width='45dp',
            background_color=(0.15, 0.15, 0.15, 1)
        )

        self.et_link = TextInput(
            text='',
            hint_text='Pega el link aquí...',
            hint_text_color=(0.4, 0.4, 0.4, 1),
            foreground_color=(1, 1, 1, 1),
            background_color=(0.1, 0.1, 0.1, 1),
            multiline=False,
            padding=['10dp', '10dp', '10dp', '10dp']
        )

        self.btn_download = Button(
            text='📥', 
            size_hint_x=None, 
            width='45dp',
            background_color=(0.15, 0.15, 0.15, 1)
        )
        self.btn_download.bind(on_press=self.iniciar_descarga_hilo)

        top_bar.add_widget(self.btn_paste)
        top_bar.add_widget(self.btn_settings)
        top_bar.add_widget(self.et_link)
        top_bar.add_widget(self.btn_download)

        self.add_widget(top_bar)
        self.add_widget(BoxLayout(size_hint_y=1))

    def pegar_link(self, instance):
        texto = Clipboard.paste()
        if texto:
            self.et_link.text = texto

    def iniciar_descarga_hilo(self, instance):
        url = self.et_link.text.strip()
        if not url:
            return
        threading.Thread(target=self.descargar_video, args=(url,), daemon=True).start()

    def descargar_video(self, url):
        if platform == 'android':
            from android.storage import get_downloads_dir
            ruta_guardado = os.path.join(get_downloads_dir(), 'YT_%(title)s.%(ext)s')
        else:
            ruta_guardado = 'YT_%(title)s.%(ext)s'

        ydl_opts = {
            'outtmpl': ruta_guardado,
            'format': 'best', 
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.et_link.text = ""
        except Exception as e:
            print(f"Error al descargar: {e}")

class YTApp(App):
    def build(self):
        self.title = "YT"
        return YTHome()

if __name__ == '__main__':
    YTApp().run()
