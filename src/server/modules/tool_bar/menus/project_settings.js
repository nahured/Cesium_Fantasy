const {float_menu} = await import(window.base_url+"modules/float_menu/float_menu_construct.js") 


export class ProjectSettings extends float_menu {
    constructor() {
        super({
          menu_title: "project_settings_title",
          html: "resources/html/popups/project_settings.html",
          css:"resources/html/popups/project_settings.css",
          size: { width: "300px", height: "300px" }
        });
        this.p1;
        this.p2;
    }

    set_logic(){
        this.set_tabs()
    }

    set_tabs(){
        const tab_contend = document.getElementById("project_settings_tab_nav")

        for (const i of Array.from(tab_contend.children)){
            i.addEventListener("click",()=>{ this.switchTab(i,i.id)})
        }
    }

    switchTab(btn, tabId) {
        const tab_contend = document.getElementById("project_settings_tab_nav")
        const div_config = document.getElementById("project_settings_div")
        // Desactivar todos los botones y ocultar todos los contenidos
        tab_contend.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.style.display = 'none');
      
        // Activar el seleccionado
        btn.classList.add('active');
        document.getElementById('tab-' + tabId).style.display = 'block';
      }
}