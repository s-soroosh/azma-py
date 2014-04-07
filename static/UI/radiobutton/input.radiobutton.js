$(window).load(function () {
    $('input[type="radio"]').each(function (index, item) {
        var $item = $(item);
        $item.hide();
        $item.after('<div class="radio-mine"><span class="radio-mine-inside glyphicon glyphicon-pushpin"></span></div>');
        $item.change(function () {

            var rdo = $(this);
            var
                rdo_name = rdo.attr('name'),
                rdo_id = rdo.attr('id');

            $('input[name="' + rdo_name + '"]').each(function (index, item) {
                var rdo = $(item);
                if (rdo.is(':checked')) {
                    rdo.siblings().children().animate({
                        opacity: 1.0
                    }, 800);
                }
                else {
                    rdo.siblings().children().animate({
                        opacity: 0.0
                    }, 200);
                }

            });
        });

        var rdo = $(item);
        if (rdo.is(':checked')) {
            rdo.siblings().children().animate({
                opacity: 1.0
            }, 800);
        }
        else {
            rdo.siblings().children().animate({
                opacity: 0.0
            }, 200);
        }

    });
});