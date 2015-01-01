(function($, console) {

var frontendUrl = "http://homsar.harlanhaskins.com";
var apiUrl = "http://cardgage.harlanhaskins.com/api/quotes/homsar";
var twitterUrl = "http://twitter.com/share";
var facebookUrl = "http://www.facebook.com/sharer.php";

function getQuote() {
	$.ajax({
		url: apiUrl,
		method: "GET",
		success: function(r) {
			var quote = r.quotes[0];
			$("#quote").html("\""+quote+"\"")
			$("#twitter").attr("href", twitterUrl + "?text=\"" + quote + "\"&hashtags=HomsarQuotes&url=" + frontendUrl);
			$("#facebook").attr("href", facebookUrl + "?t=" + quote + "&u=" + frontendUrl);
		},
		error: function(e) {
			console.error(e);
			$("#quote").html("ERROR GETTING QUOTE");
		}
	})
}

$(document).on("ready", function(e) {
	getQuote();
	$("#generate").on("click", getQuote);
});

})(jQuery, window.console);
