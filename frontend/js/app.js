(function($) {

var url = "http://cardkov.harlanhaskins.com/api/quotes";

function getQuote() {
	$.ajax({
		url: url,
		method: "GET",
		success: function(r) {
			var quote = r.quotes[0];
			$("#quote").html("\""+quote+"\"")
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

})(jQuery);
