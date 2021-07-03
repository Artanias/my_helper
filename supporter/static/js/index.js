
var notice = document.getElementsByName('notification')[0];
notice.addEventListener("change", function(){
    if (this.checked){
        document.getElementById("folder").style.display = "block";
        document.getElementById("music").style.display = "block";
        document.getElementById("random_btn").style.display = "block";
    } else {
        document.getElementById("folder").style.display = "none";
        document.getElementById("music").style.display = "none";
        document.getElementById("random_btn").style.display = "none";
    }
})
