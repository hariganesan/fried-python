// created by Hari Ganesan 4/1/14
// navigation for website

$(document).ready(function() {
	$("#nav-box").delay(700).animate({"right": "0%", "top": "0%"}, 500);
});

$("#nav-box").click(function() {
	if ($("body").hasClass("red")) {

	} else if ($("body").hasClass("green")) {

	} else if ($("body").hasClass("blue")) {
		
	} else if ($("body").hasClass("purple")) {

	} else {

	}
	$("#nav-box-overlay").css("z-index", "2");
	$("#nav-box").animate({"width": "100%", "height": "100%"}, 700);
	$("#nav-box-overlay").animate({"width": "100%", "height": "100%", opacity:1}, 700, function() {
		window.location = "/";
	});
});