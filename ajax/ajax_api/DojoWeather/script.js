var cookieBar = document.getElementById("cookie-policy"); 

function removeCookie() { 
    cookieBar.remove();
}

var highTemps = document.querySelectorAll('.highTemp');
var lowTemps = document.querySelectorAll('.lowTemp');


function convertTemp(element) { 
    // console.log(element.value);
    if (element.value === "ºF") {
        highTemps.forEach(h => {
            h.innerHTML = (parseInt(h.innerHTML) * 9/5 + 32).toFixed(0) +"º"; 
            });
        lowTemps.forEach(l => {
            l.innerHTML = (parseInt(l.innerHTML) * 9/5 + 32).toFixed(0) +"º"; 
        });
    
    // highTemps[0].innerHTML=parseInt(highTemps[0].innerHTML) * 9/5 + 32 +"º";
    // highTemps[1].innerHTML=parseInt(highTemps[1].innerHTML) * 9/5 + 32 +"º";
    // highTemps[2].innerHTML=parseInt(highTemps[2].innerHTML) * 9/5 + 32 +"º";
    // highTemps[3].innerHTML=parseInt(highTemps[3].innerHTML) * 9/5 + 32 +"º";
    // lowTemps[0].innerHTML=parseInt(lowTemps[0].innerHTML) * 9/5 + 32 +"º";
    // lowTemps[1].innerHTML=parseInt(lowTemps[1].innerHTML) * 9/5 + 32 +"º";
    // lowTemps[2].innerHTML=parseInt(lowTemps[2].innerHTML) * 9/5 + 32 +"º";
    // lowTemps[3].innerHTML=parseInt(lowTemps[3].innerHTML) * 9/5 + 32 +"º";
    } else {
        // location.reload();
        highTemps.forEach(h => {
            h.innerHTML = (((parseInt(h.innerHTML) - 32) * 5/9)).toFixed(0) +"º"; 
        });
        lowTemps.forEach(l => {
            l.innerHTML = (((parseInt(l.innerHTML) - 32) * 5/9)).toFixed(0) +"º"; 
        });
    }
}

