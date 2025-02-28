import streamlit as st

st.title("Mindset Growth Challenge:")

st.header("Growth Mindset Challenge: Streamlit Web App")
st.write("A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes. It reminds us that every challenge is an opportunity to learn and improve.")

st.header("Today's Growth Mindset Quote")
st.write("Success doesn't come to you, you've got to go to it. ...")

st.header("What is Your Challenge Today?")
user_input = st.text_input("Describe a Challenge You Are Facing Today:")

if user_input:
    st.success(f"You Are Facing: {user_input}. Believe you can and you're halfway there!")
else:
    st.warning("Tell us about your challenge to get started.")

# Reflection
st.header("Reflect on Your Learning")
reflection = st.text_area("Write Your Reflection Here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievements
st.header("Celebrate Your Wins!")
achievements = st.text_input("Share Something You Have Recently Accomplished:")

if achievements:
    st.success(f"Amazing! You Have Achieved: {achievements}")
else:
    st.info("Success is stumbling from failure to failure with no loss of enthusiasm. — Winston Churchill")

# Footer
st.write("---")
st.write('"Success is the result of perfection, hard work, learning from failure, loyalty, and persistence." — Colin Powell')
st.write("Created by Mary Melvin")
