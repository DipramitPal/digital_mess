$(document).ready(function(){

	$("#student-page").click(function(){
		console.log("Student")
		window.location.href = "/student";
	});

	$("#admin-page").click(function(){
		console.log("Admin")
		window.location.href = "/admin";
	});

	$("#food").multiselect();

	function getSelectedValues() {
		var selectedVal = $("#multiselect").val();
			for(var i=0; i<selectedVal.length; i++){
				function innerFunc(i) {
					setTimeout(function() {
						location.href = selectedVal[i];
					}, i*2000);
				}
				innerFunc(i);
			}
		}

});