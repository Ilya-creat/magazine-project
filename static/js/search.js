
const search = document.querySelector('.searchButton');
search.addEventListener('click', search_post);

function showStuff(id, bool) {
    console.log(id, bool, "#test-" + id, document.querySelector("#test-" + id));
    if (bool === false)
        document.querySelector("#test-" + id).style.display = 'none';
    else
        document.querySelector("#test-" + id).style.display = 'block';
}

function search_post() {
    $.ajax(
        {
            // Post the variable fetch to url.
            type: 'post',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            url: "/api/search",
            dataType: 'json', // expected returned data format.
            data: JSON.stringify(
                {
                    "text": $('#video-url').val(),
                }
            ),
            method: "post",
            script: "jquery",
            success: function (data) {

                for(let i = 0; i < data.products.length; i++){
                    showStuff(data.products[i].id, data.products[i].bool);
                }
            },
            complete: function (data) {

            }
        });
}
