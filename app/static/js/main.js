$(document).ready(function () {

    // The below applies/removes the zoom class on the nav buttons when the mouse enters/leaves

    $(".btn-main").on("mouseenter", event => {
        $(event.currentTarget).addClass("btn-zoom");
    });

    $(".btn-main").on("mouseleave", event => {
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
        $(".pass-input").append('<label for="password"><strong>New Password</strong></label>').append('<input class="form-control" type="password" name="new-password" id="new-password" minlength="8" required>');
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

});