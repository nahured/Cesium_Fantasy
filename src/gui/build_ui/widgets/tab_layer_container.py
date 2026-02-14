import src.gui.modules.widgets.tab_layer_container as tab_layer_container

class TabLayer(tab_layer_container.TabLayer):
    """
    esta clase de se utilizara para manejar la interfaz de las capas
    """

    def button_add_OnButtonClick( self, event ):
        """
        esta funcion se llamara cuando se queira añadir una nueva capa
        """
        print("añadir")
        event.Skip()

    def button_edit_OnButtonClick( self, event ):
        """
        esta funcion se llamara cuando se queira editar una capa
        """
        print("editar")
        event.Skip()

    def buton_delete_OnButtonClick( self, event ):
        """
        esta funcion se llamara cuando se quiera eliminar una capa
        """
        print("eliminar")
        event.Skip()
