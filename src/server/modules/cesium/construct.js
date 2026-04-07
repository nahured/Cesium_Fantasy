

export function create_viewer(type) {
    switch (type) {
        case "clear":
            clear_cesium()
            break
        default:
            default_cesium()
    }
}

function clear_cesium(){
    window.viewer = new Cesium.Viewer('cesiumContainer',{
        creditContainer : null, 
        animation       : false,
        baseLayerPicker : false,
        fullscreenButton: false,
        geocoder        : false,
        homeButton      : false,
        infoBox         : false,
        sceneModePicker : false,
        selectionIndicator: false,
        timeline        : false,
        navigationHelpButton: false,
        shouldAnimate   : true,
    })
    viewer.creditDisplay.destroy();
    add_layer();
}

function default_cesium(){
    window.viewer = new Cesium.Viewer('cesiumContainer')
}

function add_layer(){
    window.viewer.imageryLayers.addImageryProvider(
        new Cesium.TileCoordinatesImageryProvider({
          color: Cesium.Color.RED
        })
      );
}