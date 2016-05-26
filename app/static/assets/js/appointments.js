//JQuery para pasar la informacion al views de eliminar usuario

$(function(){
    $("#deleteButton").click(function(){
        $("#myModal").hide();

        var id = $("#deleteButton").val();
        console.log(id);
        
        $.ajax({
          type: 'POST',
          url: '/delete_appointment',
          data: JSON.stringify(id),
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
// Get the button that closes the modal
var cancel = document.getElementById("cancel_delete");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

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
// When the user clicks on the button, open the modal 
function openModal(id) {
    console.log(id);
    modal.style.display = "block";
    document.getElementById('deleteButton').value =  id;
}