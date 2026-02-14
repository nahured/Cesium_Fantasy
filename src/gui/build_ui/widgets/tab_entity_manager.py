import src.gui.modules.widgets.tab_entity_manager as tab_entity_manager

class EntityManager(tab_entity_manager.EntityManager):

    def button_new_OnButtonClick(self, event):
        return super().button_new_OnButtonClick(event)
    
    def tree_entity_OnTreeItemActived(self, event):
        print(f"se selecciono {event:=}")
        return super().tree_entity_OnTreeItemActived(event)

