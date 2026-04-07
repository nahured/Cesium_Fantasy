
function mod(a, b) {
    return ((a % b) + b) % b;
  }

export function get_grid(p1,p2,zoom){
    const level = 2**(zoom+1)
    const abs = mod((p1.x-p2.x),level)
    const distance = {
        "x":level-abs,
        "y":p1.y-p2.y
    }
    return distance
}

export function degreesToTile(long,lat,zoom) {
    const level = parseInt(zoom)
    const dat = {
        "x":get_tile_x(long,level),
        "y":get_tile_y(lat,level)
    }
    return dat
}

function get_tile_x(long,zoom){
    const level = 360/(2**(zoom+1))
    const absolute = Math.abs((long+180)/level)
    const x = Math.floor(absolute)
    return x
}

function get_tile_y(lat,zoom){
    const level = -180/(2**zoom)
    const absolute = Math.abs((lat-90)/level)
    const y = Math.floor(absolute)
    return y
}

