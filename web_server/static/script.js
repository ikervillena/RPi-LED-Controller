$(document).ready(function() {
    $('#scale').on('input', function() {
        var scale = $(this).val();
        $.post('/set_scale', { scale: scale });
    });

    $('#color').on('input', function() {
        var color = $(this).val();
        $.post('/set_color', { color: color });
    });

    $('#random-color-btn').on('click', function() {
        $.post('/set_random_color', function(response) {
            $('#color').val(response);
        });
    });
    $('#send-email-btn').on('click', function() {
    var color = $('#color').val();
    var email = $('#email').val();

    $.post('/send_email', { color: color, email: email }, function(response) {
        console.log(response);
        alert(response);
    });
});
});