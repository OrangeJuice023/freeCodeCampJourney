document.addEventListener("DOMContentLoaded", () => {
  let sessionLength = 25;
  let breakLength = 5;
  let isRunning = false;
  let interval;

  // Helper function to format time in mm:ss
  const formatTime = (time) => {
    const minutes = Math.floor(time / 60).toString().padStart(2, "0");
    const seconds = (time % 60).toString().padStart(2, "0");
    return `${minutes}:${seconds}`;
  };

  // Helper function to update the timer display
  const updateTimer = () => {
    document.getElementById("time-left").textContent = formatTime(sessionLength * 60);
  };

  // Helper function to update break length and display
  const updateBreakLength = (value) => {
    breakLength = Math.min(60, Math.max(1, breakLength + value));
    document.getElementById("break-length").textContent = breakLength;
  };

  // Helper function to update session length and display
  const updateSessionLength = (value) => {
    sessionLength = Math.min(60, Math.max(1, sessionLength + value));
    document.getElementById("session-length").textContent = sessionLength;
    updateTimer();
  };

  // Helper function to toggle the timer (start/pause)
  const toggleTimer = () => {
    if (isRunning) {
      clearInterval(interval);
    } else {
      interval = setInterval(() => {
        if (sessionLength === 0) {
          // Switch between session and break
          if (document.getElementById("timer-label").textContent === "Session") {
            document.getElementById("timer-label").textContent = "Break";
            sessionLength = breakLength;
          } else {
            document.getElementById("timer-label").textContent = "Session";
            sessionLength = document.getElementById("session-length").textContent;
          }
          // Play audio when timer reaches 00:00
          document.getElementById("beep").play();
        } else {
          sessionLength -= 1;
        }
        updateTimer();
      }, 1000);
    }
    isRunning = !isRunning;
  };

  // Helper function to reset the timer to default state
  const resetTimer = () => {
    clearInterval(interval);
    isRunning = false;
    sessionLength = 25;
    breakLength = 5;
    document.getElementById("timer-label").textContent = "Session";
    updateTimer();
    document.getElementById("break-length").textContent = breakLength;
    document.getElementById("session-length").textContent = sessionLength;
    document.getElementById("beep").pause();
    document.getElementById("beep").currentTime = 0;
  };

  // Event listeners for button clicks
  document.getElementById("break-decrement").addEventListener("click", () => updateBreakLength(-1));
  document.getElementById("break-increment").addEventListener("click", () => updateBreakLength(1));
  document.getElementById("session-decrement").addEventListener("click", () => updateSessionLength(-1));
  document.getElementById("session-increment").addEventListener("click", () => updateSessionLength(1));
  document.getElementById("start_stop").addEventListener("click", toggleTimer);
  document.getElementById("reset").addEventListener("click", resetTimer);

  // Initial timer display
  updateTimer();
});
