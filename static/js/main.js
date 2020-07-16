$(document).ready(function(){
    
    /*
    The below adds an extra line for recipe ingredient/step form in the new_recipe.html
    when the corresponding button is clicked.
    */
    
    $("#add_ingredient").on("click", () => {
        $("#ingredient").append('<input class="form-control" type="text" name="ingredients" required>');
    });

    $("#add_step").on("click", () => {
        $("#step_inputs").append('<input class="form-control" type="text" name="step" required>');
    });
    
    /* 
    The below removes a line for recipe ingredient/step form in the new_recipe.html
    when the corresponding button is clicked.
    */

    $("#remove_ingredient").on("click", () => {
     $("#ingredient input:last-child").remove();   
    });

    $("#remove_step").on("click", () => {
        $("#step_inputs input:last-child").remove();
    });

    // The below applies/removes the zoom class on the nav buttons when the mouse enters/leaves

    $(".btn-sign-up").on("mouseenter", event => {
        $(event.currentTarget).addClass("btn-zoom");
    });

    $(".btn-sign-up").on("mouseleave", event => {
        $(event.currentTarget).removeClass("btn-zoom");
    });

    $(".index-image").on("mouseenter", event => {
        $(event.currentTarget).addClass("index-image-zoom");
    });

    $(".index-image").on("mouseleave", event => {
        $(event.currentTarget).removeClass("index-image-zoom");
    });

    // Below toggles the display of Ingredients / Steps within recipe view on small screen

    $(".toggle-recipe-list").on("click", event => {
        $(event.currentTarget).siblings().slideToggle(400);
    })

    /*
    The below is linked to the manage recipe form and allows the user to upload a new image.
    If the user wants to upload a new image, they can click on the button to upload new image
    which then appends the label and input to the form, adds the relevant enctype to the form/
    If the user presses the cancel button then it removes the above from the form.
    */

    $("#change").on("click", () => {
        $("#current-image").append('<label for="description">Provide an image for this dish</label>');
        $("#current-image").append('<input class="form-control" type="file" name="recipe_image" id="recipe_image" accept="image/*" required>');
        $("#manage-recipe").attr("enctype","multipart/form-data");
        $("#cancel-change").removeClass("d-none");
        $("#change-image-text").addClass("d-none");
        $("#change").addClass("d-none");
    });

    $("#cancel-change").on("click", () => {
        $("#current-image label").remove();
        $("#current-image input").remove();
        $("#manage-recipe").removeAttr("enctype","multipart/form-data");
        $("#cancel-change").addClass("d-none");
        $("#change-image-text").removeClass("d-none");
        $("#change").removeClass("d-none");

    });

    // Below shows profile update form on a new users profile to allow them to update it.
    
    $(".profile-form").on("click", () => {
        $(".profile").toggleClass("d-none");
        $(".new-profile-info").addClass("d-none");
    });

    // The below toggles the required inputs in account management for a user to change their password

    $("#change-pass").on("click", () => {
        $(".email-change").after('<div class="form-group pass-input"></div>');
        $(".pass-input").after('<div class="form-group conf-input"></div>');
        $(".pass-input").append('<label for="password"><strong>New Password</strong></label>').append('<input class="form-control" type="password" name="new-password" id="new-password" required>');
        $(".conf-input").append('<label for="password"><strong>Confirm New Password</strong></label>').append('<input class="form-control" type="password" name="password-conf" id="conf-password" required>');
        $("#cancel-pass").removeClass("d-none");
        $("#change-pass-text").addClass("d-none");
        $("#change-pass").addClass("d-none");
    });

    $("#cancel-pass").on("click", () => {
        $(".pass-input").remove();
        $(".conf-input").remove();
        $("#cancel-pass").addClass("d-none");
        $("#change-pass-text").removeClass("d-none");
        $("#change-pass").removeClass("d-none");

    });

    /*
    The below AJAX function handles the form request for account update and determines the information sent to 
    server as the account update fields are dynamic and then returns if there is any errors and shows
    in the account update MSFIDOCredentialAssertion. In addition, it disabled the default function of
    the submit button 
    */ 

    $("#submit-changes").on("click", function(event) {
        
        let validForm = this.form.checkValidity();

        if (validForm) {
            event.preventDefault();
        
            let user_id = $(this).attr("user_id");
            let email = $("#account-email").val();
            let password = $("#current-password").val();
            let newPassword = $("#new-password").val();
            let confPassword = $("#conf-password").val();

            if (newPassword == "") {
                req = $.ajax({
                    url : '/profile/account_management',
                    type : 'POST',
                    data : {email : email, password : password, user_id : user_id}
                }).done(function(req) {
                    if (req.error) {
                        $("#change-error").text(req.error).removeClass("d-none");
                        $("#change-success").addClass("d-none");
                    }
                    else {
                        $("#change-success").text(req.success).removeClass("d-none");
                        $("#change-error").text(req.error).addClass("d-none");
                    }
                });
            }
            else {
                req = $.ajax({
                    url : '/profile/account_management',
                    type : 'POST',
                    data : {
                        email : email,
                        "new-password" : newPassword,
                        "conf-password" : confPassword, 
                        password : password,
                        user_id : user_id
                    }
                }).done(function(req) {
                    if (req.error) {
                        $("#change-error").text(req.error).removeClass("d-none");
                        $("#change-success").addClass("d-none");
                    }
                    else {
                        $("#change-success").text(req.success).removeClass("d-none");
                        $("#change-error").text(req.error).addClass("d-none");
                    }
                });
            }
        }        
    });
});