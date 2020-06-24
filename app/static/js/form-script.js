window.onload = function enableDisableButton() {
  const inputs = document.querySelectorAll("input");
  const form = document.querySelector("form");
  const submitInput = document.querySelector(".button input");

  submitInput.disabled = true;

  function onChange() {
    const formButton = document.querySelector(".button");
    let disable = false;

    for (const element of inputs) {
      if (!element.value || element.value === "") {
        disable = true;
      }
    }

    if (!disable) {
      formButton.classList.remove("disable");
      submitInput.disabled = false;
    }
  }

  function clean() {
    for (const element of inputs) {
      element.removeEventListener("input", onChange);
    }

    form.removeEventListener("submit", clean);
  }

  for (const element of inputs) {
    element.addEventListener("input", onChange);
  }

  form.addEventListener("submit", clean);
};
