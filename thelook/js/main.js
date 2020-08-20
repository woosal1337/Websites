/* ======================================
-----------------------------------------
	The Look - Photo Gallery Template
	Version: 1.0
 ---------------------------------------
 =======================================*/


'use strict';


$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut();
	$("#preloder").delay(400).fadeOut("slow");

});

(function($) {

	/*------------------
		Navigation
	--------------------*/
	$('.main-menu').slicknav({
		appendTo:'.header-warp',
		closedSymbol: '<i class="fa fa-angle-down"></i>',
		openedSymbol: '<i class="fa fa-angle-up"></i>'
	});

	/*------------------
		Background Set
	--------------------*/
	$('.set-bg').each(function() {
		var bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});


	/*------------------
		Hero Slider
	--------------------*/
	var sliderCount;
	$(".hero-slider").on("initialized.owl.carousel", function(e) {
		sliderCount = e.item.count;
		if( sliderCount < 10) {
			sliderCount = "0" + sliderCount;
		}
	}).owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        items: 1,
        dots: false,
        animateOut: 'fadeOut',
    	animateIn: 'fadeIn',
		navText: ['<img src="img/icons/arrow-left-white.png" alt="">', '<img src="img/icons/arrow-right-black.png" alt="">'],
        smartSpeed: 1200,
		autoplay: true,
		mouseDrag: false
    }).on("changed.owl.carousel", function(e) {
		
		var Index = e.item.index - 1;
		var Count = e.item.count;
		var PreIndex = Index - 1;
		var NextIndex = Index + 1;


		if(PreIndex < 0) {
			PreIndex = Count - 1;
		}

		if(PreIndex < 1) {
			PreIndex = Count;
		}

		if (PreIndex < 10) {
			PreIndex = "0" + PreIndex;
		}

		if(NextIndex > Count) {
			NextIndex = 1;
		}

		if (NextIndex < 10) {
			NextIndex = "0" + NextIndex;
		}


		$(".hero-slider .owl-nav button.owl-prev").html('<img src="img/icons/arrow-left-white.png" alt=""> <span> '+ PreIndex +'</span> ');
		$(".hero-slider .owl-nav button.owl-next").html('<span> '+ NextIndex +' </span> <img src="img/icons/arrow-right-black.png" alt="">');
	});

	$(".hero-slider .owl-nav button.owl-prev").html('<img src="img/icons/arrow-left-white.png" alt=""> <span> '+ sliderCount +'</span> ');

	$(".hero-slider .owl-nav button.owl-next").html('<span>02</span> <img src="img/icons/arrow-right-black.png" alt="">');


	/*------------------
		Gallery Slider
	--------------------*/
	$('.gallery-slider').owlCarousel({
		loop: true,
		nav: true,
		navText: ['<img src="img/icons/arrow-left-black.png" alt="">', '<img src="img/icons/arrow-right-black.png" alt="">'],
		dots:false,
		autoplay: true,
		margin: 99,
		stagePadding: 183,
		responsive : {
			0 : {
				items: 1,
				stagePadding: 0,
				margin: 30,
			},
			480 : {
				items: 2,
				stagePadding: 0,
				margin: 30,
			},
			768 : {
				items: 2,
				stagePadding: 80,
				margin: 50,
			},
			992 : {
				items: 2,
				margin: 80,
				stagePadding: 153,
			}
		}
	});
	$('.gallery-slider').append('<div class="nav-warp"><div class="sp-container"></div></div>');
	$('.gallery-slider .owl-nav').appendTo('.nav-warp .sp-container');

	


	/*------------------
		Accordions
	--------------------*/
	$('.panel-link').on('click', function (e) {
		$('.panel-link').parent('.panel-header').removeClass('active');
		var $this = $(this).parent('.panel-header');
		if (!$this.hasClass('active')) {
			$this.addClass('active');
		}
		e.preventDefault();
	});



	/*------------------
		Circle progress
	--------------------*/
	$('.circle-progress').each(function() {
		var cpvalue = $(this).data("cpvalue");
		var cpcolor = $(this).data("cpcolor");
		var cptitle = $(this).data("cptitle");
		var cpid 	= $(this).data("cpid");

		$(this).append('<div class="'+ cpid +' loader-circle"></div><div class="progress-info"><h4>'+ cpvalue +'%</h4><p>'+ cptitle +'</p></div>');

		if (cpvalue < 100) {

			$('.' + cpid).circleProgress({
				value: '0.' + cpvalue,
				size: 119,
				thickness: 15,
				fill: cpcolor,
				emptyFill: "rgba(0, 0, 0, 0)"
			});
		} else {
			$('.' + cpid).circleProgress({
				value: 1,
				size: 119,
				thickness: 15,
				fill: cpcolor,
				emptyFill: "rgba(0, 0, 0, 0)"
			});
		}
	});
	

})(jQuery);
