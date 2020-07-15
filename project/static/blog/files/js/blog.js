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