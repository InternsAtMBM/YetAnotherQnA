/**
 * Created by zuck007 on 7/15/16.
 */

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function(){
    console.log("first");
    $("#question-vote-up").click(function(){
        console.log("ok first");
        $.ajax({
            type: "POST",
            url: '{% url "forum:question_rating" question.id 1 %}',
            success: function(result){
                console.log(result);
                window.location.reload();

            },
            headers:{
                'X-CSRFToken': getCookie('csrftoken'),
            },
            error: function(rs,e) {
                console.log("error");
                console.log(rs);
            },
            async:false

        });
    });
    $("#question-vote-down").click(function(){
        $.ajax({
            type: "POST",
            url: '{% url "forum:question_rating" question.id -1 %}',
            success: function(result){
                console.log(result);
                window.location.reload();
            },
            headers:{
                'X-CSRFToken': getCookie('csrftoken'),
            },
            error: function(rs,e) {
                console.log("error");
                console.log(rs);
            },
            async: false
        });
    });
});