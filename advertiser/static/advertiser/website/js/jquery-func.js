/*global $, console, alert*/
$(function () {
	//=================================== scroll  ===================================//
    'use strict';
/*$body.scrollspy({
      target: '#navbar-main',
      offset: navHeight
    });

    $window.on('load', function () {
      $body.scrollspy('refresh')
    });

    $('#navbar-main [href=#]').click(function (e) {
      e.preventDefault()
    });*/
    window.onload = function () {
        
        setTimeout(function () {
            $(".rslides li h1").css({
                opacity: "1",
                top: 0,
                transform: "rotate(0)"
            });
            $(".rslides li h1 span").css({
                opacity: "1",
                top: "135px"
            });
            $(".rslides li h4").css({
                opacity: "1",
                top: 0,
                transform: "rotate(0)"
            });
            $(".rslides li p").css({
                opacity: "1",
                top: 0,
                transform: "rotate(0)"
            });
        }, 200);
        
    };
    
    /*window.on("scroll", function () {
        var sc = this.scrollTop();
        console.log("Window at - " + sc);
    });*/

});

