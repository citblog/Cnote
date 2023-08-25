import urwid
import urwid.raw_display
from urwid import Button

def exit_program(button):
    #pass
    raise urwid.ExitMainLoop()
def new_string(button):
    pass
def save_string(button):
    pass



class MyApp:
    def __init__(self):
        # Создаем виджеты окон с рамками
   
        self.top_left = urwid.LineBox(urwid.Filler(urwid.Text("Top Left Window")), title="Top Left")
        self.top_right = urwid.LineBox(urwid.Filler(urwid.Text("Top Right Window")), title="Top Right")
  
  ##  top_left = urwid.Pile([
  ##      (3,urwid.LineBox(urwid.Filler(urwid.Text("Tag")))),
  ##  ])
  ##  top_right = urwid.Pile([
  ##      (3,urwid.LineBox(urwid.Filler(urwid.Text("Radio")))),
  ##  ])
  
        self.middle_window = urwid.LineBox(urwid.Filler(urwid.Text("Middle Window")), title="Middle")
        self.button_1 = urwid.LineBox(urwid.Button(u"Button 1"))
        self.button_2 = urwid.LineBox(urwid.Button(u"Button 2"))
        self.button_3 = urwid.LineBox(urwid.Button(u"Button 3"))
        self.button_4 = urwid.LineBox(urwid.Button(u"Button 4"))
    
        self.middle_left = urwid.Pile([
            ('weight', 2, self.middle_window),
            ])

        self.middle_right = urwid.Pile([
            ('pack', self.button_1),
            ('pack', self.button_2),
            ('pack', self.button_3),
            ('pack', self.button_4),
            ])

        self.bottom_window = urwid.LineBox(urwid.Filler(urwid.Text("Bottom Window")), title="Bottom")
        self.button_5 = urwid.LineBox(urwid.Button(u"Button 5"))
        self.button_6 = urwid.LineBox(urwid.Button(u"Button 6"))

        self.bottom_left = urwid.Pile([
            ('weight', 2, self.bottom_window),
        ])

  #  bottom_right = urwid.Pile([
  #      urwid.Columns([
  #          ('weight', 1, urwid.Pile([
  #              ('weight', 1, button_5),
   #             ('weight', 1, button_6),
  #         ])),
   #   #      ('weight', 1, urwid.Filler(urwid.Text(""))),
      #      ('weight', 1, urwid.LineBox(urwid.Button(u"Button 7"))),
  #      ]),
  #  ]) 

        self.bottom_right = urwid.Pile([
                ('weight', 1, self.button_5),
                ('weight', 1, self.button_6),
            ])
        self.bottom_right1 = urwid.Pile([
            #    ('weight', 1, self.button_5),
                ('weight', 1, self.button_6),
             ])
    # Создаем пустую часть "Last Window" под Bottom Window
    ##last_window = urwid.LineBox(urwid.Filler(urwid.Text("Last Window")), title="Last")

    # Добавляем четыре кнопки в одной строке в "Last Window"
        self.quit_button = urwid.Button(u"New")
        self.save_button = urwid.Button(u"Save")
        self.new_button = urwid.Button(u"Exit")
                
        urwid.connect_signal(self.quit_button, 'click', exit_program)
        urwid.connect_signal(self.save_button, 'click', save_string)
        urwid.connect_signal(self.new_button, 'click', new_string)
        
        self.last_buttons = urwid.Columns([
            ('weight', 1,urwid.LineBox(self.quit_button )),
            ('weight', 1, urwid.LineBox(self.save_button)),
            ('weight', 1, urwid.LineBox(self.new_button)),
             ])

    # Создаем горизонтальные панели для верхних окон
        self.top_cols = urwid.Columns([
            ('weight', 2, self.top_left),
            ('weight', 1, self.top_right),
            ])

    # Создаем вертикальную панель для всех частей
        self.main_pile = urwid.Pile([
           ('weight', 1, self.top_cols),
            ('weight', 4, urwid.Columns([
            ('weight', 3, self.middle_left),
            ('weight', 1, self.middle_right),
        ])),
        urwid.Columns([
            ('weight', 3, self.bottom_left),
            ('weight', 1, self.bottom_right),
          #  ('weight', 1, bottom_right1),
          #  ('weight', 1,  button_5),
           # ('weight', 1,  button_6),
            ]),
    ##  ('weight', 1, last_window),
            ('pack', self.last_buttons),
         ])

    # Создаем виджет рамки для всей композиции
        self.main_frame = urwid.Frame(self.main_pile, header=urwid.Text("Console note"))


    def run(self):
        palette = [
            ('body', 'default', 'default'),
            ('button', 'black', 'light gray', 'standout'),
        ]
          # Создаем главный цикл urwid
        loop = urwid.MainLoop(self.main_frame, unhandled_input=exit_program)

    # Запускаем главный цикл
        loop.run()

if __name__ == "__main__":
    app = MyApp()
    app.run()
