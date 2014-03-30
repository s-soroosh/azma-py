$(window).load(function () {
    window.image_preview = false;
    $(".exam-img").click(function () {
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
});