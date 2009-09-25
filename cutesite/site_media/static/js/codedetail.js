$(document).ready(function () {
      jQuery.each(jQuery.browser, function(i, val) {
      if(i=="mozilla" && jQuery.browser.version.substr(0,5)=="1.9.0") {
        // Figure out something for Camino 2.1
      } else {
        $('.detail-paper').borderImage('url(/site_media/images/border.png) 33% round');
      }
      });
});
