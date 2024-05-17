const deleteModal = new bootstrap.Modal(document.getElementById("deleteCourseModal"));
const deleteButtons = document.getElementsByClassName("btn-delete-course");
const deleteConfirm = document.getElementById("deleteCourseConfirm");

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