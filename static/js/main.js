$(document).ready(function(){
    
    // The below adds an extra line for a recipe ingredient to the new_recipe.html
    // when the corresponding button is clicked.
    
    $("#add_ingredient").on("click", () => {
        $("#ingredient").append('<input class="form-control" type="text" name="ingredients">');
    });

    // The below removes the last recipe ingredient input when the corresponding button is clicked.

    $("#remove_ingredient").on("click", () => {
     $("#ingredient input:last-child").remove();   
    });

    $("#add_step").on("click", () => {
        $("#step_inputs").append('<input class="form-control" type="text" name="step">');
    });

    $("#remove_step").on("click", () => {
        $("#step_inputs input:last-child").remove();
    });
});