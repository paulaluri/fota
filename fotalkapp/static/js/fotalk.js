var emojis = {":)":"😊", ";)":"😉",":D":"😃",":P":"😋",":p":"😋"};

$(document).ready(function(){
	$(".fota-text").keyup(function(){
		var txt = $(this).val();
		for(var key in emojis){
			txt = txt.replace(key, emojis[key]);
		}
		$(this).val(txt);
	});
});