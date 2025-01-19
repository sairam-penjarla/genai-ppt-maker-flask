let shouldStopStream = false; // Add this flag to control the streaming
let currentSessionId = null;

window.onload = function () {
  // Clear chat container on page load
  document.getElementById("slides-container").innerHTML = "";
};

document.querySelector(".new-session-button").addEventListener("click", function () {
  location.reload(); // Refresh the page
});

const toggleThemeButton = document.getElementById('theme-toggle');

// Load the preferred theme from localStorage
const currentTheme = localStorage.getItem('theme') || 'light-mode';
document.documentElement.classList.add(currentTheme); // Apply theme to the html tag
toggleThemeButton.textContent = currentTheme === 'dark-mode' ? 'Switch to Light Mode' : 'Switch to Dark Mode';

// Toggle theme on button click
toggleThemeButton.addEventListener('click', () => {
  const html = document.documentElement; // Target the html element
  if (html.classList.contains('dark-mode')) {
    html.classList.replace('dark-mode', 'light-mode');
    toggleThemeButton.textContent = 'Switch to Dark Mode';
    localStorage.setItem('theme', 'light-mode');
    html.style.backgroundColor = "#ffffff"; // Apply background color to html
  } else {
    html.classList.replace('light-mode', 'dark-mode');
    toggleThemeButton.textContent = 'Switch to Light Mode';
    localStorage.setItem('theme', 'dark-mode');
    html.style.backgroundColor = "#252525"; // Apply background color to html
  }
});































/////////////////////////////////////////////////////////
//                  Utility functions                  //
/////////////////////////////////////////////////////////

function generateSessionId() {
  // Using the crypto API to generate a random UUID
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
    const r = (Math.random() * 16) | 0;
    const v = c === "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

function handleKeyPress(event) {
  const sendButton = document.getElementById("sendButton");

  if (event.key === "Enter" && !sendButton.disabled) {
    event.preventDefault();
    generateSlidesFromInputBar();
  }
}

function generateSlidesFromInputBar() {
  const userInput = document.getElementById("userInput");
  const message = userInput.innerText.trim();
  generateSlides(message);
}

function handlePaste(event) {
  event.preventDefault();

  const text = event.clipboardData.getData("text/plain");

  document.execCommand("insertText", false, text);
}

function slideLoadingAnimation() {
  const chatContainer = document.getElementById("slides-container");
  const loadingMessageContainer = document.createElement("div");
  loadingMessageContainer.classList.add("bot-loading-message-container");
  loadingMessageContainer.id = "slide-loading-animation";
  chatContainer.appendChild(loadingMessageContainer);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

function resetSendButton() {
  const slideLoadingAnimationConst = document.getElementById("slide-loading-animation");
  if (slideLoadingAnimationConst) {
    slideLoadingAnimationConst.remove();
  }
  const userInput = document.getElementById("userInput");
  const sendButton = document.getElementById("sendButton");
  const sendIcon = document.getElementById("sendIcon");

  userInput.setAttribute("contenteditable", "true");
  sendButton.disabled = false;
  sendIcon.src = "static/images/arrow-left.svg";
  sendIcon.onclick = null; // Remove the stopStream function from the click event
}

function cleanInput() {
  const userInput = document.getElementById("userInput");
  userInput.innerHTML = userInput.innerHTML.replace(/<span[^>]*>(.*?)<\/span>/g, "$1");
}

function updateSidebarWithSession(sessionId, firstQuestion, session_icon) {
  const sessionList = document.getElementById("session-list");

  // Create the list item for the session
  const sessionItem = document.createElement("li");
  sessionItem.className = "chat-item"; // Set the class name
  sessionItem.setAttribute("session_id", sessionId); // Set the session_id attribute
  sessionItem.onclick = () => loadSessionData(sessionId); // Click handler for the session item

  // Create a div for the emoji container
  const emojiDiv = document.createElement("div");
  emojiDiv.className = "chat-item-emoji"; // Set a class for styling

  // Create the emoji image
  const emojiImage = document.createElement("img");
  emojiImage.className = "emoji-button"; // Add a class for styling
  emojiImage.src = `/static/images/session-icons/${session_icon}`; // Use backticks for template literals

  // Append the emoji image to the emoji container
  emojiDiv.appendChild(emojiImage);

  // Create a div for the session text
  const sessionTextDiv = document.createElement("div");
  sessionTextDiv.className = "chat-item-question"; // Set a class for styling
  sessionTextDiv.textContent = firstQuestion; // Display the first question or a default name

  // Create a div for the delete icon container
  const deleteIconDiv = document.createElement("div");
  deleteIconDiv.className = "chat-item-delete-container"; // Set a class for styling

  // Create the delete icon
  const deleteIcon = document.createElement("img");
  deleteIcon.className = "delete-button"; // Add a class for styling
  deleteIcon.src = "/static/images/delete_black.svg"; // Set the source of the delete icon
  deleteIcon.alt = "Delete"; // Set an alt text for accessibility
  deleteIcon.onclick = (e) => {
    e.stopPropagation(); // Prevent triggering the `onclick` for the session item
    deleteSession(sessionId); // Call the delete function
  };

  // Append the delete icon to the delete icon container
  deleteIconDiv.appendChild(deleteIcon);

  // Create a div for the session indicator
  const indicatorDiv = document.createElement("div");
  indicatorDiv.className = "chat-item-indicator"; // Set a class for styling

  // Append all child elements to the session item
  sessionItem.appendChild(emojiDiv); // Add the emoji container
  sessionItem.appendChild(sessionTextDiv); // Add the session text container
  sessionItem.appendChild(deleteIconDiv); // Add the delete icon container
  sessionItem.appendChild(indicatorDiv); // Add the session indicator

  // Insert the new session item at the top of the list
  sessionList.insertBefore(sessionItem, sessionList.firstChild);
}































/////////////////////////////////////////////////////////
//                  sidebar functions                  //
/////////////////////////////////////////////////////////

async function clearAllChats() {
  // Show confirmation dialog
  const confirmation = confirm("Are you sure you want to clear all chats?");
  if (!confirmation) {
    return; // Exit if the user cancels
  }

  try {
    // Send POST request to Flask backend to delete all sessions
    const response = await fetch("/delete_all_sessions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (response.ok) {
      alert("All sessions have been cleared.");
      location.reload(); // Reload the page to reflect the changes
    } else {
      const errorMessage = await response.text();
      alert("Failed to clear sessions: " + errorMessage);
    }
  } catch (error) {
    console.error("Error clearing sessions:", error);
    alert("An error occurred while clearing sessions. Please try again.");
  }
}

async function deleteSession(sessionId) {
  // Show confirmation dialog
  const confirmation = confirm("Are you sure you want to delete this session?");
  if (!confirmation) {
    return; // Exit if the user cancels
  }

  try {
    // Send POST request to Flask backend to delete the specific session
    const response = await fetch("/delete_session", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ session_id: sessionId }),
    });

    if (response.ok) {
      alert("Session deleted successfully.");
      // Remove the session from the DOM
      const sessionElement = document.querySelector(`[session_id="${sessionId}"]`);
      if (sessionElement) {
        sessionElement.remove();
      }
    } else {
      const errorMessage = await response.text();
      alert("Failed to delete session: " + errorMessage);
    }
  } catch (error) {
    console.error("Error deleting session:", error);
    alert("An error occurred while deleting the session. Please try again.");
  }
}

