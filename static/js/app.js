$(function(){
  $("#apple-crsl .b_indicators .carousel-inner").slidesjs({
    width: 940,
    height: 350,
    navigation: {
      active: false
    },
    play: {
      active: false,
      auto: true,
      effect: 'slide',
      interval: 3000,
    }
  });

  // $('#apple-crsl').carousel({
  //   interval: 0,
  //   pause: false,
  // });


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

    