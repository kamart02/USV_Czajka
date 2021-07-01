let latlng = L.latLng(55.4411764, 11.7928708);
let circle = L.circleMarker(latlng, {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 10
}).addTo(mymap);

let isProgramMoving=false;
let markerArray = [];

let goldIcon = new L.Icon({
    iconUrl: '/static/main/img/marker-icon-gold.png',
    shadowUrl: '',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });

let greenIcon = new L.Icon({
    iconUrl: '/static/main/img/marker-icon-green.png',
    shadowUrl: '',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });

const updateGpsPointer = (result) => {
    let tableD = {
        latitude: 0,
        longitude: 0
    };
    //console.log(0);
    if(result.length==0){
        tableD.latitude = 0;
        tableD.longitude = 0;
    }
    else{
        tableD = result[result.length-1]
    }
    let latlng = L.latLng(tableD.latitude, tableD.longitude);
    if($('#checkbox-radio-option-one').is(":checked")){
        isProgramMoving=true;
        mymap.panTo(latlng);
        isProgramMoving=false;
    }
    circle.setLatLng(latlng);
}

const addMarker = (latlng) => {
    markerArray.push(L.marker(latlng).addTo(mymap));
}

let lastMarkerID

const loadAllMapMarkers = (results) => {
    let tableD = results;
    //console.log(tableD);
    tableD.forEach(element => {
        //console.log(element);
        markerArray.push(L.marker(L.latLng(element.latitude, element.longitude)).addTo(mymap).bindPopup(`
        <table class='pure-table pure-table-horizontal'>
        <thead>
            <tr>
                <td>
                    Sensor
                </td>
                <td>
                    Value
                </td>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>
                    PH:
                </td>
                <td>
                    ${element.ph}
                </td>
            </tr>
            <tr>
                <td>
                    Turbility:
                </td>
                <td >
                    ${element.turbility}
                </td>
            </tr>
            <tr>
                <td>
                    Temperature:
                </td>
                <td>
                    ${element.temperature}
                </td>
            </tr>
            <tr>
                <td> </td>
                <td> </td>
            </tr>
            <tr>
                <td>
                    Latitude:
                </td>
                <td>
                    ${element.latitude}
                </td>
            </tr>
            <tr>
                <td>
                    Longitude:
                </td>
                <td>
                    ${element.longitude}
                </td>
            </tr>

        </tbody>
    </table>`));
        lastMarkerID = element.id;
    });
}



const loadNewMapMarkers = (results) => {
    let tableD;
    if(results.length==0){
        tableD =  {
            'ph': 0,
            'temperature': 0,
            'turbility':0,
            'longitude': 0,
            'latitude': 0,
            'id':-1,
        }
    }
    else{
        tableD = results[results.length-1]
    }
    if(waypoints.length!=0){
        if(waypoints[0].getLatLng().lat==tableD.latitude && waypoints[0].getLatLong().lng==tableD.longitude){
            mymap.removeLayer(waypoints[0]);
            waypoints.shift();
        }
    }
    
    //console.log(tableD.id)
    //console.log(lastMarkerID);
    if(tableD.id!=lastMarkerID && results.length!=0){
        markerArray.push(L.marker(L.latLng(tableD.latitude, tableD.longitude)).addTo(mymap).bindPopup(`
        <table class='pure-table pure-table-horizontal'>
        <thead>
            <tr>
                <td>
                    Sensor
                </td>
                <td>
                    Value
                </td>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>
                    PH:
                </td>
                <td>
                    ${tableD.ph}
                </td>
            </tr>
            <tr>
                <td>
                    Turbility:
                </td>
                <td >
                    ${tableD.turbility}
                </td>
            </tr>
            <tr>
                <td>
                    Temperature:
                </td>
                <td>
                    ${tableD.temperature}
                </td>
            </tr>
            <tr>
                <td> </td>
                <td> </td>
            </tr>
            <tr>
                <td>
                    Latitude:
                </td>
                <td>
                    ${tableD.latitude}
                </td>
            </tr>
            <tr>
                <td>
                    Longitude:
                </td>
                <td>
                    ${tableD.longitude}
                </td>
            </tr>

        </tbody>
    </table>`));
        lastMarkerID=tableD.id;
        //console.log(lastMarkerID);
    }
}

mymap.on('movestart', (e) => {
    if(!isProgramMoving){
        $('#checkbox-radio-option-one').prop("checked", false);
    }
})

let waypoints = [];

mymap.on('click', (e) => {
    if($('#waypoints').is(':checked')){
        waypoints.push(L.marker(e.latlng, {draggable: true, icon: goldIcon}).addTo(mymap));
    }
});
