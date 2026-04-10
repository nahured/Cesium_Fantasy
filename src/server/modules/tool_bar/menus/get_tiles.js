const {float_menu} = await import(window.base_url+"modules/float_menu/float_menu_construct.js") 
const {degreesToTile,get_grid} = await import(window.base_url+"utils/math.js")
const {get_images_gmatrix} = await import(window.base_url+"utils/files.js")
// hola_mundo_menu.js

export class GetTile extends float_menu {

  constructor() {
    super({
      menu_title: i18next.t("get_tile:title"),
      html: "resources/html/popups/get_tile.html",
      css:"resources/html/popups/get_tile.css",
      size: { width: "300px", height: "150px" },
    });
    this.p1;
    this.p2;
  }

  set_logic(){
    this.set_max()
    this.set_button()
    this.set_buttons()
  }

  set_max(){
    this.level = document.getElementById("get_tile-level")
    this.p1x = document.getElementById("get_tile-point-1-x")
    this.p1y = document.getElementById("get_tile-point-1-y")
    this.p2x = document.getElementById("get_tile-point-2-x")
    this.p2y = document.getElementById("get_tile-point-2-y")

    this.level.addEventListener("input", (e) => {
      const level = parseInt(e.target.value)
      const x = `${(2**(level+1))-1}`
      const y = `${(2**(level))-1}`
      this.p1x.max = x
      this.p1y.max = y
      this.p2x.max = x
      this.p2y.max = y
      if (parseInt(this.p1x.value)>parseInt(this.p1x.max)){
        this.p1x.value = this.p1x.max
      }
      if (parseInt(this.p1y.value)>parseInt(this.p1y.max)){
        this.p1y.value = this.p1y.max
      }
      if (parseInt(this.p2x.value)>parseInt(this.p2x.max)){
        this.p2x.value = this.p2x.max
      }
      if (parseInt(this.p2y.value)>parseInt(this.p2y.max)){
        this.p2y.value = this.p2y.max
      }
    })
  }

  set_buttons(){
    const button = document.getElementById("get_tile_button")
    button.addEventListener("click",()=> {this.get_grid()})
  }

  get_grid(){
    const button_p1 = document.getElementById("button-point-1-get-tile")
    const button_p2 = document.getElementById("button-point-2-get-tile")
    const level = document.getElementById("get_tile-level")
    const p1 = {
      "x": parseInt(this.p1x.value),
      "y": parseInt(this.p1y.value)
    }
    const p2 = {
      "x": parseInt(this.p2x.value),
      "y": parseInt(this.p2y.value)
    }
    const grid = get_grid(p1,p2,parseInt(level.value))
    const a = get_images_gmatrix("mundo",grid)
    console.log("grid: ",grid)
    
  }

  set_button(){
    const button_p1 = document.getElementById("button-point-1-get-tile")
    button_p1.addEventListener("click",() =>{this.add_event_get_position("button-point-1-get-tile")})
    window.addEventListener("button-point-1-get-tile",(e)=>{this.set_tiles(this.p1x,this.p1y,e.detail,"button-point-1-get-tile")})
    const button_p2 = document.getElementById("button-point-2-get-tile")
    button_p2.addEventListener("click",() =>{this.add_event_get_position("button-point-2-get-tile")})
    window.addEventListener("button-point-2-get-tile",(e)=>{this.set_tiles(this.p2x,this.p2y,e.detail,"button-point-2-get-tile")})
  }

  set_tiles(p1,p2,coord,event){ // WARNING, se tiene que agregar funciones para convertir coord a tiles
    const level = document.getElementById("get_tile-level")
    const data = degreesToTile(coord.lon,coord.lat,level.value)
    p1.value = data.x
    p2.value = data.y
    window.removeEventListener(event,this.set_tiles)
  }

  add_event_get_position(name){
    const handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas)
    handler.setInputAction(function (click) {
      // `click.position` es la posición en pantalla (pixels)
      const cartesian = viewer.camera.pickEllipsoid(
        click.position,
        viewer.scene.globe.ellipsoid
      );
    
      if (cartesian) {
        const cartographic = Cesium.Cartographic.fromCartesian(cartesian);
        const lon = Cesium.Math.toDegrees(cartographic.longitude);
        const lat = Cesium.Math.toDegrees(cartographic.latitude);
        const event = new CustomEvent(name,{"detail":{"lon":lon,"lat":lat}})
        window.dispatchEvent(event)
      }
      handler.removeInputAction(Cesium.ScreenSpaceEventType.LEFT_CLICK);
    }, Cesium.ScreenSpaceEventType.LEFT_CLICK)
  }
}
