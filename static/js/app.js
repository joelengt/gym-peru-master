$(function(){

  $('#apple-crsl').carousel({
    interval: 0,
    pause: false,
  });


  $('.effect').viewportChecker({
    classToAdd: 'moveAnimation',
    offset: 150
  });

  $('.btn-up').click(function(e) {
    e.preventDefault();
    $("html, body").animate({
        scrollTop: 0
    }, 1000); 
  });


}); 

    