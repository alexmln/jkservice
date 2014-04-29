$(document).ajaxStart(function() {
    $("body").addClass("loading");
});

$(document).ajaxStop(function() {
    $("body").removeClass("loading");
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function captcha_refresh() {
    var csrftoken, data;
    data = {
        csrfmiddlewaretoken: getCookie('csrftoken'),
    }
    $.ajax({
        dataType: "json",
        url: /captcha_refresh/,
        data: data,
        success: function(json) {
            $('#id_captcha_0').val(json.key);
            $('.captcha').attr('src', json.image);
            $('#id_captcha_1').val('');
        }
    });
    return false;
}

function send_message() {
    var subject, message, email, csrftoken, data;
    data = {
        csrfmiddlewaretoken: getCookie('csrftoken'),
        subject: $('#subject').val(),
        message: $('#message').val(),
        email: $('#email').val(),
        captcha_0: $('#id_captcha_0').val(),
        captcha_1: $('#id_captcha_1').val()
    }
    $.ajax({
        url: '/feedback/send_message/',
        type: 'POST',
        data: data,
        dataType: 'json',
        beforeSend: function() {
            $('#report').removeClass().text()
        },
        success: function(json) {
            captcha_refresh();
            if (json.status) {
                $('#report').addClass('text-success').text(json.message);
            }
            else {
                $('#report').addClass('text-danger').text(json.message);
            }
        },
        error: function() {
            $(".main-body").html("<h5>Извините произошла ошибка. Мы постараемся исправить ее как можно скорее.</h5>");
        }
    });
}