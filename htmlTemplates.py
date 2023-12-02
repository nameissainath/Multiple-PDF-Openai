css = '''<style>
.chat-message {
    padding: 1rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
    align-items: center; /* Align items vertically in the center */
    justify-content: flex-start; /* Start alignment horizontally */
}

.chat-message.user, .chat-message.bot {
    background-color: #475063; /* Same background for consistency */
    flex-direction: row; /* Keep avatar and message in a row */
}

.chat-message.user {
    background-color: #2b313e; /* Different background color for user messages */
}

.chat-message .avatar {
    flex-shrink: 0; /* Prevent the avatar from shrinking */
    margin-right: 1rem; /* Space between avatar and message */
    width: 50px; /* Fixed width for avatars */
    height: 50px; /* Fixed height for avatars */
}

.chat-message .avatar img {
    max-width: 100%; /* Ensure avatar image fills the container */
    border-radius: 50%; /* Circular avatars */
}

.chat-message .message {
    flex-grow: 1; /* Allow the message to take up remaining space */
    color: #fff;
    font-size: 0.9rem; /* Adjust font size for readability */
    padding: 0.5rem 1rem; /* Padding inside the message bubble */
}
</style>


'''

bot_template = '''
<div class="chat-message bot">
    
   {{MSG}}
</div>
'''

user_template = '''
<div class="chat-message user">
      
    {{MSG}}
</div>
'''

