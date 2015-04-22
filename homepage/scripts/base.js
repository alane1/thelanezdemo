$(function() {

  function fixDiv() {
    var $leftNav = $('.left-navigation-div');
    if ($(window).scrollTop() > 100) {
      $leftNav.addClass('scroll-fixed');
    } else {
      $leftNav.removeClass('scroll-fixed');
    }
  }
  $(window).scroll(fixDiv);
  fixDiv();

});
