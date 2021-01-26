if($(window).width()<768){
    $(".logout-show").addClass("logout-hide");
} 
else {
    $(".logout-show").removeClass("logout-hide");
}


$(window).resize(function(){
    if($(window).width()<768){
          $(".logout-show").addClass("logout-hide");
      } 
      else {
          $(".logout-show").removeClass("logout-hide");
      }
  });