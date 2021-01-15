let latlng = L.latLng(55.4411764, 11.7928708);
let circle = L.circleMarker(latlng, {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 10
}).addTo(mymap);

let isProgramMoving=false;
let markerArray = [];

const updateGpsPointer = () => {
    let tableD = getLastData();
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

const loadAllMapMarkers = () => {
    let tableD = getAllMapData();
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



const loadNewMapMarkers = () => {
    let tableD = getLastMapData();
    //console.log(tableD.id)
    //console.log(lastMarkerID);
    if(tableD.id!=lastMarkerID){
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
        waypoints.push(L.marker(e.latlng, {draggable: true}).addTo(mymap));
    }
});
