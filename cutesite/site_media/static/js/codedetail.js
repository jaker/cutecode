var CodeDetail = {};
var voteUp = $("#doubleplusgood");
var voteDown = $("#ungood");


$(document).ready(function () {
  jQuery.each(jQuery.browser, function(i, val) {
    if(i=="mozilla" && jQuery.browser.version.substr(0,5)=="1.9.0") {
      // Figure out something for Camino 2.1
    } else {
      $('.detail-paper').borderImage('url(/site_media/static/images/border.png) 33% round');
    }
  });

  $("input[type='submit']").addClass("small awesome");

  voteUp.click(CodeDetail.chooseVote);
  voteDown.click(CodeDetail.chooseVote);
});


CodeDetail.chooseVote = function(event) {
  //most effect types need no options passed by default
  var options = {};
  var codeID = $("code.vote-number").attr("id");

  //run the effect
  if (this.id === "doubleplusgood") {
    voteDown.fadeOut("fast",CodeDetail.voteCallback($(this)));


    var postURL = codeID + "/upvote/";
    $.post(postURL, null, CodeDetail.updateScore, "json");
  } else {
    voteUp.fadeOut("fast",CodeDetail.voteCallback($(this)));

    var postDownURL = codeID + "/downvote/";
    $.post(postDownURL, null, CodeDetail.updateScore, "json");
  }
};

CodeDetail.animateVote = function(element) {
 element.animate({
   bottom: "0.5em"}, 500 );
};

//callback function to bring a hidden box back
CodeDetail.voteCallback = function(element){
  CodeDetail.animateVote(element);
};

CodeDetail.updateScore = function(data){
  var newScore = data.score;

  if (data.success == true) {
    var voteNum = $("code.vote-number");
    voteNum.fadeTo("normal", 0.33);
    voteNum.html(newScore.score);
    voteNum.fadeTo("normal", 1.0);
  }
};