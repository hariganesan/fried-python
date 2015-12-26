// Created by Hari Ganesan 3/28/14
// main.js for website

var colors = {
  "mobile": "#422",
  "games": "#231",
  "web": "#124",
  "about": "#ffa"
};

$(document).ready(function() {
  $(".planet").css({"display": "none"});
  $("#planet-mobile").fadeIn(400, function() {
    $("#planet-games").fadeIn(400, function() {
      $("#planet-web").fadeIn(400, function() {
        $("#planet-about").fadeIn(400);
      });
    });
  });
})

$(".planet").hover(function() {
  $("body").animate({"background-color": jQuery.Color(colors[this.id.slice(7)])}, 600);
  $(this).animate({"background-color": jQuery.Color("#333")}, 600);
}, function() {
  $("body").animate({"background-color": jQuery.Color("#111")}, 600);
  $(this).animate({"background-color": jQuery.Color("#555")}, 600);
});

$(".planet").click(function() {
  if ($(this).hasClass("click")) {
    $(this).removeClass("click");
  } else {
    $(this).addClass("click");    
  }
});
