window.base_url = window.location.href.substring(0, window.location.href.lastIndexOf('/') + 1)

const {create_viewer} = await import(window.base_url+"modules/cesium/construct.js") 
const {create_tool_bar} = await import(window.base_url+"modules/tool_bar/construct.js") 



window.resource_manager = {}



function make_cesium_container() {
    const cesium_div = document.createElement("div");
    cesium_div.id = "cesiumContainer";
    cesium_div.className = "cesium-container";
    document.body.appendChild(cesium_div);            // ← lo agregamos al body
}


function main(){
    make_cesium_container()
    create_viewer("clear")
    create_tool_bar()
}

main();