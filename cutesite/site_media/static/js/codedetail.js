var CodeDetail = {};
CodeDetail.voteUp = $("#doubleplusgood");
CodeDetail.voteDown = $("#ungood");
CodeDetail.selected = "selectedvote";


$(document).ready(function () {
  jQuery.each(jQuery.browser, function(i, val) {
    if(i=="mozilla" && jQuery.browser.version.substr(0,5)=="1.9.0") {
      // Figure out something for Camino 2.1
    } else {
      $('.detail-paper').borderImage('url(/site_media/static/images/border.png) 33% round');
    }
  });

  $("input[type='submit']").addClass("small awesome");

  CodeDetail.voteUp.click(CodeDetail.chooseVote);
  CodeDetail.voteDown.click(CodeDetail.chooseVote);
});


CodeDetail.chooseVote = function(event) {
  //most effect types need no options passed by default
  var options = {};
  var codeID = $("code.vote-number").attr("id");

  //run the effect
  if ($(this).attr("id") === "doubleplusgood") {
    var upAction = "/upvote/";

    // Clear the vote if we already voted up
    if ($(this).hasClass(CodeDetail.selected)) {
      upAction = "/clearvote/";
      $("#vote-buttons > a").removeClass(CodeDetail.selected);
      CodeDetail.voteDown.fadeIn("fast");
    } else {
      CodeDetail.voteDown.fadeOut("fast",CodeDetail.voteCallback($(this)));
    }

    var postURL = codeID + upAction;
    $.post(postURL, null, CodeDetail.updateScore, "json");
    //TODO: Make this code tighter and more generic
  } else {
    var downAction = "/upvote/";

    if ($(this).hasClass(CodeDetail.selected)) {
      downAction = "/clearvote/";
      $("#vote-buttons > a").removeClass(CodeDetail.selected);
      CodeDetail.voteUp.fadeIn("fast");
    } else {
      CodeDetail.voteUp.fadeOut("fast",CodeDetail.voteCallback($(this)));
    }

    var postDownURL = codeID + downAction;
    $.post(postDownURL, null, CodeDetail.updateScore, "json");
  }
};

CodeDetail.animateVote = function(element) {
  element.toggleClass(CodeDetail.selected);
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