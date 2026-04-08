


export class float_menu{
    constructor(options){
        this.float_menu_body = document.createElement("div");
        this.menu_title = options.menu_title;
        this.html = options.html;
        this.css = options.css;
        this.size = options.size;
        this.menu_body = document.createElement('div');
    }

    async load_css(){
        const url = window.base_url+this.css
        if (this.css){
            if (document.querySelector(`link[href="${url}"]`)) return;
            const link = document.createElement("link");
            link.rel = "stylesheet";
            link.href = url;
            document.head.appendChild(link);
        }
    }

    async load_html() {
        const res = await fetch(window.base_url+this.html)
        const html = await res.text()
        this.menu_body.innerHTML = html
    }

    set_logic(){}

    async get_elements() {
        await this.load_html()
        this.load_css()
        //const cesium_container = document.getElementById("cesiumContainer")
        this.float_menu_body.id = "float-menu-container"
        this.float_menu_body.className = "float-menu-container"
        this.menu_body.className = "float-menu-body-container"
        this.float_menu_body.appendChild(this.make_options_menu())
        this.float_menu_body.appendChild(this.menu_body)
        
        this.float_menu_body.style.width = this.size.width
        this.float_menu_body.style.height = this.size.height
        
        document.body.appendChild(this.float_menu_body)
        //cesium_container.
    }

    make_options_menu(){
        const menu_div = document.createElement("div")
        menu_div.className = "float-menu-container-buttons"
        const title = document.createElement("h2")
        title.textContent = this.menu_title
        title.className = "float-menu-container-buttons-title"
        menu_div.appendChild(title)
        
        menu_div.addEventListener("mousedown", (e) => {
            // getBoundingClientRect() da la posición real en pantalla
            const rect = this.float_menu_body.getBoundingClientRect();
            const shiftX = e.clientX - rect.left;
            const shiftY = e.clientY - rect.top;
        
            const mover = (e) => {
                this.move_float_menu(e, shiftX, shiftY);
            };
        
            document.addEventListener('mousemove', mover);
        
            document.addEventListener("mouseup", () => {
                document.removeEventListener('mousemove', mover);
            }, { once: true });
        });
        const button_delete = document.createElement("button")
        button_delete.textContent = "X"
        button_delete.className = "float-menu-container-buttons-delete"
        this.add_click(button_delete,() => {
            this.float_menu_body.remove()
            const index = window.pupup_menu.indexOf(this.menu_title)
            window.pupup_menu.splice(index,1)
        })
        menu_div.appendChild(button_delete)

        return menu_div
    }

    move_float_menu(e, shiftX, shiftY) {
        this.float_menu_body.style.left = e.clientX - shiftX + "px";
        this.float_menu_body.style.top  = e.clientY - shiftY + "px";
    }

    add_click(element,funcion){
        element.addEventListener("click",funcion)
    }

    async build() {
        await this.get_elements()
        this.set_logic() // la logica se tiene que cargar al final
        return this
    }
}