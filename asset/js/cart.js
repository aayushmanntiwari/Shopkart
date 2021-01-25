var cartbutton = document.getElementsByClassName('update-cart')
for(i = 0;i<cartbutton.length;i++){
    cartbutton[i].addEventListener('click', function(){
        var varient_id = this.dataset.product /* this is how we get custom attribute value */
        var action = this.dataset.action /* this is how we get custom attribute value */
        var user_check = this.dataset.check
        var quantity = $('#quantity').val()
        var product_id = $('#product_id').val()
        if (user_check == "True") {
            updateUserOrder(varient_id,action,user_check,quantity,product_id) /* if user is logged in this function will be called */
        }
        else {
            alert('Something went wrong !')
        }
    })
}




function updateUserOrder(varient_id,action,user_check,quantity,product_id){
        /*Now we want to send varient_id ,action to the Orders views.py updateItem(function) as follow  */
		var url = '/updateItem/' /* this is the url of views.updateItem which called  updateItem function in views.py */

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken, /* this is added in order to avoid "csrf forbidden error 403"  becuse in form we passed like this {% csrf_token %} */
            }, 
            /* this will send data as string to views function of url "updateItem" url make sure of positional(postion-wise) arugment will be followed  */
			body:JSON.stringify({'varient_id':varient_id, 'action':action, 'user_check':user_check, 'quantity':quantity, 'product_id':product_id})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}