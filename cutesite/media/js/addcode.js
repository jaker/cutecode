$(document).ready(function () {
  $("label").inFieldLabels();

  jQuery.each(jQuery.browser, function(i, val) {
    if(i=="mozilla" && jQuery.browser.version.substr(0,5)=="1.9.0") {
      // Figure out something for Camino 2.1
    } else {
      $('#addcode').borderImage('url(/site_media/images/border.png) 33% round');
    }
    });
});
