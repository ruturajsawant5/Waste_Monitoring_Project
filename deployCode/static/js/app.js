var db1 = document.querySelector("#db1");
var db2 = document.querySelector("#db2");
var db3 = document.querySelector("#db3");
var btn = document.querySelector("#button");

//local api route
var url="/api/getBinDetails";

// gets and sets DUSTBIN VALUES
function getBinData(){
var XHR = new XMLHttpRequest();

  XHR.onreadystatechange = function() {
    var c1=0,c2=0,c3=0;
    if(XHR.readyState == 4) {
      if(XHR.status == 200) {
        // console.log(XHR.responseText);
        var responseData = JSON.parse(XHR.responseText);
        // console.log(responseData);

        c1=responseData.capacity1;
        c2=responseData.capacity2;
        c3=responseData.capacity3;
        db1.textContent=c1;
        db2.textContent=c2;
        db3.textContent=c3;
  
      } else {
        console.log("There was a problem!");
      }
    }
  }
  
  XHR.open("GET", url);
  XHR.send();

}

//Executes above function for every 3 seconds
setInterval(function(){
  getBinData();
},3000);

//first exec
getBinData();
