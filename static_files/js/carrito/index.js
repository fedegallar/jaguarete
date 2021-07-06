$(document).ready(function(){
    $(".eliminar").click(function(){
      $.ajax({
        headers: {'X-CSRFToken': Cookies.get('csrftoken')},
        url: $(this).attr('href'),
        type: 'DELETE',
        success: function(data){
          M.toast({html: 'Se ha eliminado el articulo del carrito',
          classes: 'green'});
          setTimeout(function(){
            location.reload();
          },1200);
        },
        error: function(){
          M.toast({html: 'Hubo un error. Intente mas tarde',
        classes: 'red center'})
        }
      });
    });
    $(".editar").click(function(){
      $('.modal').modal();
      $('.modal').modal('open');
      $.ajax({
        headers: {'X-CSRFToken': Cookies.get('csrftoken')},
        url: $(this).attr('django-url'),
        type: 'GET',
        success: function(data){
          $('.contentForm').html(data);
        },
        error: function(){
          M.toast({html: 'Hubo un error. Intente mas tarde',
        classes: 'red center'})
        }
      });
    });
  });