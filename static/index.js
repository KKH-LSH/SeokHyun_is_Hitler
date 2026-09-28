document.addEventListener("DOMContentLoaded", function() {
    var led = document.querySelector("#led");
    var on = document.querySelector("#on");
    var off = document.querySelector("#off");

    on.addEventListener("click", function() {
        $.ajax({
            type: 'GET',
            url: '/on',
        }).done(function(result) {
            led.src = "/static/on.jpeg";
        }).fail(function(result) {
            alert("서버 응답 에러: " + result.status);
        });
    });

    off.addEventListener("click", function() {
        $.ajax({
            type: 'GET',
            url: '/off',
        }).done(function(result) {
            led.src = "/static/offf.jpeg";
        }).fail(function(result) {
            alert("서버 응답 에러: " + result.status);
        });
    });
});