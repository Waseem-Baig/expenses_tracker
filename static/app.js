// Enhanced JavaScript for Expense Tracker
document.addEventListener("DOMContentLoaded", function () {
  // Auto-set today's date in the add form
  const dateInput = document.querySelector('input[name="date"]');
  if (dateInput && !dateInput.value) {
    dateInput.value = new Date().toISOString().split("T")[0];
  }

  // Animate cards on load
  document.querySelectorAll(".card").forEach((card, index) => {
    card.style.animationDelay = `${index * 0.1}s`;
    card.classList.add("fade-in-up");
  });

  // Add loading states to forms
  document.querySelectorAll("form").forEach((form) => {
    form.addEventListener("submit", function (e) {
      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML =
          '<i class="fas fa-spinner fa-spin"></i> Processing...';
        submitBtn.disabled = true;

        // Re-enable after a delay (in case of validation errors)
        setTimeout(() => {
          submitBtn.innerHTML = originalText;
          submitBtn.disabled = false;
        }, 3000);
      }
    });
  });

  // Add hover effects to table rows
  document.querySelectorAll(".table tbody tr").forEach((row) => {
    row.addEventListener("mouseenter", function () {
      this.style.transform = "scale(1.01)";
      this.style.transition = "transform 0.2s ease";
    });

    row.addEventListener("mouseleave", function () {
      this.style.transform = "scale(1)";
    });
  });

  // Category input suggestions
  const categoryInput = document.querySelector('input[name="category"]');
  if (categoryInput) {
    const suggestions = [
      "Food",
      "Transport",
      "Entertainment",
      "Utilities",
      "Shopping",
      "Health",
      "Education",
      "Travel",
      "Bills",
      "Other",
    ];

    // Create datalist for suggestions
    const datalist = document.createElement("datalist");
    datalist.id = "category-suggestions";
    suggestions.forEach((suggestion) => {
      const option = document.createElement("option");
      option.value = suggestion;
      datalist.appendChild(option);
    });

    categoryInput.setAttribute("list", "category-suggestions");
    categoryInput.parentNode.appendChild(datalist);
  }

  // Smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });

  // Add tooltip functionality
  document.querySelectorAll("[title]").forEach((element) => {
    element.addEventListener("mouseenter", function () {
      const tooltip = document.createElement("div");
      tooltip.className = "tooltip";
      tooltip.textContent = this.getAttribute("title");
      tooltip.style.cssText = `
                position: absolute;
                background: var(--dark-bg);
                color: white;
                padding: 8px 12px;
                border-radius: 6px;
                font-size: 0.8rem;
                z-index: 1000;
                pointer-events: none;
                box-shadow: var(--shadow-md);
            `;
      document.body.appendChild(tooltip);

      const rect = this.getBoundingClientRect();
      tooltip.style.left =
        rect.left + rect.width / 2 - tooltip.offsetWidth / 2 + "px";
      tooltip.style.top = rect.top - tooltip.offsetHeight - 8 + "px";
    });

    element.addEventListener("mouseleave", function () {
      const tooltip = document.querySelector(".tooltip");
      if (tooltip) {
        tooltip.remove();
      }
    });
  });

  // Add keyboard shortcuts
  document.addEventListener("keydown", function (e) {
    // Ctrl/Cmd + Enter to submit forms
    if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      const activeForm = document.activeElement.closest("form");
      if (activeForm) {
        activeForm.submit();
      }
    }

    // Escape to clear filters
    if (e.key === "Escape") {
      const filterForm = document.querySelector(".filter-form");
      if (filterForm) {
        filterForm.reset();
      }
    }
  });

  // Add real-time validation
  document.querySelectorAll('input[name="amount"]').forEach((input) => {
    input.addEventListener("input", function () {
      const value = parseFloat(this.value);
      if (value && value <= 0) {
        this.style.borderColor = "var(--danger-color)";
        this.title = "Amount must be positive";
      } else {
        this.style.borderColor = "var(--success-color)";
        this.title = "";
      }
    });
  });

  // Initialize theme toggle if user prefers dark mode
  if (
    window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches
  ) {
    document.body.classList.add("dark-theme");
  }

  console.log(
    "💰 Expense Tracker UI Enhanced! Welcome to your financial dashboard."
  );
});
