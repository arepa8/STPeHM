$("#show-add-role").click(function(){
  hide_modify_role()
	$('.show-add-role').css('display','block');
});

$("#show-view-role").click(function(){
	$('.show-view-role').css('display','block');
});

function hide_add_role(){
    $('.show-add-role').hide();
}

$("#add-role").click(function(){
	var rol = $('#add-role-input').val();
  console.log(rol);
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


function show_modify_role(id,name){
  hide_add_role();
  $('.show-modify-role').css('display','block');
  $('#modify-role-input').val(name);
  $('#modify-role-form').val(id);
};

function hide_modify_role(){
    $('.show-modify-role').hide();
}

$("#modify-role-form").click(function(){
  var id = $('#modify-role-form').val();
  var name = $('#modify-role-input').val();
  console.log(id,name)
  $.ajax({
          type: 'POST',
          url: '/modify_role',
          data: JSON.stringify({id:id,name:name}),
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

function delete_role(id){
  $.ajax({
          type: 'POST',
          url: '/delete_role',
          data: JSON.stringify(id),
          contentType:'application/json; charset=utf-8',

          success: function(response) {
              console.log(response);
              //window.location.reload(true);
          },
          error: function(error) {
              console.log(error);
          }
      });
};

