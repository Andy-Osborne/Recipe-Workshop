$(document).ready(function(){
    
    /*
    The below adds an extra line for recipe ingredient/step form in the new_recipe.html
    when the corresponding button is clicked.
    */
    
    $("#add_ingredient").on("click", () => {
        $("#ingredient").append('<input class="form-control" type="text" name="ingredients">');
    });

    $("#add_step").on("click", () => {
        $("#step_inputs").append('<input class="form-control" type="text" name="step">');
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

    
});