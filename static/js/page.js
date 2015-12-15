$(document).ready(function() {
  var windowHeight = $(window).height();
  var originalHeight = $("#header-wrapper").height();
  $("#header-wrapper a").css({"display": "none"});
  $("#wrapper").css({"display": "none"});
  $("#header-wrapper").css({"height": windowHeight})
    .animate({"height": originalHeight}, 500, function() {
      $("#header-wrapper a").fadeIn(700, function() {
        $("#wrapper").fadeIn(700);
      });
  });
});

$(".nav-link").click(function() {
  var windowHeight = $(window).height();
  var target = $(this).attr("data-target");
  console.log($(this));

  $("#header-wrapper a").fadeOut(500, function() {
    $("#header-wrapper").animate({"height": windowHeight}, 500, function() {
      window.location = target;
    });
  });
  $("#wrapper").fadeOut(500);
});
