/*$(document).ready(function(){
	$('.shuffle').shuffle();
});
$.fn.shuffle=function () {
   var parent = $(".shuffle");
   var divs = parent.children();
   while (divs.length) {
       parent.append(divs.splice(Math.floor(Math.random() * divs.length), 1)[0]);
   };
};
*/
$(document).ready(function(){ 
    $('button').click(function() { 
       $(this).addClass('active');// use this here
    });
});

$(document).ready(function(){ 
	var loc=window.location.href
	loc=loc.split("/")
	for(i=1;i<=10;i++)

	{
		var e= $("<a href='/"+loc[3]+i+"/"+i+".html/' target='_blank' class='btn btn-circle' style='color: red;''><i style='color: #fc299f;'>♥</i></a>")
		$("#pagination").append(e)
		
	}

});