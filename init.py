from ui import Ui
import os

global home
home = os.getcwd()
if os.path.isdir(home + '/content') is False:
    os.mkdir(home+'/content')

ui = Ui() 