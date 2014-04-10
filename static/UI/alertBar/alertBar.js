/*
 *Easy Usage :
 * 1-include js and css in page After Jquery File
 * 2-call window.alertBar(Error Message Text);
 * attention : This function is not designed for displaying html messages and invoking alertBar with Html Text Content
 * can lead you to unexpected behavior :-S
 * */


$("body").prepend("<div class='alertBar'></div>");
window.alertbarBox = $(".alertBar");
alertbarBox.mouseover(function () {
    alertbarBox.stop().css("opacity", "1")
});
alertbarBox.mouseout(function () {
    setTimeout(function () {
        alertbarBox.animate(
            {
                "opacity": "0.0"
            }
            , 1000, function () {
                alertbarBox.hide()
            }
        )
    }, 2000)
});
console.log(alertbarBox);
var alertBar = function (text) {
    alertbarBox.html(text);
    alertbarBox.show()
        .animate(
        {
            "opacity": "1.0"
        }
        , 1000, function () {
            setTimeout(function () {
                alertbarBox.animate(
                    {
                        "opacity": "0.0"
                    }
                    , 1000, function () {
                        alertbarBox.hide()
                    }
                )
            }, 1000)
        })
}

