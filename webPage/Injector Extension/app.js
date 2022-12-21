
function sleep(milliseconds) {
    return new Promise(resolve => setTimeout(resolve, milliseconds));
}

sleep(10000).then(function()
{
    // var vediamo = document.getElementById("refresh");
    // vediamo.click();
    var vediamo = document.getElementById("clickMe");
    vediamo.click();
});