async function loadSessionData(sessionId) {
  try {
    // Fetch previous conversations from the backend
    const response = await fetch("/get_session_data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        sessionId: sessionId,
      }),
    });
    const data = await response.json(); // Assume the response is in JSON format
    if (data) {
      renderSession(data.session_data, sessionId);
    } else {
      console.log("No conversations found for this session.");
    }
  } catch (error) {
    console.error("Error loading previous conversations:", error);
  }
}

function renderSession(sessionData, sessionId) {
  // Set the current session ID
  currentSessionId = sessionId;

  // Clear the slides container
  const slidesContainer = document.getElementById("slides-container");
  slidesContainer.innerHTML = "";

  // Loop through the session data
  sessionData.forEach((item) => {
    try {
      // Extract key (prompt) and value (dictionary containing slides_content)
      const [prompt, data] = Object.entries(item)[0];

      // Extract slides_content from the data dictionary
      const slidesContent = data.slides_content;

      // Append the user message
      appendUserMessage(prompt);

      // Render the slides content
      renderSlides(slidesContent);
    } catch (error) {
      console.error("Error rendering session data:", error);
    }
  });
}






























/////////////////////////////////////////////////////////
//                  slides functions                  //
/////////////////////////////////////////////////////////

function appendUserMessage(content) {
  const chatContainer = document.getElementById("slides-container");

  const messageContainer = document.createElement("div");
  messageContainer.classList.add("user-message-container");

  // Create the main content wrapper
  const messageContentWrapper = document.createElement("div");
  messageContentWrapper.classList.add("user-message");
  messageContentWrapper.classList.add("message");

  // Create the text content container
  const textContentContainer = document.createElement("div");
  textContentContainer.classList.add("text-content-container");

  textContentContainer.textContent = content;

  // Append the text content and action container to the main content wrapper
  messageContentWrapper.appendChild(textContentContainer);

  // Append the message content wrapper and edit icon container to the message container
  messageContainer.appendChild(messageContentWrapper);

  const allUserMessages = document.createElement("div");
  allUserMessages.classList.add("all-user-messages");
  allUserMessages.appendChild(messageContainer);

  // Append the message container to the chat container
  chatContainer.appendChild(allUserMessages);

  // Scroll to the bottom of the chat container
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

async function generateSlides(message) {
  const userInput = document.getElementById("userInput");
  const sendButton = document.getElementById("sendButton");

  if (message === "") return;

  
  userInput.setAttribute("contenteditable", "false");
  sendButton.disabled = true;
  
  // Append the user message block
  appendUserMessage(message);
  userInput.innerText = "";
  
  // Show a loading animation
  slideLoadingAnimation();

  try {
    const responseAgent = await fetch("/generate_slides", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        session_id: currentSessionId,
        user_input: message,
      }),
    });
    
    if (!responseAgent.ok) {
      console.error("Error:", responseAgent.statusText);
      // Show error message to user
      return;
    }
    
    // Parse the JSON response
    const responseData = await responseAgent.json();
    
    // Check if slides_content exists in the response
    if (responseData.slides_content) {
      if (!currentSessionId) {
        currentSessionId = generateSessionId(); // Generate a new session ID
        updateSidebarWithSession(currentSessionId, message, responseData.session_icon); // Update the sidebar with the new session
      }
      // Send a request to /update_session route.
      await fetch("/update_session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          session_id: currentSessionId,
          prompt: message, // Assuming the prompt is the user message
          slide_planning: responseData.slide_planning,
          slides_content: responseData.slides_content,
          session_icon: responseData.session_icon,
        }),
      });
      // Render all slides
      renderSlides(responseData.slides_content);
    } else {
      console.error("Slides content is missing in the response.");
      // Show error message to user
    }
  } catch (error) {
    console.error("Error during fetch or processing:", error.message);
    // Show error message to user
  } finally {
    resetSendButton();
  }
}

