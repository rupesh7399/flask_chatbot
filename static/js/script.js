// Function to send a message to the bot and get a response
function sendMessage() {
    var userMessage = $('#userInput').val();
    if (userMessage.trim() === '') return;

    // Append user message to chatbox
    $('#chatBox').append('<div class="message user-msg">' + userMessage + '</div>');

    // Clear input box
    $('#userInput').val('');

    // Send AJAX request to backend
    $.ajax({
        url: '/get_response',
        type: 'POST',
        data: { 'user_input': userMessage },
        success: function(response) {
            // Append bot's response to chatbox
            $('#chatBox').append('<div class="message bot-msg">' + response.response + '</div>');

            // Scroll to the bottom of the chat
            $('#chatBox').scrollTop($('#chatBox')[0].scrollHeight);
        },
        error: function() {
            alert('Error in communication with server');
        }
    });
}
