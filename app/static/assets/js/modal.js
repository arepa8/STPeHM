//JQuery para pasar la informacion al views de eliminar usuario

$(function(){
    $("#deleteButton").click(function(){
        $("#myModal").hide();

        var ci = $("#delete_user").val();
        console.log(ci);
        
        $.ajax({
          type: 'POST',
          url: '/delete_user',
          data: JSON.stringify(ci),
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
});


// Funciones para controlar la aparicion del modal
// Get the modal
var modal = document.getElementById('myModal');
// Get the button that opens the modal
var btn = document.getElementById("delete_user");
// Get the button that closes the modal
var cancel = document.getElementById("cancel_delete");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}
// When the user clicks on the button, close the modal 
cancel.onclick = function() {
    modal.style.display = "none";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
