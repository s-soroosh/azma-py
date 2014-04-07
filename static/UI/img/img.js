$(window).load(function () {
    window.image_preview = false;
    var image_width = 200, image_height = 200;//images will be showed with this size
    var $images = $(".exam-img");
    $images.click(function () {
        if (!window.image_preview) {
            window.image_preview = true;
            $("body").append("<div id='preview_sheet'></div>");
            $("#preview_sheet").append("<div class='image-box'></div>")
            $(".image-box").append("<img src='" + $(this).attr("src") + "'/>")

            $("#preview_sheet").click(function () {
                $(this).remove();
                window.image_preview = false;

            });

        }
    });
    $images.each(function (index, item) {
        item = $(item);
        var w = parseFloat(item.css('width'));
        var h = parseFloat(item.css('height'));


        if (w > image_width || h > image_height)
            item.css('width', image_width).css('height', image_height);
        else {
            var diff_width = image_width - w, diff_height = image_height - h;

            item.css("padding-left", diff_width / 2)
                .css("padding-right", diff_width / 2)
                .css("padding-top", diff_height / 2)
                .css("padding-bottom", diff_height / 2);

        }
    })

});