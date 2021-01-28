var item = document.getElementsByClassName('delete-wishlistitem')
for(i=0;i<item.length;i++){
    item[i].addEventListener('click',function(){
        var order_id = this.dataset.order
        var user_check = this.dataset.check
        if (user_check == "True") {
            deleteUserOrder(order_id) /* if user is logged in this function will be called */
        }
        else {
            alert('Something went wrong !')
        }
    })
}

function deleteUserOrder(order_id){
    /*Now we want to send varient_id ,action to the Orders views.py updateItem(function) as follow  */
    var url = '/deletewishlistitem/' /* this is the url of views.updateItem which called  updateItem function in views.py */

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken, /* this is added in order to avoid "csrf forbidden error 403"  becuse in form we passed like this {% csrf_token %} */
        }, 
        /* this will send data as string to views function of url "updateItem" url make sure of positional(postion-wise) arugment will be followed  */
        body:JSON.stringify({'order_id':order_id})
    })
    .then((response) => {
       return response.json();
    })
    .then((data) => {
        location.reload()
    });
}