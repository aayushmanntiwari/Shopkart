var wishlistbutton = document.getElementsByClassName('add-to-wishlist')
for(i = 0;i < wishlistbutton.length;i++){
    wishlistbutton[i].addEventListener('click',function(){
        var varient_id = this.dataset.product
        var product_id = $('#product_id').val()
        var user_check = this.dataset.check
        var action = this.dataset.action
        if (user_check == 'True') {
            console.log(true)
            addtowishlist(varient_id,product_id,user_check,action)
        }
        else {
            alert('Something went wrong !')
        }
    })

}

function addtowishlist(varient_id,product_id,user_check,action){
    var url = '/addtowishlist/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'Accept': 'application/json',
            'X-CSRFToken':csrftoken, /* this is added in order to avoid "csrf forbidden error 403"  becuse in form we passed like this {% csrf_token %} */
        }, 
        /* this will send data as string to views function of url "updateItem" url make sure of positional(postion-wise) arugment will be followed  */
        body:JSON.stringify({'varient_id':varient_id, 'product_id':product_id, 'user_check':user_check,'action':action})
    })
    .then((response) => {
       return response.json();
    })
    .then((data) => {
        location.reload()
    });
}