# >--------------- DECLARACIONES ---------------<
import src.gui.modules.main as main

from pubsub import pub

class Windows(main.Windows):
    def __init__(self, parent):
        super().__init__(parent)
        pub.sendMessage('ui-finish')
    pass