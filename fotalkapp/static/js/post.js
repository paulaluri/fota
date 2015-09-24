$(document).ready(function(){
	updateTime();
	window.setInterval(getPosts);
});

$("#postText").keyup(function(event){
    if(event.keyCode == 13){
        var form = $("#postForm");
		var url = form.attr("action");

		$.post(url, form.serialize(), "html").done(function(data){
			$("#postText").val("");
			$(".fota-posts").prepend(data);

			var id = $(data).attr("pid");
			if($(".fota-posts").attr("latest") < id)
				$(".fota-posts").attr("latest", id);
			$(".fota-content[pid='" + id + "']").slideDown(200);
			updateTime();
		});
    }
});

function getPosts(){
	/*var form = $("#postForm");
	var url = form.attr("action");

	$.get(url, "html").done(function(data){
		$("#postText").val("");
		$(".fota-posts").prepend(data);

		var id = $(data).attr("pid");
		if($(".fota-posts").attr("latest") < id)
				$(".fota-posts").attr("latest", id);
		$(".fota-content[pid='" + id + "']").slideDown(200);
		updateTime();
	});*/
}

function updateTime(){
	$(".post-time[type='raw']").each(function(){
		var dt = $(this);
		var datetime = new Date(dt.html()).toLocaleString();
		dt.html(datetime);
		dt.attr("type", "done");
		dt.show();
	});
}