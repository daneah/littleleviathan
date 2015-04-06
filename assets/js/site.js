$('.itunes-link').on('click', function(){
    ga('send', 'event', 'button', 'click', 'itunes-store');
});

$('.newsletter-form').on("submit", function(){
    ga('send', 'event', 'button', 'click', 'newsletter-signup');
});