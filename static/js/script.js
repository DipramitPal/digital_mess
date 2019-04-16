$(document).ready(function(){

	$("#student-page").click(function(){
		console.log("Student")
		window.location.href = "/student";
	});

	$("#admin-page").click(function(){
		console.log("Admin")
		window.location.href = "/admin";
	});

	 $('#admintable').DataTable({
	 	"ajax": {
            "url": "/admin/get_students",
            "type": "GET"

        },
        "columns": [
            { "data": "id" },
            { "data": "rollnumber" },
            { "data": "name" },
            { "data": "item" },
            { "data": "verify" },
            
        ]

	 });

	 $("#admintable tbody").on('click','tr',function(){
	 	console.log("hello")

	 });

	$('#admintable tbody').on('click', '.verify_btn',function() {
            var id = $(this).attr('data-id');
            var date = $(this).attr('data-date');
            var name = $(this).attr('data-name');
            var rollnumber = $(this).attr('data-rollnumber');
            // var item = $(this).attr('data-food')
            // console.log()
            $("#id").val(id)
            $("#date").val(date)
            $("#name").val(name)
            $("#rollnumber").val(rollnumber)
            // $("#item").val(item)
           
            $('#verify_confirm').modal('show');
        });
    
    $("#verify_confirm").on('click','.verify_confirm_btn',function(){
    	var id = $("#id").val() 
        var date = $("#date").val() 
        var name = $("#name").val() 
        var rollnumber = $("#rollnumber").val()
        $.ajax({
        	url:'/admin/verify_student',
        	data: JSON.stringify({'id': id}),
        	type: 'POST',
        	success : function(response)
        	{
        		alert(response)
        		$('#verify_confirm').modal('hide');
        		$('#'+rollnumber).attr('disabled','disabled')
        		console.log($('#'+rollnumber).val())
        	}

        });

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