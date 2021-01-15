const tableUpdate = () =>{
    let tableD = getLastData();
    $('#ph').html(tableD.ph);
    $('#turbility').html(tableD.turbility);
    $('#temperature').html(tableD.temperature);
    $('#longitude').html(tableD.longitude);
    $('#latitude').html(tableD.latitude);
    
};