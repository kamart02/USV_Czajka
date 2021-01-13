const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

let temp;

const getSpeedData =  () => {
    let ret
    ret = $.ajax('api/speed/speed/1/', {
        type: 'GET',
        async: false,
    })
    return ret.responseJSON;
}

const sendSpeedData = (lSpeed, rSpeed) => {
    $.ajax('api/speed/speed/1/',{
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
    ret = $.ajax('api/data/data/', {
        async: false,
        type: 'GET',
    }).responseJSON;
    return ret[ret.length-1];
}

const getAllData = () => {
    return $.ajax('api/data/data/', {
        async: false,
        type: 'GET',
    }).responseJSON;
}