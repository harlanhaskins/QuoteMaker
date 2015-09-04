(function($, console) {

var twitterUrl = "http://twitter.com/share";
var facebookUrl = "http://www.facebook.com/sharer.php";

$.fn.getQuote = function () {
    $.ajax({
        url: apiUrl,
        method: "GET",
        success: function(r) {
            var quote = r.quotes[0];
            $("#quote").html("\""+quote+"\"");
            $(this).populateSocialMedia();
        },
        error: function(e) {
            console.error(e);
            $("#quote").html("ERROR GETTING QUOTE");
        }
    });
};

$.fn.populateSocialMedia = function () {
    var quote = $.trim($('#quote').html());
    $("#twitter").attr("href", twitterUrl + "?text=" + quote + "&hashtags=QuoteMaker&url=" + frontendUrl);
    $("#facebook").attr("href", facebookUrl + "?t=" + quote + "&u=" + frontendUrl);
};

$(document).ready(function() {
    $(this).populateSocialMedia();
});

})(jQuery, window.console);


