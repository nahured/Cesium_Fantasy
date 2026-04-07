
export function mod(a, b) {
    return ((a % b) + b) % b;
  }

export function get_grid(p1,p2,zoom){
    const level = 2**(zoom+1)
    const abs = mod((p1.x-p2.x),level)
    const distance = {
        distance:{
            x:level-abs,
            y:(p1.y-p2.y)*-1
        },
        point:{
            x:p1.x,
            y:p1.y
        },
        zoom:zoom
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

export function range(start, end, step = 1) {
    // Si solo se pasa un argumento → range(end) → empieza desde 0
    if (end === undefined) {
        end = start;
        start = 0;
    }

    const result = [];

    if (step === 0) {
        throw new Error("El step no puede ser 0");
    }

    // Determinar la dirección correcta
    const isIncreasing = end > 0;

    if (isIncreasing) {
        end = end+1
        for (let i = start; i < end; i += step) {
            result.push(i);
        }
    } else {
        end = end-1
        for (let i = start; i > end; i -= step) {
            result.push(i);
        }
    }

    return result;
}