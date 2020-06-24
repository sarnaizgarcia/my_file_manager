window.onload = function uploadFileForm() {
  const inputFile = document.querySelector("#file");
  const description = document.querySelector("#description");
  const button = document.querySelector(".button");
  const submitButton = document.querySelector(".button input");
  const form = document.querySelector("form");

  submitButton.disabled = true;

  function onChange() {
    const inputFileEmpty = inputFile.files.length === 0;
    const descriptionEmpty = !description.value || description.value === "";

    if (!inputFileEmpty && !descriptionEmpty) {
      button.classList.remove("disable");
      submitButton.disabled = false;
    }
  }

  function onSubmit() {
    inputFile.removeEventListener("change", onChange);
    description.removeEventListener("change", onChange);
    form.removeEventListener("submit", onSubmit);
  }

  inputFile.addEventListener("change", onChange);
  description.addEventListener("change", onChange);
  form.addEventListener("submit", onSubmit);
};
