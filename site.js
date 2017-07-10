<script type="text/javascript">
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
</script>