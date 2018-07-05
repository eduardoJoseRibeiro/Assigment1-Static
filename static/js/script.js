function isScrolledIntoView(elem){
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $(elem).offset().top;
    var elemBottom = elemTop + $(elem).height();

    return ((elemBottom - 200 <= docViewBottom) && (elemTop + 200 >= docViewTop));
}

$(window).on('scroll', function(){
    if (isScrolledIntoView('.animate-left')) {
        $('.animate-left').addClass('animated bounceInLeft');
    }
    if (isScrolledIntoView('.animate-up')) {
        $('.animate-up').addClass('animated bounceInUp');
    }
    if (isScrolledIntoView('.animate-right')) {
        $('.animate-right').addClass('animated bounceInRight');
    }
});