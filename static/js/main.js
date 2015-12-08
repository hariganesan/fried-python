// Created by Hari Ganesan 3/28/14
// main.js for website
var qArray = ["q-left", "q-right"];

var colors = ["red", "orange", "yellow", "green", "blue", "purple"];

var homeLinkClicked = false;
var currentColor = null;
var currentColorIndex = 0;

$(".homeLink").hover(
  function() {
    if (currentColorIndex >= colors.length - 1) {
      currentColorIndex = 0;
    } else {
      currentColorIndex += 1;
    }

    currentColor = colors[currentColorIndex];
    $(this).parent().addClass(currentColor);
    $(this).parent().addClass("hover");
  }, function() {
    if (!homeLinkClicked) {
      $(this).parent().removeClass(currentColor);
      $(this).parent().removeClass("hover");
      currentColor = null;
    }
  }
);

$(".homeLink").click(
  function() {
    for (var i = 0; i < 4; i++) {
      if ($(this).parent().attr("id") !== qArray[i]) {
        moveElement(qArray[i]);
      }
    }
    homeLinkClicked = true;
    $(this).delay(1000).fadeOut(300);
    $(this).parent().delay(600)
      .animate({width: '100%', height: '100%', top: '0%', left: '0%'}, 600);
    var target = $(this).attr("data-target");
    setTimeout(function() {
      window.location = target;
    }, 2000);
    // document.getElementById("link-" + $(this).attr("data-target")).click();
  }
);

function moveElement(elementID) {
  if (elementID === "q-left") {
    $("#" + elementID).animate({left: '-=1000'}, 800);
  } else if (elementID === "q-right") {
    $("#" + elementID).animate({left: '+=1000'}, 800);
  }
};
