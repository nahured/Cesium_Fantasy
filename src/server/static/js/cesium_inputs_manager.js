

function get_mouse_scene_position(){
    try{
        const response = fetch('/api/mouse/click',{
            method:'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                x:135,
                y:92,
                z:298
            })
        })
    } catch (err) {
        console.error("Error de conexión:", err);
    }
}