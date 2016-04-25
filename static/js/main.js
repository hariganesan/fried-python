var currentOpacity = 0;
var windowWidth = 0;
var windowHeight = 0;

var roles = [
  "a co-founder", "an entrepreneur", "a developer", "a product guy", "not a ninja"
];

var getRandomColor = function() {
  var getRandomColorBit = function() {
    return Math.floor((Math.random()*100) + 40).toString(16);
  };

  return "#" + getRandomColorBit() + getRandomColorBit() + getRandomColorBit();
}

var currentRole = -1;
var fadeDelay = 200;

$(document).ready(function() {
  windowWidth = $(window).width();
  windowHeight = $(window).height();
  currentOpacity = parseFloat($("#headshot").css("opacity"));

  var roleChanger = function() {
    if (++currentRole >= roles.length) {
      currentRole = 0;
    }

    $("#role").fadeOut(fadeDelay, function() {
      $(this).css("color", getRandomColor())
      $(this).html(roles[currentRole]).fadeIn(fadeDelay);
    });

    setTimeout(roleChanger, 4000);
  }

  roleChanger();
});

$(window).resize(function() {
  windowWidth = $(window).width();
  windowHeight = $(window).height();
});

$(document).mousemove(function(e) {
    var pageX = e.pageX;
    var pageY = e.pageY;

    if (pageX <= windowWidth/4) {
      $("#headshot").css("opacity", 0.15);
    } else if (pageX <= windowWidth/2) {
      $("#headshot").css("opacity", currentOpacity*pageX/(windowWidth/2));
    } else {
      $("#headshot").css("opacity", currentOpacity);
    }
});
