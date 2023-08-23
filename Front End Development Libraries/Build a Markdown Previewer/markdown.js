(function () {
  const markdownTextArea = document.getElementById('editor');
  const previewContainer = document.getElementById('preview');

  const defaultMarkdownContent = `# Heading 1
## Heading 2
[Link to Google](https://www.google.com)
\`inline code\`

\`\`\`
// Code block
function add(a, b) {
  return a + b;
}
\`\`\`

- List item 1
- List item 2

> Blockquote

![Image](https://via.placeholder.com/150)  
**Bold Text**`;

  function updatePreview() {
    const markdownContent = markdownTextArea.value;
    const htmlContent = marked(markdownContent, { gfm: true });
    previewContainer.innerHTML = htmlContent;
  }

  markdownTextArea.value = defaultMarkdownContent;
  updatePreview();

  markdownTextArea.addEventListener('input', () => updatePreview());
})();
