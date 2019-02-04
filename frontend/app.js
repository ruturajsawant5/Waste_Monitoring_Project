var db1 = document.querySelector("#db1");
var db2 = document.querySelector("#db2");
var db3 = document.querySelector("#db3");
var btn = document.querySelector("#button   ");
var url = "https://vlm4qgyyg8.execute-api.ap-south-1.amazonaws.com/First";


// btn.addEventListener("click", function(){

//     fetch(url,{mode: 'no-cors'})
//     .then(handleError)
//     .then(parseJSON)
//     .then(updateProfile)
//     .catch(printError);

// });

// function handleError(res){
//     if(!res.ok){
//         throw Error("404");
//     }
//     return res;
// }

// function parseJSON(data){
//     // var a = JSON.parse(data);
//     return data.json();
// }

// function updateProfile(data){
//     // var av = data.results[0].picture.medium;
//     console.log(data);
// }

 var c1=0,c2=0,c3=0;
// function printError(err){
//     console.log(err);
// }

var XHR = new XMLHttpRequest();

XHR.onreadystatechange = function() {
  if(XHR.readyState == 4) {
    if(XHR.status == 200) {
      var parsedData = JSON.parse(XHR.responseText);
      c1 = parsedData.capcity1;
      c2 = parsedData.capcity2;
      c3 = parsedData.capcity3;

    } else {
      console.log("There was a problem!");
    }
  }
}

XHR.open("GET", url);
XHR.send();

    setInterval(function(){
        db1.textContent=c1;
        db2.textContent=c2;
        db3.textContent=c3;
    },3000);
