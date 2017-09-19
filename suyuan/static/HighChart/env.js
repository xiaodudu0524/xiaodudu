$(function () {
    $.getJSON('/shouye/data/', function (data) {
       var arr = new Array()
       for(var i=0;i<data.length;i++){
           year = parseInt(data[i].slice(0,1)[0].split(",")[0])
           month = parseInt(data[i].slice(0,1)[0].split(",")[1])-1
           day = parseInt(data[i].slice(0,1)[0].split(",")[2])
           env_data = Number(data[i].slice(1))
           glwz_time = Date.UTC(year,month,day)
           // window.alert(glwz_time)
           var arr1 = new Array()
           arr1.push(glwz_time)
           arr1.push(env_data)
           arr.push(arr1)
       };
       var chart = null;
        $('#container1').highcharts({
            chart: {
                zoomType: 'x'
            },
            title: {
                text: '空气湿度'
            },
            subtitle: {
                text: document.ontouchstart === undefined ?
                '鼠标拖动可以进行缩放' : '手势操作进行缩放'
            },
            credits: {
                enabled:false
            },
            xAxis: {
                type: 'datetime',
                dateTimeLabelFormats: {
                    millisecond: '%H:%M:%S.%L',
                    second: '%H:%M:%S',
                    minute: '%H:%M',
                    hour: '%H:%M',
                    day: '%m-%d',
                    week: '%m-%d',
                    month: '%Y-%m',
                    year: '%Y'
                }
            },
            tooltip: {
                dateTimeLabelFormats: {
                    millisecond: '%H:%M:%S.%L',
                    second: '%H:%M:%S',
                    minute: '%H:%M',
                    hour: '%H:%M',
                    day: '%Y-%m-%d',
                    week: '%m-%d',
                    month: '%Y-%m',
                    year: '%Y'
                }
            },
            yAxis: {
                title: {
                    text: '摄氏度'
                }
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 0,
                            y2: 1
                        },
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    marker: {
                        radius: 2
                    },
                    lineWidth: 1,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    threshold: null
                }
            },
            series: [{
                type: 'area',
                name: '温度',
                data: arr
            }]
        },function (c) {
            chart = c;
        });
        $('ul li').click(function(){
        var self = $(this);
        for(var i=0;i<chart.series.length;i++) {
            var serie = chart.series[i];
            serie.update({
                type: self.data('type')
            });
        }
        });
    });
});
