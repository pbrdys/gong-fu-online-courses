// Initialize delete modal using Bootstrap Modal
const deleteModal = new bootstrap.Modal(document.getElementById("deleteCourseModal"));
// Get all delete buttons
const deleteButtons = document.getElementsByClassName("btn-delete-course");
// Get delete confirmation button
const deleteConfirm = document.getElementById("deleteCourseConfirm");

for (let button of deleteButtons) {
  // Add click event listener to each delete button
  button.addEventListener("click", (e) => {
    let courseId = e.target.getAttribute("course_id");
    // Set the confirmation link with the course ID
    deleteConfirm.href = `delete_course/${courseId}`;
    // Show the delete confirmation modal
    deleteModal.show();
  });
}
