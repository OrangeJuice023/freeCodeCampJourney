const QUOTES_API_URL = "https://type.fit/api/quotes";

var colors = ['#16a085', '#27ae60', '#2c3e50', '#f39c12', '#e74c3c', '#9b59b6', '#FB6964', '#342224', "#472E32", "#BDBB99", "#77B1A9", "#73A857"];
var currentQuote = '', currentAuthor = '';

function inIframe() {
  try {
    return window.self !== window.top;
  } catch (e) {
    return true;
  }
}

function openURL(url) {
  window.open(url, "Share", "width=550, height=400, toolbar=0, scrollbars=1, location=0, statusbar=0, menubar=0, resizable=0");
}

function getRandomColor() {
  return colors[Math.floor(Math.random() * colors.length)];
}

function updateQuote(quote, author) {
  $("#text").html(`<i class="fas fa-quote-left"></i> ${quote}`);
  $("#author").text(author);
}

function cleanQuoteAuthor(author) {
  // Remove " - type.fit" from the author (if present)
  return author.replace(/\s*-\s*type\.fit$/i, '');
}

function fetchQuote() {
  fetch(QUOTES_API_URL)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      let randomIndex = Math.floor(Math.random() * data.length);
      let quote = data[randomIndex].text;
      let author = data[randomIndex].author || "Unknown";

      currentQuote = quote;
      currentAuthor = cleanQuoteAuthor(author);

      updateQuote(quote, currentAuthor); // Use the cleaned author

      const tweetButton = document.getElementById("twitter-button");
      tweetButton.href = `https://twitter.com/intent/tweet?hashtags=quotes&related=freecodecamp&text=${encodeURIComponent(
        `"${quote}" - ${currentAuthor}`
      )}`;

      const tumblrButton = document.getElementById("tumblr-button");
      tumblrButton.href = `https://www.tumblr.com/widgets/share/tool?posttype=quote&tags=quotes,freecodecamp&caption=${encodeURIComponent(
        currentAuthor
      )}&content=${encodeURIComponent(quote)}&canonicalUrl=https%3A%2F%2Fwww.tumblr.com%2Fbuttons&shareSource=tumblr_share_button`;

      const color = getRandomColor();
      $("html body").animate({ backgroundColor: color, color: color }, 1000);
      $(".button").animate({ backgroundColor: color }, 1000);
    })
    .catch((error) => {
      console.error("Error fetching quote:", error);
    });
}

$(document).ready(function () {
  fetchQuote();

  $('#new-quote').on('click', fetchQuote);

  $('#tweet-quote').on('click', function () {
    if (!inIframe()) {
      openURL(`https://twitter.com/intent/tweet?hashtags=quotes&related=freecodecamp&text=${encodeURIComponent(
        `"${currentQuote}" - ${currentAuthor}`
      )}`);
    }
  });

  $('#tumblr-quote').on('click', function () {
    if (!inIframe()) {
      openURL(`https://www.tumblr.com/widgets/share/tool?posttype=quote&tags=quotes,freecodecamp&caption=${encodeURIComponent(
        currentAuthor
      )}&content=${encodeURIComponent(currentQuote)}&canonicalUrl=https%3A%2F%2Fwww.tumblr.com%2Fbuttons&shareSource=tumblr_share_button`);
    }
  });
});
