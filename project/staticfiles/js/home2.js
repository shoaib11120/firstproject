var slideIndex=0;

$(document).ready(function(){
	console.log("loaded");

	setTimeout(showSlides,1000);
	function showSlides() {
		var i;
		var slides=document.getElementsByClassName("LPC");
		
		if (slideIndex>=slides.length) {
			slideIndex=0;
		}
		console.log(slides.length);
		slides[slideIndex].style.transform="translateX(-10%)";
		
		slideIndex++;
		
		// for (i = 0; i < slides.length; i++) {
		// 	slides[i].style.display="none";
		// }
		slides[slideIndex-1].style.display="block";

		slides[slideIndex-1].style.transform="translateX(0)";
		setTimeout(showSlides,5000);
	}
	
});
function blogdetail(loca) {
		console.log(loca);
		window.location.href=loca;
	}