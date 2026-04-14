const {float_menu} = await import(window.base_url+"modules/float_menu/float_menu_construct.js") 


export class ProjectSettings extends float_menu {
    constructor() {
        super({
          menu_title: "project_settings_title",
          html: "resources/html/popups/project_settings.html",
          css:"resources/html/popups/project_settings.css",
          size: { width: "600px", height: "300px" }
        });
        this.p1;
        this.p2;
    }

    set_logic(){
        this.set_tabs()
        this.set_buttons()
        this.set_new_project()
    }

    set_new_project(){
        // botones
        const div = document.getElementById("project_settings_div")
        const button_make_folder = document.getElementById("get_project_folder")
        const button_save = document.getElementById("new_project_save")
        const folder_label = document.getElementById("folder_label")
        button_make_folder.addEventListener("click",async () => {
            const path = await pywebview.api.file_dialog_api.open_folder_dialog()
            folder_label.value = path
            
        })
        button_save.addEventListener("click",async ()=>{
            const form = document.getElementById("new_project_form")
            const obj = new FormData(form)
            const data = Object.fromEntries(obj)
            console.log("data 1 ",data)
            console.log("data ",JSON.stringify(data))
        })
    }

    set_buttons(){
        const load_project_button = document.getElementById("load_project")
        load_project_button.addEventListener("click", async () => {
            console.log("cargar ")
            const path = await pywebview.api.file_dialog_api.open_folder_dialog()
            const list = await pywebview.api.project.load_project(path)
            console.log("lista = ",list)
        } )
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