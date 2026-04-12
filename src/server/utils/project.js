const {ProviderImagery} = await import(window.base_url+"utils/global.js") 

window.project_config = {
    "lang":"es",
    "projects_paths":{
        "new":"path"
    },
    "default_project":"new"
}



export async function load_config() {
    const conf = await pywebview.api.project.get_config()
    if (validate_config_file(conf)){
        window.project_config = conf
    } else {
        save_config()
        alert(i18next.t("alert:config_file_no_valid"))
    }
}

export async function save_config() {
    if (validate_config_file(window.project_config)){
        pywebview.api.project.save_config(window.project_config)
    } else {
        alert(i18next.t("alert:config_objet_no_valid"))
    }
}

function validate_config_file(data){
    if (data) {
        console.log("load jaon")
        return true
    } else {
        console.log("no load jaon")
        return false
    }
}


export function new_map_layer_config(
    layer_name,
    icon_name,
    size_pixel,
    provider//:ProviderImagery,
){
    return {
        name:layer_name,
        icon:icon_name,
        size:size_pixel,
        provider:provider
    }
}

const world_project = {
    config:{
        program:{},
        cesium:{}
    },
    map_list:{}
}

