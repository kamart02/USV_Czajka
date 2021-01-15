const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

let temp;

const getSpeedData =  () => {
    let ret
    ret = $.ajax('api/speed/1/', {
        type: 'GET',
        async: false,
    })
    return ret.responseJSON;
}

const sendSpeedData = (lSpeed, rSpeed) => {
    $.ajax('api/speed/1/',{
        type: 'PUT',
        headers: { "X-CSRFToken": csrftoken },
        data:{  
            rightSpeed: rSpeed,
            leftSpeed: lSpeed
        }
    });
}

const getLastData = () => {
    let ret;
    ret = $.ajax('api/data/', {
        async: false,
        type: 'GET',
    }).responseJSON;
    return ret[ret.length-1];
}

const getAllData = () => {
    return $.ajax('api/data/', {
        async: false,
        type: 'GET',
    }).responseJSON;
}

const getLastMapData = () => {
    let ret;
    ret = $.ajax('api/mapdata/', {
        async: false,
        type: 'GET',
    }).responseJSON;
    return ret[ret.length-1];
}

const getAllMapData = () => {
    let ret;
    ret = $.ajax('api/mapdata/', {
        async: false,
        type: 'GET',
    }).responseJSON;
    return ret;
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

const sendAbort = (value) => {
        $.ajax('api/abort/',{
            type: 'POST',
            dataType: 'JSON',
            headers: { "X-CSRFToken": csrftoken },
            data: {
                "abort": value
            }
        }
        )
    };