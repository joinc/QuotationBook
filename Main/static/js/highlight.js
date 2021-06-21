function highlight(words) {
    words = words.replace("<", "");
	words = words.replace(">", "");
	let text = document.getElementById('quote-content').innerHTML
	let reg = new RegExp(words, 'gi');
	let result = text.replace(reg, function(str) {
	    return "<div class='highlight'>" + str + "</div>"
	});
	document.getElementById('quote-content').innerHTML = result;
}
