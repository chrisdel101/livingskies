function initNavbar() {

    var scrollSpeed = 750;
    var scrollOffset = 68;
    var easing = 'swing';

        currentClass: 'active',


    $('#navbar-top .navbar-default').affix({
        offset: {
            top: $('#home').height()
        }
    });
}
function initPortfolio () {
    var portfolio = $('#portfolio');
    var items = $('.items', portfolio);
    var filters = $('.filters li a', portfolio);

    items.imagesLoaded(function() {
        items.isotope({
            itemSelector: '.item',
            layoutMode: 'fitRows',
            transitionDuration: '0.7s'
        });
    });

    filters.click(function(){
        var el = $(this);
        filters.removeClass('active');
        el.addClass('active');
        var selector = el.attr('data-filter');
        items.isotope({ filter: selector });
        return false;
    });
}
function initAnimations() {
    $('.animated').appear(function () {
        var el = $(this);
        var animation = el.data('animation');
        var delay = el.data('delay');
        if (delay) {
            setTimeout(function () {
                el.addClass(animation);
                el.addClass('showing');
                el.removeClass('hiding');
            }, delay);
        } else {
            el.addClass(animation);
            el.addClass('showing');
            el.removeClass('hiding');
        }
    }, {
        accY: -60
    });

    // Service hover animation
	$('.service').hover(function(){
		$('i', this).addClass('animated tada');
	},function(){
        $('i', this).removeClass('animated tada');
	});
}
function initStart(){
	var homeHeight = $(window).innerHeight()-69;
	$('#home').height(homeHeight);
	// fancybox
    $(".fancybox").fancybox();
	$('.collapse ul li a').click(function(){
		$(this).parents('.collapse').removeClass('in');
		});
    if(window.innerWidth < 768){
        console.log('in')
        $('#home').height('');
    }
    console.log('hh', homeHeight)
	}

$(document).ready(function () {
	initStart()
    initNavbar();
    initPortfolio();
    initAnimations();
	$(window).resize(function(){
		initStart()
	});
});
$(window).load(function () {
    $(".loader .fading-line").fadeOut();
    $(".loader").fadeOut("slow");
});
