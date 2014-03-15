        $(window).load(function () {
            $('input[type="checkbox"]').each(function (index, item) {
                $(item).hide();
                $(item).after('<div class="checkbox-mine"><span class="checkbox-mine-inside glyphicon glyphicon-ok"></span></div>');
                $(item).change(function () {
                    var chk = $(this);
                    console.log(item);
                    if (chk.is(':checked')) {
                        $(this).siblings().children().animate({
                            opacity: 1.0
                        }, 800);
                    }
                    else {
                        $(this).siblings().children().animate({
                            opacity: 0.0
                        }, 200);
                    }
                });
            });
        });