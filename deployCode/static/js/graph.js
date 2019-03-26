var url2="/api/getGraphDetails";

//getting and setting graph readings
function getGraphData(){
 var XHR = new XMLHttpRequest();

  XHR.onreadystatechange = function() {
    // var c1=0,c2=0,c3=0;
    if(XHR.readyState == 4) {
      if(XHR.status == 200) {
        // console.log(XHR.responseText);
        var responseData = JSON.parse(XHR.responseText);
        // console.log(responseData.data[0][1]);

              var label_graph = new Array(10);
              var cap1_graph = new Array(10);
              var cap2_graph = new Array(10);
              var cap3_graph = new Array(10);



  
//       //   // dates
        label_graph[0]=responseData.data[0][4];
        label_graph[1]=responseData.data[1][4];
        label_graph[2]=responseData.data[2][4];
        label_graph[3]=responseData.data[3][4];
        label_graph[4]=responseData.data[4][4];
        label_graph[5]=responseData.data[5][4];
        label_graph[6]=responseData.data[6][4];
        label_graph[7]=responseData.data[7][4];
        label_graph[8]=responseData.data[8][4];
        label_graph[9]=responseData.data[9][4];


        // c1
        cap1_graph[0]=responseData.data[0][1];
        cap1_graph[1]=responseData.data[1][1];
        cap1_graph[2]=responseData.data[2][1];
        cap1_graph[3]=responseData.data[3][1];
        cap1_graph[4]=responseData.data[4][1];
        cap1_graph[5]=responseData.data[5][1];
        cap1_graph[6]=responseData.data[6][1];
        cap1_graph[7]=responseData.data[7][1];
        cap1_graph[8]=responseData.data[8][1];
        cap1_graph[9]=responseData.data[9][1];

        // c2
        cap2_graph[0]=responseData.data[0][2];
        cap2_graph[1]=responseData.data[1][2];
        cap2_graph[2]=responseData.data[2][2];
        cap2_graph[3]=responseData.data[3][2];
        cap2_graph[4]=responseData.data[4][2];
        cap2_graph[5]=responseData.data[5][2];
        cap2_graph[6]=responseData.data[6][2];
        cap2_graph[7]=responseData.data[7][2];
        cap2_graph[8]=responseData.data[8][2];
        cap2_graph[9]=responseData.data[9][2];

        // c3
        cap3_graph[0]=responseData.data[0][3];
        cap3_graph[1]=responseData.data[1][3];
        cap3_graph[2]=responseData.data[2][3];
        cap3_graph[3]=responseData.data[3][3];
        cap3_graph[4]=responseData.data[4][3];
        cap3_graph[5]=responseData.data[5][3];
        cap3_graph[6]=responseData.data[6][3];
        cap3_graph[7]=responseData.data[7][3];
        cap3_graph[8]=responseData.data[8][3];
        cap3_graph[9]=responseData.data[9][3];

        // chart


        new Chart(document.getElementById("line-chart"), {
        type: 'line',
        data: {

            // time
        //   labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
          labels: [label_graph[0],label_graph[1],label_graph[2],label_graph[3],label_graph[4],label_graph[5],label_graph[6],label_graph[7],label_graph[8],label_graph[9]],

          
          datasets: [{ 
            //   data: [86,114,106,106,107,111,133,221,783,2478],
            data: [cap1_graph[0],cap1_graph[1],cap1_graph[2],cap1_graph[3],cap1_graph[4],cap1_graph[5],cap1_graph[6],cap1_graph[7],cap1_graph[8],cap1_graph[9]],

              label: "Bin 1",
              borderColor: "#3e95cd",
              fill: false
            }, { 
            //   data: [282,350,411,502,635,809,947,1402,3700,5267],
            data: [cap2_graph[0],cap2_graph[1],cap2_graph[2],cap2_graph[3],cap2_graph[4],cap2_graph[5],cap2_graph[6],cap2_graph[7],cap2_graph[8],cap2_graph[9]],
            

              label: "Bin 2",
              borderColor: "#8e5ea2",
              fill: false
            }, { 
            //   data: [168,170,178,190,203,276,408,547,675,734],
            data: [cap3_graph[0],cap3_graph[1],cap3_graph[2],cap3_graph[3],cap3_graph[4],cap3_graph[5],cap3_graph[6],cap3_graph[7],cap3_graph[8],cap3_graph[9]],
              label: "Bin 3",
              borderColor: "#3cba9f",
              fill: false
            }
          ]
        },
        options: {
          title: {
            display: true,
            text: 'Bin Percentages'
          }
        }
      });




  
      } else {
        console.log("There was a problem!");
      }
    }
  }
  
  XHR.open("GET", url2);
  XHR.send();
} 

//executing above function for every 10 secinds
setInterval(function(){
  getGraphData();
},10000);

//first exec
getGraphData();
