var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-71.59496643495604,-33.035960040525815], // Coordenadas iniciales del mapa (UTFSM)
    zoom: 0.01 // Nivel de zoom inicial
});
map.addControl(new mapboxgl.NavigationControl());

map.addControl(new mapboxgl.GeolocateControl({
    positionOption:{
        enableHighAccuracy: true
    },
    trackUserLocation: true
}))