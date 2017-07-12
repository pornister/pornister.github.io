$(document).ready(function(){
	$('.shuffle').shuffle();
});
$.fn.shuffle=function () {
   var parent = $(".shuffle");
   var divs = parent.children();
   while (divs.length) {
       parent.append(divs.splice(Math.floor(Math.random() * divs.length), 1)[0]);
   };
};
$(document).ready(function(){ 
    $('button').click(function() { 
       $(this).addClass('active');// use this here
    });
});