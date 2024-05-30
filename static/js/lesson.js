// Initialize delete modal using Bootstrap Modal
const deleteModal = new bootstrap.Modal(document.getElementById("deleteLessonModal"));
// Get all delete buttons for lessons
const deleteButtons = document.getElementsByClassName("btn-delete-lesson");
// Get delete confirmation button
const deleteConfirm = document.getElementById("deleteLessonConfirm");

for (let button of deleteButtons) {
  // Add click event listener to each delete button
  button.addEventListener("click", (e) => {
    let lessonId = e.target.getAttribute("lesson_id");
    let courseSlug = e.target.getAttribute("course_slug");
    // Set the confirmation link with the course slug and lesson ID
    deleteConfirm.href = `/courses/${courseSlug}/delete/${lessonId}/`;
    // Show the delete confirmation modal
    deleteModal.show();
  });
}
