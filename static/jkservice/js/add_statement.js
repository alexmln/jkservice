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


function add_statement() {
    var company, pa, cwm_1, cwm_2, hwm_1, hwm_2, captcha_0, captcha_1, csrftoken, data;
    data = {
        csrfmiddlewaretoken: getCookie('csrftoken'),
        company: $('input:radio[name=company]:checked').val(),
        pa: $('#id_pa').val(),
        cwm_1: $('#id_cwm_1').val(),
        cwm_2: $('#id_cwm_2').val(),
        hwm_1: $('#id_hwm_1').val(),
        hwm_2: $('#id_hwm_2').val(),
        captcha_0: $('#id_captcha_0').val(),
        captcha_1: $('#id_captcha_1').val()
    }
    $.ajax({
        url: '/add_statement/',
        type: 'POST',
        data: data,
        dataType: 'json',
        beforeSend: function() {
            $('#message').removeClass().text()
        },
        success: function(json) {
            captcha_refresh()
            if (json.status) {
                $('#message').addClass('text-success').text(json.message);
            }
            else {
                $('#message').addClass('text-danger').text(json.message);
            }
        },
        error: function() {
            $(".main-body").html("<h5>Извините произошла ошибка. Мы постараемся исправить ее как можно скорее.</h5>");
        }
    });
}
