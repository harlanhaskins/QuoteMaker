(function($, console) {

var frontendUrl = "http://cardgage.harlanhaskins.com";
var apiUrl = "http://cardgage.harlanhaskins.com/api/quotes";
var twitterUrl = "http://twitter.com/share";

function getQuote() {
	$.ajax({
		url: apiUrl,
		method: "GET",
		success: function(r) {
			var quote = r.quotes[0];
			$("#quote").html("\""+quote+"\"")
			$("#twitter").attr("href", twitterUrl + "?text=\"" + quote + "\"" + "&hashtags=CardgageQuotes&url=" + frontendUrl);
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
