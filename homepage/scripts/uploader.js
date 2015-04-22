$(function() {

	$('.upload').on('change', function() {
		var fd = new FormData();
		var file = this.files[0];
		fd.append('uploadfile', file);
		$.ajax({
			url: '/homepage/uploader.upload/',
			type: 'POST',
			contentType: false, //telling jquery not to mess with it
			processData: false, //telling jquery not to mess with it
			data: fd,
			xhr: function() {
				var xhr = jQuery.ajaxSettings.xhr();
				if (xhr.upload) {
					xhr.upload.addEventListener('progress', function(evt) {
						if (evt.lengthComputable) {

							// update the UI
							percentUploaded = parseInt((evt.loaded / evt.total) * 100)

							// console.log(percentUploaded);
							console.log(evt);
							$('.upload_progress').html("Upload Progress: " + parseInt(percentUploaded) + "%")
							//TODO later - add select to only grab the closest progress bar if more than one

						} //if
					}, false); //addEventListener
				} //if
				return xhr;
			}, //xhr
			success: function(data) {
				console.log('success')
				console.log(data)

				$('#id_upload_fullname').val(data);
				$('.upload').remove();
				$('.upload_progress').html("Upload Progress: COMPLETE " + file.name)

			},
			error: function(err) {
				console.log('err')
				console.log(err)

				$('.upload_progress').html("Upload Progress: ERROR please try again.")
			}
		});
	});


	// $('#id_upload').closest('form').off('submit.uploader').on('submit.uploader', function() {
	// 	this.remove()
	// });

});
