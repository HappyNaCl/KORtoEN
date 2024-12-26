import axios from "axios";

const uploadBtn = document.getElementById("uploadBtn");
const hangulExt = document.getElementById("hangul-ext");
const englishExt = document.getElementById("english-ext");
const loaders = document.getElementsByClassName("loader");
const docsCheckbox = document.getElementById("document-checkbox");
// loader[0] -> hangul, loader[1] -> english

console.log(import.meta.env.VITE_OCR_API + "/ocr");
uploadBtn.addEventListener("click", async () => {
  const imageFormData = new FormData();
  const image = document.getElementById("fileInput").files[0];
  const isDocs = docsCheckbox.checked;

  imageFormData.append("file", image);
  imageFormData.append("is_document", isDocs);

  for (let loader of loaders) {
    loader.style.display = "block";
  }

  const ocrResponse = await axios
    .post(import.meta.env.VITE_OCR_API + "/ocr", imageFormData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    })
    .catch((err) => {
      console.error("Error uploading file:", err);
    });

  hangulExt.innerText = "";
  loaders[0].style.display = "none";
  for (let text of ocrResponse.data.text) {
    hangulExt.innerText += text + "\n";
  }

  const textFormData = new FormData();
  textFormData.append("text", ocrResponse.data.text);
  const translateResponse = await axios
    .post(import.meta.env.VITE_TRANSLATE_API + "/translate", textFormData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    })
    .catch((err) => {
      console.error("Error translating text:", err);
    });
  loaders[1].style.display = "none";
  englishExt.innerText = "";
  englishExt.innerText = translateResponse.data.translated_text;
});

const fileInput = document.getElementById("fileInput");
const fileNameSpan = document.getElementById("fileName");
const imageResult = document.getElementById("image-result");

fileInput.addEventListener("change", function () {
  if (fileInput.files.length > 0) {
    const file = fileInput.files[0];

    fileNameSpan.textContent = file.name;

    const reader = new FileReader();

    reader.onload = function (e) {
      imageResult.innerHTML = "";

      const img = document.createElement("img");
      img.id = "image-uploaded";
      img.src = e.target.result;

      imageResult.appendChild(img);
    };

    reader.readAsDataURL(file);
  } else {
    fileNameSpan.textContent = "No file chosen, yet.";
    imageResult.textContent = "No image uploaded.";
  }
});

const themeToggle = document.getElementById("theme-toggle");

const savedTheme = localStorage.getItem("theme") || "light";
document.documentElement.setAttribute("data-theme", savedTheme);

themeToggle.style.backgroundColor = getComputedStyle(
  document.documentElement
).getPropertyValue("--button-idle");

themeToggle.addEventListener("click", () => {
  const currentTheme = document.documentElement.getAttribute("data-theme");

  const newTheme = currentTheme === "dark" ? "light" : "dark";

  document.documentElement.setAttribute("data-theme", newTheme);

  localStorage.setItem("theme", newTheme);

  setTimeout(() => {
    const buttonColor = getComputedStyle(document.documentElement)
      .getPropertyValue("--button-idle")
      .trim();
    themeToggle.style.backgroundColor = buttonColor;
  });
});
