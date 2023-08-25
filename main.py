import urwid
import urwid.raw_display
from urwid import Button


def exit_program(button):
    # pass
    raise urwid.ExitMainLoop()


def new_string(button):
    pass


def save_string(button):
    pass


class MyApp:
    def __init__(self):
        # Создаем виджеты окон с рамками

        self.top_left = urwid.LineBox(
            urwid.Filler(urwid.Text("Top Left Window")), title="Top Left"
        )
        self.top_right = urwid.LineBox(
            urwid.Filler(urwid.Text("Top Right Window")), title="Top Right"
        )

        self.middle_window = urwid.LineBox(
            urwid.Filler(urwid.Text("Middle Window")), title="Middle"
        )
        self.button_1 = urwid.Button("Button 1")
        self.button_2 = urwid.Button("Button 2")
        self.button_3 = urwid.Button("Button 3")
        self.button_4 = urwid.Button("Button 4")

        self.middle_left = urwid.Pile(
            [
                ("weight", 2, self.middle_window),
            ]
        )

        self.middle_right = urwid.Pile(
            [
                ("pack", self.button_1),
                ("pack", self.button_2),
                ("pack", self.button_3),
                ("pack", self.button_4),
            ]
        )

        self.bottom_window = urwid.LineBox(
            urwid.Filler(urwid.Text("Bottom Window")), title="Bottom"
        )
        self.button_5 = urwid.Button("Button 5")
        self.button_6 =urwid.Button("Button 6")

        self.bottom_left = urwid.Pile(
            [
                ("weight", 2, self.bottom_window),
            ]
        )

        self.bottom_right = urwid.Pile(
            [
                ("pack", self.button_5),
                ("pack", self.button_6),
            ]
        )

        ##last_window = urwid.LineBox(urwid.Filler(urwid.Text("Last Window")), title="Last")
        # Добавляем 3 кнопки в одной строке в "Last Window"

        self.quit_button = urwid.Button("New")
        self.save_button = urwid.Button("Save")
        self.new_button = urwid.Button("Exit")

        urwid.connect_signal(self.quit_button, "click", exit_program)
        urwid.connect_signal(self.save_button, "click", save_string)
        urwid.connect_signal(self.new_button, "click", new_string)

        self.last_buttons = urwid.Columns(
            [
                ("weight", 1, (self.quit_button)),
                ("weight", 1, (self.save_button)),
                ("weight", 1, (self.new_button)),
            ]
        )

        # Создаем горизонтальные панели для верхних окон
        self.top_cols = urwid.Columns(
            [
                ("weight", 2, self.top_left),
                ("weight", 1, self.top_right),
            ]
        )

        # Создаем вертикальную панель для всех частей
        self.main_pile = urwid.Pile(
            [
                ("weight", 1, self.top_cols),
                (
                    "weight",
                    4,
                    urwid.Columns(
                        [
                            ("weight", 3, self.middle_left),
                            ("weight", 1, self.middle_right),
                        ]
                    ),
                ),
                urwid.Columns(
                    [
                        ("weight", 3, self.bottom_left),
                        ("weight", 1, self.bottom_right),
                    ]
                ),
                ("pack", self.last_buttons),
            ]
        )

        # Создаем виджет рамки для всей композиции
        self.main_frame = urwid.Frame(self.main_pile, header=urwid.Text("Console note"))

    def run(self):
        palette = [
            ("body", "default", "default"),
            ("button", "black", "light gray", "standout"),
        ]
        # Создаем главный цикл urwid
        loop = urwid.MainLoop(self.main_frame, unhandled_input=exit_program)

        # Запускаем главный цикл
        loop.run()


if __name__ == "__main__":
    app = MyApp()
    app.run()
