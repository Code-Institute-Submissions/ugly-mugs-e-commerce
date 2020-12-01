$(document).ready(function() {
    // Function to append html 
    
    // Append classes to input fields in allauth forms
    $( "div[id='div_id_login']" ).addClass('account-icon');
    $( "div[id='div_id_password']" ).addClass('security-icon');
    $( "div[id='div_id_email']" ).addClass('email-icon');
    $( "div[id='div_id_email2']" ).addClass('email-icon');
    $( "div[id='div_id_username']" ).addClass('account-icon');
    $( "div[id='div_id_password1']" ).addClass('security-icon');
    $( "div[id='div_id_password2']" ).addClass('security-icon');

    // Append classes to input fields in crispy forms
    $( "div[id='div_id_default_phone_number']" ).addClass('phone-icon');
    $( "div[id='div_id_default_street_address1']" ).addClass('location-icon');
    $( "div[id='div_id_default_street_address2']" ).addClass('location-icon');
    $( "div[id='div_id_default_town_or_city']" ).addClass('location-icon');
    $( "div[id='div_id_default_county']" ).addClass('location-icon');
    $( "div[id='div_id_default_postcode']" ).addClass('location-icon');
    $( "div[id='div_id_default_country']" ).addClass('country-icon');

    // Append classes to input fields in stripe
    $( "div[id='div_id_full_name']" ).addClass('account-icon');
    $( "div[id='div_id_phone_number']" ).addClass('phone-icon');
    $( "div[id='div_id_street_address1']" ).addClass('location-icon');
    $( "div[id='div_id_street_address2']" ).addClass('location-icon');
    $( "div[id='div_id_town_or_city']" ).addClass('location-icon');
    $( "div[id='div_id_county']" ).addClass('location-icon');
    $( "div[id='div_id_postcode']" ).addClass('location-icon');
    $( "div[id='div_id_country']" ).addClass('country-icon');
});

$(document).ready(function() {
    // Append icons to classes
    $(".email-icon").prepend( "<i  class='material-icons'>email</i>" );
    $(".phone-icon").prepend( "<i  class='material-icons'>phone</i>" );
    $(".location-icon").prepend( "<i  class='material-icons'>location_city</i>" );
    $(".account-icon").prepend( "<i  class='material-icons'>account_circle</i>" );
    $(".security-icon").prepend( "<i  class='material-icons'>security</i>" );
    $(".country-icon").prepend( "<i  class='material-icons'>language</i>" );
});
