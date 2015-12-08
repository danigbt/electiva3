//For getting CSRF token
function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
         var cookie = jQuery.trim(cookies[i]);
         // Does this cookie string begin with the name we want?
         if (cookie.substring(0, name.length + 1) == (name + '=')) {
             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
             break;
          }
     }
 }
 return cookieValue;
}

$(function() {

    $("#name,#email,#message,textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function($form, event, errors) {
            
        },
        submitSuccess: function($form, event) {
            
            $("#btnSubmit").attr("disabled", true);
            event.preventDefault();
            console.log("Submit funciona!")

            var csrftoken = getCookie('csrftoken');
            
            
            var name = $("input#name").val();
            var email = $("input#email").val();
            
            var message = $("textarea#message").val();
            var firstName = name; 
            
            if (firstName.indexOf(' ') >= 0) {
                firstName = name.split(' ').slice(0, -1).join(' ');
            }
            $.ajax({
                url: "/",
                type: "POST",
                data: {
                    csrfmiddlewaretoken : csrftoken,
                    name: name,
                    
                    email: email,
                    message: message
                },
                cache: false,
                success: function(json) {
                    console.log(json);
                    
                    $("#btnSubmit").attr("disabled", false);
                    $('#success').html("<div class='alert alert-success'>");
                    $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-success')
                        .append("<strong>Su mensaje ha sido enviado. </strong>");
                    $('#success > .alert-success')
                        .append('</div>');

                    
                    $('#contactForm').trigger("reset");
                },
                error: function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                    
                    $('#success').html("<div class='alert alert-danger'>");
                    $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-danger').append("<strong>Perdón " + firstName + ", el mensaje no pueder ser enviado. Intente más tarde!");
                    $('#success > .alert-danger').append('</div>');
                    
                    $('#contactForm').trigger("reset");
                },
            })
        },
        filter: function() {
            return $(this).is(":visible");
        },
    });

    $("a[data-toggle=\"tab\"]").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });
});

// When clicking on Full hide fail/success boxes
$('#name').focus(function() {
    $('#success').html('');
});
