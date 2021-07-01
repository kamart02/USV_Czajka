const tableUpdate = (results) =>{
    let tableD
    if (results.length==0){
        tableD = {
            'ph': 0,
            'temperature': 0,
            'turbility':0,
            'longitude': 0,
            'latitude': 0,
            'voltage': 0,
        }
    }
    else{
        tableD = results[results.length-1];
    }
    $('#ph').html(tableD.ph);
    $('#turbility').html(tableD.turbility);
    $('#temperature').html(tableD.temperature);
    $('#longitude').html(tableD.longitude);
    $('#latitude').html(tableD.latitude);
    $('#voltage').html(tableD.voltage);
    
    addGraphData(graph, tableD.voltage);
};