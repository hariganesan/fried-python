// created by Hari Ganesan 2/18/14
// colors.js: an experiment in color

// On load
$(document).ready(function() {
  resizeContent();
});

$(window).resize(function() {
  resizeContent();
})

function resizeContent() {
  // do something here
  var height = $(window).height();
  var width = $(window).width();

  $('#main').css("height", height);
  $('#main').css("width", width);
};

var colorID = 0;

var colorArray = ["white", "red", "orange", "yellow", "green", "blue", "purple", "black"];

$(".box").on("click", function() {
  $(".box").removeClass(colorArray[colorID]);

  if (++colorID > colorArray.length - 1) {
    colorID = 0;
  }
  
  $(".box").addClass(colorArray[colorID]);
});
