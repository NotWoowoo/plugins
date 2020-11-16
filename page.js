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
    document.title = "Woowoo's plugins";
}