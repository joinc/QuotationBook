function highlight(words) {
    words = words.replace("<", "");
	words = words.replace(">", "");
	let text = document.getElementById('quote-content').innerHTML
	let result = text.replace(new RegExp(words,'g'), "<div style='text-decoration: underline dotted red; display:inline;'>" + words + "</div>");
	document.getElementById('quote-content').innerHTML = result;
}
