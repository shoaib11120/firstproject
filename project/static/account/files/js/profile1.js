

$(document).ready(function(){
  $("#editProfileButton").click(function(){
    $(".innerFormInput").css("border", "2px solid black");
    $(".innerFormInput").prop("disabled", false);
    $("#submitProfileButton").css("display","block")
    $("#photoChooseButton").css("display","block")
    $(".innerPhoto").children().css("display","block")
    $(this).css("display","none")
  });
});