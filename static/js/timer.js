document.addEventListener("DOMContentLoaded", () => {
  const timer = document.getElementById("timer");
  const form = document.getElementById("exam-form");
  if (!timer || !form) return;
  let remaining = Number(timer.dataset.minutes || 10) * 60;
  const update = () => {
    const minutes = Math.floor(remaining / 60);
    const seconds = remaining % 60;
    timer.textContent = `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
    if (remaining <= 60) timer.classList.add("urgent");
    if (remaining <= 0) {
      clearInterval(interval);
      alert("Time is up. Your examination will be submitted now.");
      form.submit();
      return;
    }
    remaining -= 1;
  };
  update();
  const interval = setInterval(update, 1000);
});
