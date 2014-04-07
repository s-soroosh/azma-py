        $(window).load(function () {
            $('input[type="checkbox"]').each(function (index, item) {
                var $item = $(item);
                $item.hide();
                $item.after('<div class="checkbox-mine"><span class="checkbox-mine-inside glyphicon glyphicon-ok"></span></div>');

                $item.change(function () {
                    var chk = $(this);
                    if (chk.is(':checked')) {
                        chk.siblings().children().animate({
                            opacity: 1.0
                        }, 800);
                    }
                    else {
                        chk.siblings().children().animate({
                            opacity: 0.0
                        }, 200);
                    }
                });
                var chk = $(item);
                if (chk.is(':checked')) {
                    chk.siblings().children().animate({
                        opacity: 1.0
                    }, 800);
                }
                else {
                    chk.siblings().children().animate({
                        opacity: 0.0
                    }, 200);
                }

            });
        });