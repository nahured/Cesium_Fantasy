

function load_traslate(lang,ns){
    return fetch(window.base_url+"modules/translations/locales/"+lang+"/"+ns+".json").then(res =>{
        if (!res.ok){
            throw new Error("no se encontro la traduccion de",lang," ",ns)
        }
        return res.json()
    }).catch(()=>{
        console.log("no se encontro la traduccion de",lang," ",ns)
        return fetch(window.base_url+"modules/translations/locales/es/"+ns+".json").then(res => res.json())
    })
}


const lang_json_name_space = ["menu","get_tile","project_settings"]

async function get_langs(langs){
    let resources = {}
    for (const lang of langs){
        resources[lang] = {}
        for (const ns of lang_json_name_space){
            const translation = await load_traslate(lang, ns)
            resources[lang][ns] = translation
        }
    }
    return resources
}

export async function translation_init(){
    await i18next.init({
        lng: 'es',
        ns:lang_json_name_space,
        defaultNS: lang_json_name_space[0],
        resources: await get_langs(["es"])
    });
}

export function translation_test(){
    console.log("esto un ",i18next.t('bienvenida')," de i18next"); // "Hola mundo"
}

export function apply_translations() {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n')
        el.textContent = i18next.t(key)
    })
}