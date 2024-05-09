const editButtons = document.getElementsByClassName("btn-edit");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated course's ID upon click.
* - Fetches the content of the corresponding course.
* - Populates the `courseText` input/textarea with the course's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_course/{courseId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let courseId = e.target.getAttribute("course_id");
    let courseContent = document.getElementById(`course${courseId}`).innerText;
    courseText.value = courseContent;
    submitButton.innerText = "Update";
    courseForm.setAttribute("action", `edit_course/${courseId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated course's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific course.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let courseId = e.target.getAttribute("course_id");
      deleteConfirm.href = `delete_course/${courseId}`;
      deleteModal.show();
    });
  }