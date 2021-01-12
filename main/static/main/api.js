const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

let temp;

const getSpeedData =  () => {
    let ret
    ret = $.getJSON('api/speed/speed/1/', function(data, status){
        temp = data;
    });

    return temp;
    //console.log(ret);
    //return ret;
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
    $.getJSON('api/data/data/', function(data, status){
        return data[-1];
    });
}

const getAllData = () => {
    $.getJSON('api/data/data/', function(data, status){
        return data;
    });
}