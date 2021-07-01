const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

let temp;

let AllMapData;
let Speed;
let LastData;
let AllData;
let LastMapData;

let speedVal={
    leftSpeed: 0,
    rightSpeed: 0,
    id: 0,
};

const getSpeedData =  (callback) => {
    let ret
    ret = $.ajax('api/speed/', {
        type: 'GET',
        async: true,
        success: callback,
    });
    
}

const sendSpeedData =  (lSpeed, rSpeed) => {
    let ret
    let lll=lSpeed;
    let rrr=rSpeed;
    ret = $.ajax('api/speed/', {
        type: 'GET',
        async: true,
        success: (results) =>{
            $.ajax(`api/speed/${results[results.length-1]['id']}/`,{
                type: 'PUT',
                headers: { "X-CSRFToken": csrftoken },
                data:{  
                    rightSpeed: rrr,
                    leftSpeed: lll
                }
            });
        }
    })
    
}

const getLastData = (callback) => {
    let ret;
    ret = $.ajax('api/data/', {
        async: true,
        type: 'GET',
        success: callback,
    }).responseJSON;
    // if(ret.length==0){
    //     return {
    //         'ph': 0,
    //         'temperature': 0,
    //         'turbility':0,
    //         'longitude': 0,
    //         'latitude': 0,
    //     }
    // }
    // return ret[ret.length-1];
}

const getAllData = (callback) => {
    $.ajax('api/data/', {
        async: true,
        type: 'GET',
        success: callback,
    })
}

const getLastMapData = (callback) => {
    let ret;
    ret = $.ajax('api/mapdata/', {
        async: true,
        type: 'GET',
        success: callback,
    }).responseJSON;
    if(ret.length==0){
        return {
            'ph': 0,
            'temperature': 0,
            'turbility':0,
            'longitude': 0,
            'latitude': 0,
        }
    }
    return ret[ret.length-1];
}

const getAllMapData = (callback) => {
    let ret;
    ret = $.ajax('api/mapdata/', {
        async: true,
        type: 'GET',
        success: callback,
    }).responseJSON;
}

const sendWaypoint = (latitude, longitude) => {
    $.ajax('api/waypoint/',{
        type: 'POST',
        dataType: 'JSON',
        headers: { "X-CSRFToken": csrftoken },
        data: {
            "latitude": latitude.toFixed(6),
            "longitude": longitude.toFixed(6)
        }
        
        }
    )};


const sendStatus = (value) => {
        $.ajax('api/status/',{
            type: 'POST',
            dataType: 'JSON',
            headers: { "X-CSRFToken": csrftoken },
            data: {
                "abort": value.abort,
                "delMapData": value.delMapData,
                "delData": value.delData,
                "automation": value.automation
            }
        }
        )
    };