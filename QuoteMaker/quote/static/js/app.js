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
    var hashtag = name.replace(/ /g,'');
    $("#twitter").attr("href", twitterUrl + "?text=" + quote + "&hashtags=" + hashtag + "&url=" + frontendUrl);
    $("#facebook").attr("href", facebookUrl + "?p[title]=" + quote + " " + hashtag+ "&u=" + frontendUrl);
};

$(document).ready(function() {
    $(this).populateSocialMedia();
});

})(jQuery, window.console);


