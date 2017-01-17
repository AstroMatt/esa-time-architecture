(function($) {
    $(document).ready(function() {

        var thead = $('#changelist thead')[0];
        thead.innerHTML = thead.innerHTML.replace(/:00 - ..:59/g, '');

    });
})(django.jQuery);
