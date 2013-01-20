//equal heights
 
(function($) {
	$.fn.equalHeights = function(minHeight, maxHeight) {
		tallest = (minHeight) ? minHeight : 0;
		this.each(function() {
			if($(this).height() > tallest) {
				tallest = $(this).height();
			}
		});
		if((maxHeight) && tallest > maxHeight) tallest = maxHeight;
		return this.each(function() {
			$(this).height(tallest);
		});
	}
})(jQuery);


//http://www.agilecarousel.com/
var data=[{
      "content": "<div class='slide_inner'><a target='_blank' class='photo_link' href='#'><img class='photo' src='http://1.cdn.nhle.com/ducks/images/upload/2012/09/DucksD_DL.jpg' alt='Bike'></a><a target='_blank' class='caption' href='#'>Sample Carousel Pic Goes Here And The Best Part is that...</a></div>",
      "content_button": "<div class='thumb'><img src='http://www.agilecarousel.com/images/f2_thumb.jpg' alt='bike is nice'></div><p>Agile Carousel Place Holder</p>"
}, {
      "content": "<div class='slide_inner'><a target='_blank' class='photo_link' href='#'><img class='photo' src='http://www.agilecarousel.com/images/banner_tunnel.jpg' alt='Paint'></a><a target='_blank' class='caption' href='#'>Sample Carousel Pic Goes Here And The Best Part is that...</a></div>",
      "content_button": "<div class='thumb'><img src='http://www.agilecarousel.com/images/f2_thumb.jpg' alt='bike is nice'></div><p>Agile Carousel Place Holder</p>"
}, {
      "content": "<div class='slide_inner'><a target='_blank' class='photo_link' href='#'><img class='photo' src='http://www.agilecarousel.com/images/banner_bike.jpg' alt='Tunnel'></a><a target='_blank' class='caption' href='#'>Sample Carousel Pic Goes Here And The Best Part is that...</a></div>",
      "content_button": "<div class='thumb'><img src='http://www.agilecarousel.com/images/f2_thumb.jpg' alt='bike is nice'></div><p>Agile Carousel Place Holder uwiu erwoieu</p>"
}, {
      "content": "<div class='slide_inner'><a target='_blank' class='photo_link' href='#'><img class='photo' src='http://www.agilecarousel.com/images/banner_bike.jpg' alt='Bike'></a><a target='_blank' class='caption' href='#'>Sample Carousel Pic Goes Here And The Best Part is that...</a></div>",
       "content_button": "<div class='thumb'><img src='http://www.agilecarousel.com/images/f2_thumb.jpg' alt='bike is nice'></div><p>Agile Carousel Place Holder</p>"
}, {
      "content": "<div class='slide_inner'><a target='_blank' class='photo_link' href='#'><img class='photo' src='http://www.agilecarousel.com/images/banner_tunnel.jpg' alt='Paint'></a><a target='_blank' class='caption' href='#'>Sample Carousel Pic Goes Here And The Best Part is that...</a></div>",
       "content_button": "<div class='thumb'><img src='http://www.agilecarousel.com/images/f2_thumb.jpg' alt='bike is nice'></div><p>As dokimasoume kai ayto to carousel mpas kai doume kamia prokopi</p>"
} ]

$(document).ready(function(){
          
         
          
	$('.carousel').carousel({
		loop: true,
                autoSlide: false,
                animSpeed: 'slow'  
	});    


		 $("#flavor_2").agile_carousel({
            carousel_data: data,
            carousel_outer_height: 400,
            carousel_height: 400,
            slide_height: 230,
            carousel_outer_width: 662,
            slide_width: 662,
            transition_type: "fade",
            transition_time: 600,
            timer: 3000,
            continuous_scrolling: true,
            control_set_1: "numbered_buttons,previous_button,pause_button,next_button",
            control_set_2: "content_buttons",
            change_on_hover: "content_buttons"
        });
        
        if ($('.halfpromo'.length > 0)) {
		    $('.halfpromo.box .whitewrap').equalHeights();
	    }
        
        if ($('.album-list'.length > 0)) {
		    $('.album-list ul li').equalHeights();
	    }        
        
        
        //http://www.vissit.com/projects/eventCalendar/ 
	
	var url = window.location.href;
	$('.fb-comments').attr('data-href',url);
    
    $('#g1 a').lightBox({
        fixedNavigation:true,
        imageLoading:			'templates/images/lightbox-ico-loading.gif',		// (string) Path and the name of the loading icon
        imageBtnPrev:			'templates/images/lightbox-btn-prev.gif',			// (string) Path and the name of the prev button image
        imageBtnNext:			'templates/images/lightbox-btn-next.gif',			// (string) Path and the name of the next button image
        imageBtnClose:			'templates/images/lightbox-btn-close.gif',		// (string) Path and the name of the close btn
        imageBlank:				'templates/images/lightbox-blank.gif',			// (string) Path and the name of a blank image (one pixel)
     });
});


$(window).resize(function() {
  if ($('.halfpromo'.length > 0)) {
		$('.halfpromo.box .whitewrap').equalHeights();
	}
});






