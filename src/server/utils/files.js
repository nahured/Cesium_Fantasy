const {range} = await import(window.base_url+"utils/math.js")

export function get_images_gmatrix(dir_map,coord){
    const rangex =range(0,coord.distance.x,1)
    const rangey =range(0,coord.distance.y,1)
    console.log("coord ",coord," x ",rangex," y ",rangey)
    const limit = 2**(coord.zoom+1)
    for (const x of rangex){
        for (const y of rangey) {
            console.log(window.base_url+"data/"+dir_map+"/"+coord.zoom+"/"+((coord.point.x+x)%limit)+"/"+(coord.point.y+y))
        }
        console.log("-----")
    }
    console.log("no pasa nada",dir_map,coord)
}