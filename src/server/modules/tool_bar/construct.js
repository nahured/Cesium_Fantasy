

const {GetTile} = await import(window.base_url+"modules/tool_bar/menus/get_tiles.js") 
const {ProjectSettings} = await import(window.base_url+"modules/tool_bar/menus/project_settings.js") 
const {get_svg_path} = await import(window.base_url+"modules/resources/sgv.js") 

export async function create_tool_bar(){
    const tool_bar_base = document.createElement("div")
    tool_bar_base.id = "tool-bar-base"
    tool_bar_base.className = "tool-bar-base"
    document.body.appendChild(tool_bar_base)
    const title_div = await add_title()
    tool_bar_base.appendChild(title_div)
    const button_ul = document.createElement("ul")
    button_ul.id = "tool-bar-button-list"
    button_ul.className = "tool-bar-button-list"
    tool_bar_base.appendChild(button_ul)
    create_buttons(button_ul)
}

async function add_title(){
    const title_div = document.createElement("div")
    title_div.id = "tool-bar-title"
    title_div.className = "tool-bar-title"
    const title_icon = await get_svg_path("planet-outline","title-icon")
    title_div.appendChild(title_icon)
    title_div.addEventListener("click",() => {
        const tool_bar = document.getElementById("tool-bar-base")
        const button_ul = document.getElementById("tool-bar-button-list")
        tool_bar.classList.toggle('close')
        title_icon.classList.toggle("close")
        button_ul.classList.toggle("close")
    })
    return title_div
}

async function create_buttons(father){
    const _butons = [
        await new_a("extraer_tile","copy-outline",()=> {new GetTile().build()}), 
        await new_a("project settings","create-outline",()=> {new ProjectSettings().build()}),
        await new_a("tercero","copy-outline",()=> {alert("funciona el tercero")}),
        await new_a("cuarto","copy-outline",()=> {alert("funciona el cuarto")}),
    ]
    for (const li of _butons) {
        father.appendChild(li)
    }
}

async function new_a(text,icon,callable) {
    const li = document.createElement("li")
    li.className = "tool-bar-button-li"
    const button = document.createElement("span")
    button.id = "tool-bar-span"
    button.className = "tool-bar-span"
    li.addEventListener("click",callable)
    const button_icon = await get_svg_path(icon,"button-icon")
    const span = document.createElement("span")
    span.textContent = text
    button.appendChild(button_icon)
    button.appendChild(span)
    li.appendChild(button)
    return li
}