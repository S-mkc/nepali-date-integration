function replaceCustomWorkspaceIcon() {
  const customIconPath = "/assets/nepali_date/icon/Yarsa Color Logo.svg";
  const targetHref = `#icon-${customIconPath}`;

  document.querySelectorAll('svg.icon use').forEach((useTag) => {
    const href = useTag.getAttribute('href');
    if (href === targetHref) {
      const svg = useTag.closest('svg');
      const container = svg?.closest('.sidebar-item-icon');
      if (container && !container.querySelector('img')) {
        container.style.marginRight = "8px";
        container.innerHTML = `<img src="${customIconPath}" style="width: 22px; height: 22px;" />`;
      }
    }
  });
}

// Call once initially after page loads
frappe.after_ajax(() => {
  setTimeout(replaceCustomWorkspaceIcon, 1000);
});

// Call again after any route change
frappe.router.on('change', () => {
  setTimeout(replaceCustomWorkspaceIcon, 1000);
});