// Function to render slides
function renderSlides(slidesContent) {
  try {
    // Check if slidesContent is a string and convert it to JSON if needed
    if (typeof slidesContent === "string") {
      slidesContent = JSON.parse(slidesContent);
    }

    // Validate if slidesContent is an array
    if (!Array.isArray(slidesContent)) {
      console.error("Invalid slidesContent: Expected an array.");
      return;
    }

    // Loop through slidesContent and send each dictionary to renderSingleSlide
    slidesContent.forEach((slideData, index) => {
      try {
        // Call the function to render a single slide
        renderSingleSlide(slideData.slides[0], index + 1); // Pass slide number starting from 1
      } catch (error) {
        console.error(`Error rendering slide at index ${index}:`, error);
      }
    });
  } catch (error) {
    console.error("Error processing slidesContent:", error);
  }
}

// Function to render a single slide
function renderSingleSlide(slideData, slideNumber) {
  const slidesContainer = document.getElementById("slides-container");

  // Create the main wrapper for this slide
  const parentContainer = document.createElement("div");
  parentContainer.className = "parent-container";

  // Create a container for the slide number and slide content
  const slideContentContainer = document.createElement("div");
  slideContentContainer.className = "slide-content-container";

  // Create slide number div
  const slideNumberDiv = document.createElement("div");
  slideNumberDiv.className = "slide-number";
  slideNumberDiv.textContent = slideNumber;

  // Create the main slide container
  const newSlide = document.createElement("div");
  newSlide.className = "slide";
  newSlide.setAttribute("contenteditable", "false");
  newSlide.setAttribute("data-slide-data", JSON.stringify(slideData)); // Store slideData as a string

  // Add titles section to the slide
  const titlesDiv = document.createElement("div");
  titlesDiv.className = "titles";

  const slideTitle = document.createElement("h1");
  slideTitle.className = "slide-title";
  slideTitle.textContent = slideData.titles.slide_title;

  const longTitle = document.createElement("h2");
  longTitle.className = "long-title";
  longTitle.textContent = slideData.titles.long_title;

  const subTitle = document.createElement("h3");
  subTitle.className = "sub-title";
  subTitle.textContent = slideData.titles.sub_title;

  titlesDiv.appendChild(slideTitle);
  titlesDiv.appendChild(longTitle);
  titlesDiv.appendChild(subTitle);

  // Create content section
  const contentDiv = document.createElement("div");
  contentDiv.className = "content";

  slideData.content.forEach((point) => {
    const pointHeadingDiv = document.createElement("div");
    pointHeadingDiv.className = "point-heading";
    pointHeadingDiv.textContent = point.heading;

    const pointContentDiv = document.createElement("div");
    pointContentDiv.className = "point-content";
    pointContentDiv.textContent = point.content;

    contentDiv.appendChild(pointHeadingDiv);
    contentDiv.appendChild(pointContentDiv);
  });

  // Append titles and content to the slide
  newSlide.appendChild(titlesDiv);
  newSlide.appendChild(contentDiv);

  // Add slide number and slide to the slideContentContainer
  slideContentContainer.appendChild(slideNumberDiv);
  slideContentContainer.appendChild(newSlide);

  // Create the action buttons container
  const actionButtonsContainer = document.createElement("div");
  actionButtonsContainer.className = "action-buttons";

  // Create copy button as an image
  const copyButton = document.createElement("img");
  copyButton.className = "copy-button";
  copyButton.src = "static/images/copy.png";
  copyButton.alt = "Copy";
  copyButton.style.cursor = "pointer"; // Ensure it looks clickable
  copyButton.onclick = () => {
    // Convert slideData to Markdown format
    const slideMarkdown = `# ${slideData.titles.slide_title}
        ## ${slideData.titles.long_title}
        ### ${slideData.titles.sub_title}
        
        ${slideData.content.map((point) => `#### ${point.heading}\n${point.content}`).join("\n\n")}`;

    // Copy the Markdown to the clipboard
    navigator.clipboard
      .writeText(slideMarkdown)
      .then(() => {})
      .catch((error) => {
        console.error("Error copying to clipboard:", error);
      });
  };

  // Create download button as an image
  const downloadButton = document.createElement("img");
  downloadButton.className = "download-button";
  downloadButton.src = "static/images/download.png";
  downloadButton.alt = "Download";
  downloadButton.style.cursor = "pointer"; // Ensure it looks clickable
  downloadButton.onclick = () => displayDownloadPopup(slideData);

  // Append buttons to the action buttons container
  actionButtonsContainer.appendChild(copyButton);
  actionButtonsContainer.appendChild(downloadButton);

  // Append the slideContentContainer and actionButtonsContainer to the parent container
  parentContainer.appendChild(slideContentContainer);
  parentContainer.appendChild(actionButtonsContainer);

  // Append the parent container to the slidesContainer
  slidesContainer.appendChild(parentContainer);
}

