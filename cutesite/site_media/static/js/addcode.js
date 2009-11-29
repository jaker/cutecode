$(document).ready(function () {
  $("label").inFieldLabels();
//  $("#id_source").addClass("bespin");

  jQuery.each(jQuery.browser, function(i, val) {
    if(i=="mozilla" && jQuery.browser.version.substr(0,5)=="1.9.0") {
      // Figure out something for Camino 2.1
    } else {
      $('#addcode').borderImage('url(/site_media/static/images/border.png) 33% round');
    }
    });



});

// var _editorComponent;

// dojo.addOnLoad(function() {
//   _editorComponent = new bespin.editor.Component('editor', {
//     syntax: "js",
//     loadfromdiv: true
//   });
// });
