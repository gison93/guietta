# -*- coding: utf-8 -*-

from guietta import B, E, _, Gui, Quit

def do_eval(gui):
    try:
        result = eval(gui.expr.text())
        gui.result.setText(str(result))
    except Exception as e:
        gui.result.setText('Error: '+str(e))

gui = Gui(
    
  [  'Enter expression:', E('expr')  , _ ],
  [  'Result:'          , 'result'    , _          ],
  [  _                  , _           , Quit       ] )


gui.events(
    
    [  _            ,   ('textEdited', do_eval) , _    ], 
    [  _            ,   _                       , _    ], 
    [  _            ,   _                       , _    ], )


gui.run()

# GUI widgets are available after window closing,
print(gui.result.text())

    