// Function to display the download popup
function displayDownloadPopup(slideData) {
  // Create popup container
  const popupContainer = document.createElement("div");
  popupContainer.className = "popup-container";

  // Create popup content
  const popupContent = document.createElement("div");
  popupContent.className = "popup-content";

  // Fetch the thumbnail file names from the server
  fetch("/get_thumbnails", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json()) // Parse JSON response
    .then((data) => {
      const images = data.files; // Extract file names

      images.forEach((image, index) => {
        const imageContainer = document.createElement("div");
        imageContainer.className = "image-container";

        const img = document.createElement("img");
        img.src = `/static/thumbnails/${image}`; // Construct image path
        img.className = "thumbnail-image";
        img.alt = `Image ${index + 1}`;

        const downloadImageButton = document.createElement("img");
        downloadImageButton.className = "download-image-button";
        downloadImageButton.src = "static/images/download.png";
        downloadImageButton.alt = "Download"; // Alt text for accessibility
        downloadImageButton.title = "Download"; // Tooltip when hovered
        downloadImageButton.style.cursor = "pointer"; // Ensure it looks clickable
        downloadImageButton.onclick = () => {
          fetch("/download_slide", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              slideData: JSON.stringify(slideData),
              thumbnail_id: image,
            }),
          })
            .then((response) => response.json()) // Parse JSON response
            .then((data) => {
              if (data.file_path) {
                const link = document.createElement("a");
                link.href = data.file_path; // Server response file path
                link.download = data.file_path.split("/").pop(); // Extract filename for download
                link.click();
              } else {
                alert("Error: File path not found in the server response.");
              }
            })
            .catch((error) => {
              console.error("Error downloading image:", error);
              alert("Error downloading the file.");
            });
        };

        imageContainer.appendChild(img);
        imageContainer.appendChild(downloadImageButton);
        popupContent.appendChild(imageContainer);
      });

      // Add close button to the popup
      const closeButton = document.createElement("button");
      closeButton.className = "close-popup-button";
      closeButton.textContent = "Close";
      closeButton.onclick = () => popupContainer.remove();

      popupContent.appendChild(closeButton);
      popupContainer.appendChild(popupContent);

      // Append popup to the document body
      document.body.appendChild(popupContainer);
    })
    .catch((error) => {
      console.error("Error fetching thumbnails:", error);
      alert("Error loading thumbnails. Please try again.");
    });
}
