$(document).on('change','#post-form',function(e){
			e.preventDefault();
			$.ajax({
				type:'POST',
				/* if no error will be found then this url will be run successfully*/
				url:'/ajaxcolor/',
				data:{
					/* this are the field name when form will be submitted*/
					product_id:$('#product_id').val(),
					varient_size_id:$('#varient_size_id').val(),
					csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
					action:'post',
				},
				data_type:'html',
				success:function (data){
					console.log("success");
					/* this will basically show the data based on the size we selected just below div size-option*/
					$('#appendHere').html(data.rendered_table);
				},
				error: function (data) {
					alert('something went wrong'+data)
				}
			});
});