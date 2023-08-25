#!/usr/bin/python3
import urwid
import urwid.raw_display
from urwid import Button

def exit_program(button):
    raise urwid.ExitMainLoop()

if __name__ == "__main__":
    # Создаем виджеты окон с рамками
   
    top_left = urwid.LineBox(urwid.Filler(urwid.Text("Top Left Window")), title="Top Left")
    top_right = urwid.LineBox(urwid.Filler(urwid.Text("Top Right Window")), title="Top Right")
  
  ##  top_left = urwid.Pile([
  ##      (3,urwid.LineBox(urwid.Filler(urwid.Text("Tag")))),
  ##  ])
  ##  top_right = urwid.Pile([
  ##      (3,urwid.LineBox(urwid.Filler(urwid.Text("Radio")))),
  ##  ])
  
    middle_window = urwid.LineBox(urwid.Filler(urwid.Text("Middle Window")), title="Middle")
    button_1 = urwid.LineBox(urwid.Button(u"Button 1"))
    button_2 = urwid.LineBox(urwid.Button(u"Button 2"))
    button_3 = urwid.LineBox(urwid.Button(u"Button 3"))
    button_4 = urwid.LineBox(urwid.Button(u"Button 4"))
    
    middle_left = urwid.Pile([
        ('weight', 2, middle_window),
    ])

    middle_right = urwid.Pile([
        ('pack', button_1),
        ('pack', button_2),
        ('pack', button_3),
        ('pack', button_4),
    ])

    bottom_window = urwid.LineBox(urwid.Filler(urwid.Text("Bottom Window")), title="Bottom")
    button_5 = urwid.LineBox(urwid.Button(u"Button 5"))
    button_6 = urwid.LineBox(urwid.Button(u"Button 6"))

    bottom_left = urwid.Pile([
        ('weight', 2, bottom_window),
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

    bottom_right = urwid.Pile([
                ('weight', 1, button_5),
                ('weight', 1, button_6),
    ])
    bottom_right1 = urwid.Pile([
            #    ('weight', 1, button_5),
                ('weight', 1, button_6),
    ])
    # Создаем пустую часть "Last Window" под Bottom Window
    ##last_window = urwid.LineBox(urwid.Filler(urwid.Text("Last Window")), title="Last")

    # Добавляем четыре кнопки в одной строке в "Last Window"
    
    last_buttons = urwid.Columns([
        ('weight', 1, urwid.LineBox(urwid.Button(u"Button X"))),
        ('weight', 1, urwid.LineBox(urwid.Button(u"Button Y"))),
        ('weight', 1, urwid.LineBox(urwid.Button(u"Button Z"))),
     ##   ('weight', 1, urwid.LineBox(urwid.Button(u"Button W"))),
    ])

    # Создаем горизонтальные панели для верхних окон
    top_cols = urwid.Columns([
        ('weight', 2, top_left),
        ('weight', 1, top_right),
    ])

    # Создаем вертикальную панель для всех частей
    main_pile = urwid.Pile([
        ('weight', 1, top_cols),
        ('weight', 4, urwid.Columns([
            ('weight', 3, middle_left),
            ('weight', 1, middle_right),
        ])),
        urwid.Columns([
            ('weight', 3, bottom_left),
            ('weight', 1, bottom_right),
          #  ('weight', 1, bottom_right1),
          #  ('weight', 1,  button_5),
           # ('weight', 1,  button_6),
        ]),
    ##  ('weight', 1, last_window),
       ('pack', last_buttons),
    ])

    # Создаем виджет рамки для всей композиции
    main_frame = urwid.Frame(main_pile, header=urwid.Text("Console note"))

    # Создаем главный цикл urwid
    loop = urwid.MainLoop(main_frame, unhandled_input=exit_program)

    # Запускаем главный цикл
    loop.run()
