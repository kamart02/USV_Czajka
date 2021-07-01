let UPDATETIME=5000

$(window).ready(function() {
    $('#mainBody').show();
    
});

function getMiliseconds(){
    return Date.now();
  }

$(document).ready(() =>{

    mymap.invalidateSize();

    $('#send').click(()=>{
        $("#waypoints").prop("checked", false);
        waypoints.forEach(element => {
            sendWaypoint(element.getLatLng().lat, element.getLatLng().lng);
            element.setIcon(greenIcon);
            element.dragging.disable()
        })
        sendStatus({
            "abort": false,
            "delMapData": false,
            "delData": false,
            "automation": true
        })

    })

    $('#abort').click(()=>{
        //console.log('test');
        sendStatus({
            'abort': true,
            'delMapData': false,
            'delData': false
        })
        
    })

    $('#rmalldata').click(() =>{
        r = confirm("This action will delete all past data on the drone. (this cannot be undone)\nDo you want to continue?");
        if(r==true){
            sendStatus({
                'abort': false,
                'delMapData': true,
                'delData': true
            })
            //window.location.reload(true);
        }
    })

    $('#gethelp').click(() =>{
        r = alert("This is a help page for usage of the drone.\n\nThe layout is pretty simple. It consists of the shifter, camera view, map and some control buttons and information.\nThe drone can be controlled using the \“i\”, \“o\”, \“p\”, \”k\”, \”l\”, \”;\”\nThe actions are as follows: left engine forward, both engines forward,  right engine backwards, left engine backwards, both engines backwards, right engine backwards.\nThe control buttons in the right corner allow to download the data or abort semi-automatic mode.\nUnder the map there are some check boxes used to center the gps pointer on the map or place automation waypoints on the map. Clicking the \”Send Waypoints\” button will engage semi-autonomous mode.");
    })
    

    $('#dlmd').click(function(){
        window.location.href='api/mapdata/?format=json';
    })

    $('#dlad').click(function(){
        window.location.href='api/data/?format=json';
    })

    

    getAllMapData(loadAllMapMarkers);

    setInterval(()=>{getAllMapData(loadNewMapMarkers)}, 5000);
    setInterval(()=>{getLastData(tableUpdate)}, UPDATETIME);
    setInterval(()=>{getAllData(updateGpsPointer)}, UPDATETIME);
    setInterval(()=>{getSpeedData((results)=>{
        if(getMiliseconds()-last_check>=1000){
            L_speed=results.leftSpeed;
            R_speed=results.rightSpeed;
        }
        //redraw();
    })},UPDATETIME);
});


