<?php
$text = urlencode ( $_POST['text'] );
$url='http://34.105.38.103:12345/?content='.$text;
$fp = fopen($url, 'r');
stream_get_meta_data($fp);
while(!feof($fp)) {
$result = fgets($fp, 1024);
}

?>


<div id="main" style="width: 600px;height:400px;margin-right:5%;margin-top:7%;"></div>
<script type="text/javascript">

        var s1 = <?php echo $result; ?>;

        var myChart = echarts.init(document.getElementById('main'));

        var nodes1 = [];
        for (var i=0;i<s1.length;i++){
             nodes1.push({category:0, name: s1[i][0] +" (sub)","value":3,"size":30});
             nodes1.push({category:1, name: s1[i][2]+" (ob)","value":3,"size":30});
              }
        var nodes = [];
        for(var i = 0, l = nodes1.length; i < l; i++) {
          for(var j = i + 1; j < l; j++)
            if (nodes1[i] === nodes1[j]) j = ++i;
          nodes.push(nodes1[i]);
        }

        var links=[];
        for (var i=0;i<s1.length;i++){
             links.push({"source" : s1[i][0] +" (sub)", "target" : s1[i][2]+" (ob)",
             "flow":s1[i][1].substring(4)+" score: " + + parseFloat(s1[i][3].toFixed(2)), "value":s1[i][3]});
              }

        
        nodes.forEach(function (node) {

            node.symbolSize = node.size;

        });
        option = {

            title: {
                text: 'Relationship Grgaph',
                subtext: '示例',
                top: 'bottom',
                left: 'middle'

            },

            tooltip: {
                trigger: 'item',
                formatter:function(params){
                    if(params.data.flow){
                        return params.data.flow;
                    }
                    else{
                        return params.data.name+":"+params.data.value+"次";
                    }
                }
            },

            toolbox: {
                show : true,
                feature : {

                    saveAsImage: true
                }
            },

            legend: [{

                data:['Body1','Body2']
            }],

            series: [{
                type: 'graph',
                layout: 'force',
                symbolSize: 20,
                edgeSymbol: ['circle', 'arrow'],
                edgeSymbolSize: [4, 8],

            animation: false,
            roam: true,
            label: {
                normal : {
                    show : true,
                    position : 'right',
            },
                emphasis : {

                 }
            },
            draggable: true,
            focusNodeAdjacency:true,
            data: nodes,
            edges: links,
            categories: [

                {
                    name: 'Body1'
                },
                {
                    name:'Body2'
                }
                ],
            force : {
                repulsion : 100,
                edgeLength :120,  },

            lineStyle: {
                normal: {
                    opacity: 0.9,
                    width: 2,
                    curveness: 0

                }
            }
        }]
    };
    myChart.setOption(option);



    </script>
