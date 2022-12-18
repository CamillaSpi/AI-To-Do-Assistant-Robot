const site = window.location.hostname;
function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
};
sleep(3500).then(() => {
    var vediamo = document.getElementById("clickMe");
    vediamo.click();
});

//alert(vediamo);
//myFuncPageld()