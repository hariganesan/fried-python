// Created by Hari Ganesan 3/28/14
// main.js for website

var colorDict = {
  "q-top-left": "red",
  "q-top-right": "green",
  "q-bottom-left": "blue",
  "q-bottom-right": "purple"
};

var colorArray = [ "q-top-left", "q-top-right", 
                   "q-bottom-left", "q-bottom-right"];

var homeLinkClicked = false;

$(".homeLink").hover(
  function() {
    $(this).parent().addClass(colorDict[$(this).parent().attr("id")]);
  }, function() {
    if (!homeLinkClicked) {
      $(this).parent().removeClass(colorDict[$(this).parent().attr("id")]);
    }
  }
);

$(".homeLink").click(
  function() {
    for (var i = 0; i < 4; i++) {
      if ($(this).parent().attr("id") !== colorArray[i]) {
        moveElement(colorArray[i]);
      }
    }
    homeLinkClicked = true;
    $(this).delay(1000).fadeOut(400);
    $(this).parent().delay(1000)
      .animate({width: '100%', height: '100%', top: '0%', left: '0%'}, 700);
    var target = $(this).attr("data-target");
    setTimeout(function() {
      window.location = target;
    }, 2000);
    // document.getElementById("link-" + $(this).attr("data-target")).click();
  }
);

function moveElement(elementID) {
  if (elementID === "q-top-left" || elementID === "q-bottom-left") {
    $("#" + elementID).animate({left: '-=1000'}, 1000);
  } else if (elementID === "q-top-right" || elementID === "q-bottom-right") {
    $("#" + elementID).animate({left: '+=1000'}, 1000);
  }
};