$(document).ready(function () {

    /*
     * The below function checks that the image that has been uploaded has an acceptable file
     * extension and that the file size is below 2mb. If it is, then it shows a success message.
     * If it does not, then it shows a warning message in the html and disables the submit button. 
     * Upon change to the file input, it clears all messages in the html and removes the disabled attr
     * from the submit button.
     */

    $(".image-upload").on("change", () => {

        $(".submit-btn").removeAttr("disabled", "disabled");
        $(".warning").empty();
        $(".successful").empty();

        let fileCheck = $(".image-upload").val();
        let fileSize = $(".image-upload")[0].files[0].size;
        let extensionCheck = fileCheck.split(".").pop().toLowerCase();

        const extensions = ["jpeg", "jpg", "png"];

        if (extensions.includes(extensionCheck)) {
            if (fileSize <= 2097152) {
                $(".successful").text("Valid Image Uploaded");
            } else {
                $(".warning").text("Maximum file size is 2mb. Please upload a smaller file.");
                $(".submit-btn").attr("disabled", "disabled");
            }

        } else {
            $(".warning").text("File type not allowed. Please use either JPEG, JPG or PNG.");
            $(".submit-btn").attr("disabled", "disabled");
        }
    });

});