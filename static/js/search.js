
const search = document.querySelector('.searchButton');
search.addEventListener('click', search_post)
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
                $('.cardContainer').html(data.fragments).trigger('click');
            },
            complete: function (data) {

            }
        });
}
