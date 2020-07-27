$(document).ready(function () {

    // The below disables the ability for a user to submit the same recipe twice upon creation.

    $(".recipe-submit").on("click", function (event) {
        let validForm = this.form.checkValidity();

        if (validForm) {
            event.preventDefault();
            $(this).attr("disabled", "disabled");
            $(this).closest("form").submit();
        }
    });

    /*
    The below AJAX function handles the form request for account update and determines the information sent to 
    server as the account update fields are dynamic and then returns if there is any errors and shows
    in the account update modal. In addition, it disabled the default function of the submit button 
    */

    $("#submit-changes").on("click", function (event) {

        let validForm = this.form.checkValidity();

        $("#change-error").empty().addClass("d-none");
        $("#change-success").empty().addClass("d-none");

        if (validForm) {
            event.preventDefault();

            let user_id = $("#user_id").val();
            let email = $("#account-email").val();
            let password = $("#current-password").val();
            let newPassword = $("#new-password").val();
            let confPassword = $("#conf-password").val();

            if (newPassword == "") {
                req = $.ajax({
                    url: '/profile/account_management',
                    type: 'POST',
                    data: {
                        email: email,
                        password: password,
                        user_id: user_id
                    }
                }).done(function (req) {
                    if (req.error) {
                        $("#change-error").text(req.error).removeClass("d-none");
                        $("#change-success").addClass("d-none");
                    } else {
                        $("#change-success").text(req.success).removeClass("d-none");
                        $("#change-error").text(req.error).addClass("d-none");
                    }
                });
            } else {
                req = $.ajax({
                    url: '/profile/account_management',
                    type: 'POST',
                    data: {
                        email: email,
                        "new-password": newPassword,
                        "conf-password": confPassword,
                        password: password,
                        user_id: user_id
                    }
                }).done(function (req) {
                    if (req.error) {
                        $("#change-error").text(req.error).removeClass("d-none");
                        $("#change-success").addClass("d-none");
                    } else {
                        $("#change-success").text(req.success).removeClass("d-none");
                        $("#change-error").text(req.error).addClass("d-none");
                    }
                });
            }
        }
    });

    /*
    The below AJAX function handles when a user likes or unlikes a recipe and sends the information
    to the backend, then receives a response where it updates the likes value and the html of the
    button.
    */

    $("#react").on("click", function (event) {
        event.preventDefault();
        let url = $(this).attr("href");
        $.ajax({
            url: url,
            type: 'POST',
        }).done((data) => {
            if (data.add) {
                $("#react").html('<i class="fas fa-heart"></i>');
                $("#like-count").text(data.add);
            } else {
                $("#react").html('<i class="far fa-heart"></i>');
                $("#like-count").text(data.remove);
            }
        });
    });

    /*
    The below AJAX function handles when a user signs up for the newsletter 
    */

    $(".btn-news").on("click", function (event) {

        let validForm = this.form.checkValidity();

        if (validForm) {
            event.preventDefault();

            let email = $("#email").val();
            let url = $(this.form).attr("action");

            req = $.ajax({
                url: url,
                type: 'POST',
                data: {
                    email: email,
                }
            }).done(function (req) {
                if (req.error) {
                    $(".newsletter-text").addClass("d-none");
                    $("#newsletter").addClass("d-none");
                    $(".message").text(req.error);
                } else {
                    $(".newsletter-text").addClass("d-none");
                    $("#newsletter").addClass("d-none");
                    $(".message").text(req.success);
                }
            });
        }
    });

});