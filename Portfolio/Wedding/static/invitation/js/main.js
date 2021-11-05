

$(function() {
  // ハンバーガーメニュー
  $('.hamburger').click(function() {
      // $(this).toggleClass('active');

      if ($(this).hasClass('active')) {
        $(this).removeClass('active');
        $('.menu-content').removeClass('active');
      } else {
        $(this).addClass('active');
        $('.menu-content').addClass('active');
      }
  });
  
  $('main').click(function() {
    if ($('.hamburger').hasClass('active')) {
      $('.hamburger').removeClass('active');
      $('.menu-content').removeClass('active');
    }
  });

});