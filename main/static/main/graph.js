function addGraphData(chart, data) {

    if(chart.data.labels.length>20){
        removeGraphData(chart);
    }

    if(chart.data.labels.length<=20){
        let temp='';
        if(chart.data.labels.length!=0){
            temp='-';
        }
        chart.data.labels.unshift(temp + chart.data.labels.length * 5 + 's');
    }
    
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    
    chart.update();
}

function removeGraphData(chart) {
    //chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
    });
}

let graph

$(document).ready(() =>{
    
    let ctx = document.getElementById('wykres');
    graph = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Voltage',
                data: [],
                fill: false,
				backgroundColor: 'rgba(255, 99, 132, 1)',
				borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1,
                //lineTension: 0,
            }],
            
            
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: false,
                        suggestedMin: 14.8,
                        suggestedMax: 17,
                    }
                }]
            },
            maintainAspectRatio: false,
            responsive: true,
            
        }
    });
})