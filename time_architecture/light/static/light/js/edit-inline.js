(function($) {
    $(document).ready(function() {
        $('td[class^="field-hour_"]').each(function() {
            var value = this.innerHTML;
            this.innerHTML = '<input class="edit-inline" type="number" max="100" min="0" value="'+value+'">';
        });
    });
})(django.jQuery);
