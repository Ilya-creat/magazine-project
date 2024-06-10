const pay = document.querySelector('.payBtn');
pay.addEventListener('click', payment_post);

function payment_post() {
    let vs = document.querySelector('.busketMeals')
    let s = new Array(vs.length);
    console.log(vs.children)
    for(let i = 0; i < vs.children.length; i++){
        console.log(vs.children[i].children[0].innerText)
        s[i] = JSON.stringify(
                {
                    "products": {
                        "id": vs.children[i].id,
                        "name": vs.children[i].children[0].innerText,
                        "count": vs.children[i].children[1].children[1].innerText,
                        "price": vs.children[i].children[2].innerText,
                    },
                }
        )
    }
    $.ajax(
        {
            type: 'post',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            url: "/redirect?page=payment",
            dataType: 'json', // expected returned data format.
            data: JSON.stringify({
                "user": document.querySelector("#name").value,
                "number": document.querySelector("#phone").value,
                "address": document.querySelector("#address").value,
                "order": s
                }
            ),
            method: "post",
            script: "jquery",
            success: function (data) {
            },
            complete: function (data) {

            }
        });
}



