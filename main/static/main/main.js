$(document).ready(() =>{

    $('#send').click(()=>{
        
        waypoints.forEach(element => {
            sendWaypoint(element.getLatLng().lat, element.getLatLng().lng);
        })
    })

    $('#abort').click(()=>{
        console.log('test');
        sendAbort(true);
        
    })

    loadAllMapMarkers();

    setInterval(loadNewMapMarkers, 1000);
    setInterval(tableUpdate, 1000);
    setInterval(updateGpsPointer, 1000);
});


