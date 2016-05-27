//JQuery para pasar la informacion al views de eliminar usuario

$(function(){
    $("#deleteButton_appointment").click(function(){
        $("#myModal").hide();

        var id = $("#deleteButton_appointment").val();
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
var modal = document.getElementById('myModal_appointment');
// Get the button that closes the modal
var cancel_appointment = document.getElementById("cancel_delete_appointment");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, close the modal 
cancel_appointment.onclick = function() {
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
    document.getElementById('deleteButton_appointment').value =  id;
}