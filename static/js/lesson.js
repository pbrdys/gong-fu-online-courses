const deleteModal = new bootstrap.Modal(document.getElementById("deleteLessonModal"));
const deleteButtons = document.getElementsByClassName("btn-delete-lesson");
const deleteConfirm = document.getElementById("deleteLessonConfirm");


for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let lessonId = e.target.getAttribute("lesson_id");
    let courseSlug = e.target.getAttribute("course_slug");
    alert(courseSlug + "/delete/" + lessonId);
    deleteConfirm.href = `/courses/${courseSlug}/delete/${lessonId}/`;
    deleteModal.show();
  });
}