document.body.classList.add('js-loading');
window.addEventListener("load", function(){
    if(!document.hidden){
        document.body.classList.remove('js-loading');
    }
});

document.addEventListener('visibilitychange', function(e) {
    document.body.classList.remove('js-loading');
});

document.onload = function(){
    console.log("fff");
}

document.addEventListener("DOMContentLoaded", main);
function main(){
    document.getElementById("toolbar").innerHTML = `
    <a class = "toolbarItem" href="./index.html#homeSection">Home</a>
    <a class = "toolbarItem" href="./index.html#pluginsHeader">Plugins</a>
    <a class = "toolbarItem" href="./index.html#aboutHeader">About</a>`;
}