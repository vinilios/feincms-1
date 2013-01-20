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

$(document).ready(function(){
          
         
          
	$('.carousel').carousel({
		loop: true,
                autoSlide: false,
                animSpeed: 'slow'  
	});    


       if ($('.halfpromo'.length > 0)) {
		    $('.halfpromo.box .whitewrap').equalHeights();
	    }
        
        if ($('.album-list'.length > 0)) {
		    $('.album-list ul li').equalHeights();
	    }        
 	$('.faq li p:first-child a').click(function(e){
		e.preventDefault();
		$(this).parent('p').siblings('div.ans').slideToggle(400)
	});       
        
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






