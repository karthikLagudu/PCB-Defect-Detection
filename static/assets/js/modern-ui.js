(function () {
  "use strict";

  document.documentElement.classList.add("ui-js");

  function initReveals() {
    var items = Array.prototype.slice.call(document.querySelectorAll(".ui-reveal"));

    if (!items.length) return;

    var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    items.forEach(function (item, index) {
      var delay = Number(item.getAttribute("data-reveal-delay"));
      if (!Number.isNaN(delay) && !prefersReducedMotion) {
        item.style.transitionDelay = Math.min(delay, 180) + "ms";
      } else if (!prefersReducedMotion && item.parentElement && item.parentElement.hasAttribute("data-stagger")) {
        item.style.transitionDelay = Math.min((index % 4) * 55, 165) + "ms";
      }
    });

    if (prefersReducedMotion || !("IntersectionObserver" in window)) {
      items.forEach(function (item) { item.classList.add("is-visible"); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -7%", threshold: 0.08 });

    items.forEach(function (item) { observer.observe(item); });
  }

  function initFileDrop() {
    var input = document.querySelector("[data-file-input]");
    var drop = document.querySelector("[data-file-drop]");
    var name = document.querySelector("[data-file-name]");

    if (!input || !drop) return;

    function setName() {
      var file = input.files && input.files[0];
      if (name) name.textContent = file ? file.name : "No file selected";
    }

    ["dragenter", "dragover"].forEach(function (eventName) {
      drop.addEventListener(eventName, function (event) {
        event.preventDefault();
        drop.classList.add("is-dragging");
      });
    });

    drop.addEventListener("dragleave", function () { drop.classList.remove("is-dragging"); });
    drop.addEventListener("drop", function (event) {
      event.preventDefault();
      drop.classList.remove("is-dragging");

      if (event.dataTransfer && event.dataTransfer.files.length) {
        input.files = event.dataTransfer.files;
        input.dispatchEvent(new Event("change", { bubbles: true }));
      }
    });

    input.addEventListener("change", setName);
    setName();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      initReveals();
      initFileDrop();
    });
  } else {
    initReveals();
    initFileDrop();
  }
}());
