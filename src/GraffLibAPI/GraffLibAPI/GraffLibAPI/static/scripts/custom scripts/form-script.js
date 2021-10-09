$("#form").submit(function (event) {
    var url = window.location.href; // or window.location.href for current url
    var captured = url.split("?token=")[1]
    var result = captured ? captured : "defaultTokenValue";

    document.getElementById("token").value = result;
    document.getElementById("newPasswordRepeatInput").removeAttribute('name');
});