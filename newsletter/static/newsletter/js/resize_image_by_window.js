//Adjust image size
//needs jquery
//put a #grid and #resizeme on your html and call $('#resizeme').resizeimg() 
$.fn.resizeimg = function() {
	//Define starting width and height values for the original image
	var startwidth = 1280;  
	var startheight = 960;
	//Define image ratio
	var ratio = startheight/startwidth;
	//Gather browser dimensions
	var browserwidth = $(window).width();
	var browserheight = $(window).height();
	//Resize image to proper ratio
	if ((browserheight/browserwidth) > ratio) {
	    $(this).height(browserheight);
	    $(this).width(browserheight / ratio);
		$('#grid').height(browserheight);
		$('#grid').width(browserheight / ratio);
	    $(this).children().height(browserheight);
	    $(this).children().width(browserheight / ratio);
	} else {
	    $(this).width(browserwidth);
	    $(this).height(browserwidth * ratio);
		$('#grid').width(browserwidth);
	    $('#grid').height(browserwidth * ratio);
	    $(this).children().width(browserwidth);
	    $(this).children().height(browserwidth * ratio);
	}
	//Make sure the image stays center in the window
	$(this).children().css('left', (browserwidth - $(this).width())/2);
	$(this).children().css('top', (browserheight - $(this).height())/2);
};   