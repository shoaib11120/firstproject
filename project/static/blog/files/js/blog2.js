lastScrollTop=0;
window.addEventListener("scroll",function(){
	var st=window.pageYOffset || document.documentElement.scrollTop;
	var navBar=document.getElementById("navBar");
	if (st>lastScrollTop) {
		
		navBar.style.top="-60px";
	}else{
		navBar.style.top="0px";
	}
	lastScrollTop=st<=0?0:st;
},false);
$(".innerPost").hover(function(e){
	e.preventDefault()
	if ($(this).parent().hasClass("activePS")) {
		$(this).parent().removeClass("activePS");
	}
	else{
		deAnimatePost();
		$(this).parent().addClass("activePS");
	}
});
function deAnimatePost(){
	var activePS =document.getElementsByClassName("activePS");
	for (var i = 0; i < activePS.length; i++) {
		$(activePS[i]).removeClass("activePS");
	}
}