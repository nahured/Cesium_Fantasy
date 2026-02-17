var click_event_type = "None";

const handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas);

function send_data(to, data) {
    console.log("Enviando a:", to, "→", data); // mejor que alert para debug
    fetch(to, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: data }) // más claro
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Respuesta no OK: " + response.status);
        }
        return response.json(); // si esperas JSON de vuelta
    })
    .then(result => {
        console.log("Respuesta del servidor:", result);
    })
    .catch(err => {
        console.error("Error al enviar:", err);
        alert("Error de conexión: " + err.message);
    });
}

function get_mouse_world_location() {
    click_event_type = "world_position";
}


function click_event(movement) {
    let data = null;
    if (click_event_type === "None") {
        const picked = viewer.scene.pick(movement.position);
        if (picked) {
            data = {
                type: "entity",
                id: picked.id ? picked.id : "sin id",
                primitive: !!picked.primitive
            };
        } else {
            data = "None";
        }
    } 
    else if (click_event_type === "world_position") {
        const cartesian = viewer.scene.pickPosition(movement.position);
        if (cartesian) {
            const cartographic = Cesium.Cartographic.fromCartesian(cartesian);
            data = {
                cartesian3:cartesian,
                cartographic:cartographic,
                degrees:{
                    longitude: Cesium.Math.toDegrees(cartographic.longitude),
                    latitude: Cesium.Math.toDegrees(cartographic.latitude)
                },
                height: cartographic.height
            };
        } else {
            data = "no hay posición 3D (probablemente fuera del globo)";
        }
    } 
    else {
        data = "None";
    }

    // Siempre enviamos algo
    send_data('/api/mouse/click', data);

    // Reseteamos (puedes comentarlo si quieres mantener el modo)
    click_event_type = "None";
}

// ¡Aquí está la línea que no funcionaba bien!
handler.setInputAction(click_event, Cesium.ScreenSpaceEventType.LEFT_CLICK);


// DECORACIONES

function set_tile_rect(x1,x2,x3,x4){
    const entity = viewer.entities.getById('mi-rectangulo-unico')
    if (entity) {
        entity.rectangle.coordinates = Cesium.Rectangle.fromDegrees(x1,x2,x3,x4)
    } else {
        const redRectangle = viewer.entities.add({
            id: 'mi-rectangulo-unico',
            name: 'el grid contenedor de los tiles',
            rectangle: {
            // Definimos los límites: [Oeste, Sur, Este, Norte] en grados
            coordinates: Cesium.Rectangle.fromDegrees(x1,x2,x3,x4),
            material: Cesium.Color.RED.withAlpha(0.5),
            outline: true,
            outlineColor: Cesium.Color.BLACK,
            height: 0 // Altura sobre el nivel del mar
            },
        })
    }
};