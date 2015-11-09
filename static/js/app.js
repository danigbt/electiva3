/*var main = function(){
    //var currentSlideGlobal = $('.active-slide');
    //currentSlideGlobal.toggleClass('active');
    $('.item-menu').click(function(){
        var currentSlide = $('.active-slide');
        currentSlide.fadeOut(1).removeClass('active-slide');

        //currentSlide.toggleClass('active');

        var currentItem = $(this).get();
        //console.log( $(this).get() );
        //console.log( $(this).attr("id"));

        if ($(this).attr("id") == 'quienes_somos-i') {
            console.log( "Quienes Somos");
            $('#quienes_somos').fadeIn(1).addClass('active-slide');
            $(this).toggleClass('active');
            $('#donde_estamos-i').removeClass('active');
            $('#productos-i').removeClass('active');
            $('#contacto-i').removeClass('active');
        }else if($(this).attr("id") == 'donde_estamos-i'){
            console.log( "Donde estamos");
            $('#donde_estamos').fadeIn(1).addClass('active-slide');
            $(this).toggleClass('active');
            $('#quienes_somos-i').removeClass('active');
            $('#productos-i').removeClass('active');
            $('#contacto-i').removeClass('active');
        }else if($(this).attr("id") == 'productos-i'){
            console.log( "Productos");
            $('#productos').fadeIn(1).addClass('active-slide');
            $(this).toggleClass('active');
            $('#donde_estamos-i').removeClass('active');
            $('#quienes_somos-i').removeClass('active');
            $('#contacto-i').removeClass('active');
        }else if($(this).attr("id") == 'contacto-i'){
            console.log( "Contacto");
            $('#contacto').fadeIn(1).addClass('active-slide');
            $(this).toggleClass('active');
            $('#donde_estamos-i').removeClass('active');
            $('#productos-i').removeClass('active');
            $('#quienes_somos-i').removeClass('active');
        }else if($(this).attr("id") == 'index-i'){
            console.log( "Index");
            $('#index').fadeIn(1).addClass('active-slide');
            $('#donde_estamos-i').removeClass('active');
            $('#quienes_somos-i').removeClass('active');
            $('#productos-i').removeClass('active');
            $('#contacto-i').removeClass('active');
        };
               
    });

};
*/
/*$(document).ready(main);*/

// jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});

// Floating label headings for the contact form

$(function() {
    $("body").on("input propertychange", ".floating-label-form-group", function(e) {
        $(this).toggleClass("floating-label-form-group-with-value", !! $(e.target).val());
    }).on("focus", ".floating-label-form-group", function() {
        $(this).addClass("floating-label-form-group-with-focus");
    }).on("blur", ".floating-label-form-group", function() {
        $(this).removeClass("floating-label-form-group-with-focus");
    });
});


