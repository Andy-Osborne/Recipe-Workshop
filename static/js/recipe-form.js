$(document).ready(function () {

    /*
    Functions below take the amount of characters the user has inputted into
    the form input for recipe name or description. This calculates the remaining
    characters left and edits HTML to show user this.   
    */

    $("#recipe_name").on("keyup input", event => {
        let recipeName = $(event.currentTarget).val();
        let remaining = 35 - recipeName.length;
        $(".recipe-count").html(remaining);

        if (remaining <= 0) {
            $(".recipe-name-count").addClass("warning");
        } else {
            $(".recipe-name-count").removeClass("warning");
        }
    });

    $("#description").on("keyup input", event => {
        let descriptionName = $(event.currentTarget).val();
        let remaining = 150 - descriptionName.length;
        $(".description-count").html(remaining);

        if (remaining <= 0) {
            $(".recipe-description-count").addClass("warning");
        } else {
            $(".recipe-description-count").removeClass("warning");
        }
    });

    /*
    The below adds an extra line for recipe ingredient/step form in the new_recipe.html
    when the corresponding button is clicked.
    */

    $("#add_ingredient").on("click", () => {
        $("#ingredient").append('<input class="form-control my-2" type="text" name="ingredients" pattern="^[a-zA-Z0-9]+( [a-zA-Z0-9.z\(\)\-\,]+)*$" title="Must start with an uppercase or lowercase word. Acceptable characters are hyphens, commas, periods, and brackets. Cannot start with a space." required>');
    });

    $("#add_step").on("click", () => {
        $("#step_inputs").append('<input class="form-control my-2" type="text" name="step" pattern="^[a-zA-Z0-9]+( [a-zA-Z0-9.z\(\)\-\,]+)*$" title="Must start with an uppercase or lowercase word. Acceptable characters are hyphens, commas, periods, and brackets. Cannot start with a space." required>');
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

    /*
    The below is linked to the manage recipe form and allows the user to upload a new image.
    If the user wants to upload a new image, they can click on the button to upload new image
    which then appends the label and input to the form, adds the relevant enctype to the form/
    If the user presses the cancel button then it removes the above from the form.
    */

    $("#change").on("click", () => {
        $("#current-image").removeClass("d-none");
        $("#recipe_image").attr("required", "required");
        $("#manage-recipe").attr("enctype", "multipart/form-data");
        $("#cancel-change").removeClass("d-none");
        $("#change-image-text").addClass("d-none");
        $("#change").addClass("d-none");
    });

    $("#cancel-change").on("click", () => {
        $("#current-image").addClass("d-none");
        $("#recipe_image").removeAttr("required", "required");
        $("#manage-recipe").removeAttr("enctype", "multipart/form-data");
        $("#cancel-change").addClass("d-none");
        $("#change-image-text").removeClass("d-none");
        $("#change").removeClass("d-none");
    });

});