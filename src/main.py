from lib.tmos.tmos import OS
from lib.tmos.tmos_ui import StaticPage, WindowManager, to_screen
from lib.tmos.tmos_apps import App, AppManager

os = OS(layers=1)
wm = WindowManager(os, systray_visible=True)
apps = AppManager(wm)


class SimplePage(StaticPage):
    """
    A simple page with a message and an optional custom color.
    """

    def __init__(self, title: str, text: str, bg=None):
        super().__init__()
        self.title = title
        self.text = text
        self.bg = bg

    def _draw(self, display: "PicoGraphics", region: "Region", theme: "Theme"):
        display.set_pen(self.bg or theme.background_pen)
        display.rectangle(*region)
        display.set_pen(theme.foreground_pen)
        theme.text(display, self.text, *to_screen(region, theme.padding, theme.padding))


class ColorsApp(App):

    YELLOW = wm.display.create_pen(255, 255, 100)
    RED = wm.display.create_pen(255, 100, 100)

    name = "Colors"

    def pages(self):
        return [
            SimplePage("Yellow", "Like a lemon", self.YELLOW),
            SimplePage("Red", "Like a thing that is red", self.RED),
        ]


class AnimalsApp(App):

    name = "Animals"

    def pages(self):
        return [
            SimplePage("Cat", "Cats are why the internet exists."),
            SimplePage("Mouse", "Mice are small."),
            SimplePage("Duck", "quaaaack."),
        ]


apps.add_app(ColorsApp(), make_current=True)
apps.add_app(AnimalsApp())

os.boot(run=True)