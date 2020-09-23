$(document).ready(function () {
    $('.sidebar-collapse').on('click', function () {
        $('.sidebar').toggleClass('active');
        $('.sidebar-collapse').toggleClass('active');
    });
});
