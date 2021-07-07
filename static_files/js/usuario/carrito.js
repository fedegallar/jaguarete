$(document).ready(function(){
    if($('#message').hasClass("message")){
        M.toast({html: $('#message').text()})
    } else {
        //do that
    }
});