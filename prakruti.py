import streamlit as st
import numpy as np

# Define the questions and options
questions = {
    "Body size": ["Slim", "Medium", "Large"],
    "Body weight": ["Low", "Medium", "Overweight"],
    "Chin": ["Thin, angular", "Tapering", "Rounded, double"],
    "Cheeks": ["Wrinkled, sunken", "Smooth flat", "Rounded, plump"],
    "Eyes": ["Small, sunken, dry, active, black/brown, nervous", "Sharp, bright, gray, green, yellow/red, sensitive to light", "Big, beautiful, blue, calm, loving"],
    "Nose": ["Uneven shape, deviated septum", "Long pointed, red nose-tip", "Short rounded, button nose"],
    "Lips": ["Dry, cracked, black/brown tinge", "Red, inflamed, yellowish", "Smooth, oily, pale, whitish"],
    "Teeth": ["Stick out, big, roomy, thin gums", "Medium, soft, tender gums", "Healthy, white, strong gums"],
    "Skin": ["Thin, dry, cold, rough, dark", "Smooth, oily, warm, rosy", "Thick, oily, cool, white, pale"],
    "Hair": ["Dry, brown, black, knotted, brittle, scarce", "Straight, oily, blond, gray, red, bald", "Thick, curly, oily, wavy, luxuriant"],
    "Nails": ["Dry, rough, brittle, break easily", "Sharp, flexible, pink, lustrous", "Thick, oily, smooth, polished"],
    "Neck": ["Thin, tall", "Medium", "Big, folded"],
    "Chest": ["Flat, sunken", "Moderate", "Expanded, round"],
    "Belly": ["Thin, flat, sunken", "Moderate", "Big, pot-bellied"],
    "Belly-button": ["Small, irregular, herniated", "Oval, superficial", "Big, deep, round, stretched"],
    "Hips": ["Slender, thin", "Moderate", "Heavy, big"],
    "Joints": ["Cold, cracking", "Moderate", "Large, lubricated"],
    "Appetite": ["Irregular, scanty", "Strong, unbearable", "Slow but steady"],
    "Digestion": ["Irregular, forms gas", "Quick, causes burning", "Prolonged, forms mucus"],
    "Taste": ["Sweet, sour, salty", "Sweet, bitter, astringent", "Bitter, pungent, astringent"],
    "Thirst": ["Changeable", "Surplus", "Sparse"],
    "Elimination": ["Constipation", "Loose", "Thick, oily, sluggish"],
    "Physical Activity": ["Hyperactive", "Moderate", "Slow"],
    "Mental Activity": ["Hyperactive", "Moderate", "Dull, slow"],
    "Emotions": ["Anxiety, fear, uncertainty", "Anger, hate, jealousy", "Calm, greedy, attachment"],
    "Faith": ["Variable", "Extremist", "Consistent"],
    "Intellect": ["Quick but faulty response", "Accurate response", "Slow, exact"],
    "Recollection": ["Recent good, remote poor", "Distinct", "Slow and sustained"],
    "Dreams": ["Quick, active, many, fearful", "Fiery, war, violence", "Lakes, snow, romantic"],
    "Sleep": ["Scanty, broken up, sleeplessness", "Little but sound", "Deep, prolonged"],
    "Speech": ["Rapid, unclear", "Sharp, penetrating", "Slow, monotonous"],
    "Financial": ["Poor, spends on trifles", "Spends money on luxuries", "Rich, good money preserver"]
}

# Initialize dosha score counters
dosha_scores = {
    "VATA": 0,
    "PITTA": 0,
    "KAPHA": 0
}

# Main Streamlit app
if __name__ == '__main__':
    st.title("Ayurvedic Dosha Quiz")

    for question, options in questions.items():
        # Display the question
        st.write(f"**{question}**")

        # Use radio buttons to select an option
        user_answer = st.radio(f"Select an option for {question}", options)

        if user_answer:
            # Update dosha scores based on the user's selection
            if user_answer == options[0]:
                dosha_scores["VATA"] += 1
            elif user_answer == options[1]:
                dosha_scores["PITTA"] += 1
            elif user_answer == options[2]:
                dosha_scores["KAPHA"] += 1

            st.success(f'You selected: {user_answer}')

    st.write("Your Dosha Scores:")
    for dosha, score in dosha_scores.items():
        st.write(f"{dosha}: {score}")

    # Determine the dominant dosha
    dominant_dosha = max(dosha_scores, key=dosha_scores.get)
    st.write(f"Your Dominant Dosha: {dominant_dosha}")

    # Generate a plot of the dosha scores
    doshas = list(dosha_scores.keys())
    scores = list(dosha_scores.values())

    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots()
    ax.bar(doshas, scores)
    ax.set_xlabel("Dosha")
    ax.set_ylabel("Score")
    ax.set_title("Dosha Scores")

    # Display the Matplotlib plot using st.pyplot()
    st.pyplot(fig)
