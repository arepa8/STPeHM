$("#show-add-role").click(function(){
	$('.show-add-role').css('display','block');
});

$("#show-view-role").click(function(){
	$('.show-view-role').css('display','block');
});

$("#add-role").click(function(){
	var rol = $('#role').val();
	$.ajax({
          type: 'POST',
          url: '/add_role',
          data: JSON.stringify(rol),
          contentType:'application/json; charset=utf-8',

          success: function(response) {
              console.log(response);
              window.location.reload(true);
          },
          error: function(error) {
              console.log(error);
          }
      });
});
