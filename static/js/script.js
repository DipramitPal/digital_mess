$(document).ready(function(){

	$("#student-page").click(function(){
		console.log("Student")
		window.location.href = "/student";
	});

	$("#admin-page").click(function(){
		console.log("Admin")
		window.location.href = "/admin";
	});



});