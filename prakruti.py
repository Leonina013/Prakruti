import streamlit as st
import pandas as pd

questions_prakruti = {
    "Body size": ["Slim", "Medium", "Large"],
    "Body weight": ["Low", "Moderate", "Obese"],
    "Chin": ["Thin, angular", "Tapering", "Rounded, double"],
    "Cheeks": ["Wrinkled, sunken", "Smooth flat", "Rounded, plump"],
    "Eyes": ["Small, sunken, dry, active, black/brown, nervous", "Sharp, bright, gray, green, yellow/red, sensitive to light", "Big, beautiful, blue, calm, loving"],
    "Nose": ["Uneven shape, deviated septum", "Long pointed, red nose-tip", "Short rounded, button nose"],
    "Lips": ["Dry, cracked, black/brown tinge", "Red, inflamed, yellowish", "Smooth, oily, pale, whitish"],
    "Teeth": ["Stick out, big, roomy, thin gums", "Medium, soft, tender gums", "Healthy, white, strong gums"],
    "Skin": ["Thin, dry, cold, rough, dark", "Smooth, oily, warm, rosy", "Thick, oily, cool, white, pale"],
    "Hair": ["Dry, brown, black, knotted, brittle, scarce", "Straight, oily, blond, gray, red, bald", "Thick, curly, oily, wavy, luxuriant"],
    "Nails": ["Dry, rough, brittle, break easily", "Sharp, flexible, pink, lustrous", "Thick, oily, smooth, polished"],
    "Neck": ["Thin, tall", "Medium, Moderate", "Big, folded"],
    "Chest": ["Flat, sunken", "Moderated", "Expanded, round"],
    "Belly": ["Thin, flat, sunken", "Normal", "Big, pot-bellied"],
    "Belly-button": ["Small, irregular, herniated", "Oval, superficial", "Big, deep, round, stretched"],
    "Hips": ["Slender, thin", "Average", "Heavy, big"],
    "Joints": ["Cold, cracking", "Ordinary", "Large, lubricated"],
    "Appetite": ["Irregular, scanty", "Strong, unbearable", "Slow but steady"],
    "Digestion": ["Irregular, forms gas", "Quick, causes burning", "Prolonged, forms mucus"],
    "Taste": ["Sweet, sour, salty", "Sweet, bitter, astringent", "Bitter, pungent, astringent"],
    "Thirst": ["Changeable", "Surplus", "Sparse"],
    "Elimination": ["Constipation", "Loose", "Thick, oily, sluggish"],
    "Physical Activity": ["Hyperactive", "Adequate", "Slow"],
    "Mental Activity": ["Overlyactive", "Fair", "Dull, slow"],
    "Emotions": ["Anxiety, fear, uncertainty", "Anger, hate, jealousy", "Calm, greedy, attachment"],
    "Faith": ["Variable", "Extremist", "Consistent"],
    "Intellect": ["Quick but faulty response", "Accurate response", "Slow, exact"],
    "Recollection": ["Recent good, remote poor", "Distinct", "Slow and sustained"],
    "Dreams": ["Quick, active, many, fearful", "Fiery, war, violence", "Lakes, snow, romantic"],
    "Sleep": ["Scanty, broken up, sleeplessness", "Little but sound", "Deep, prolonged"],
    "Speech": ["Rapid, unclear", "Sharp, penetrating", "Slow, monotonous"],
    "Finances": ["Poor, spends on trifles", "Spends money on luxuries", "Rich, good money preserver"]
}

questions_vikruti = {
    "Appearance": ["Thin, bony, emaciated", "Medium, intense", "Large, sluggish"],
    "Weight": ["Underweight", "Steady", "Overweight"],
    "Joints": ["Cracking and popping", "Tender", "Swollen"],
    "Spine": ["Scoliosis tendency", "Kyphosis tendency", "Lordosis tendency, slipped disk"],
    "Muscles": ["Tremors, tics, spasms", "Tenderness", "Swelling"],
    "Skin": ["Dark, dry, rough, scaly, liver spots", "Yellow or red, rashes, pimples, acne", "Pale, oily, smooth, swelling"],
    "Lymph Nodes": ["Skinny", "Tender, inflamed", "Enlarged, congested"],
    "Veins": ["Prominent, collapsed, empty", "Bruises easily, moderate visibility", "Full, wide, stagnant"],
    "Eyes": ["Dry, restless, blinking", "Red, burning, hypersensitive to light", "Pale, swollen, sticky, excessive lacrimation"],
    "Ears": ["Ringing (tinnitus)", "Pain, infections", "Clogged, discharge"],
    "Nose, Sinuses": ["Dry, crusty", "Red, inflamed", "Congestion"],
    "Lips": ["Dry, cracked", "Red & inflamed", "Pale, oily"],
    "Mouth": ["Dry, receding gums", "Red, inflamed and tender gums", "Excessive salivation"],
    "Teeth": ["Cavities, receding gums, cracked enamel", "Yellow, wasted enamel", "Sweet tooth, strong enamel"],
    "Tongue": ["Dry, cracked, tremors, dark coating", "Red, inflamed, yellow coating", "Pale, thick white coating"],
    "Hair": ["Dry, knotted, brittle", "Oily, graying, bald", "Oily, wavy"],
    "Nails": ["Dry, rough, brittle, cracked, bitten", "Soft, sharp, inflamed", "Pale, thick, oily"],
    "Appetite": ["Variable, anorexia nervosa", "Strong, unbearable, hypoglycemia", "Low, steady"],
    "Digestion": ["Irregular, gas and bloating", "Quick, acid indigestion", "Slow, prolonged, indigestion"],
    "Metabolism": ["Irregular", "Extremely Active", "Fairly Slow"],
    "Thirst": ["Varying", "Decently Strong", "Decently Low"],
    "Elimination": ["Constipation, dry, hard stools", "Loose stools, diarrhea, burning", "Heavy, oily stools with mucus"],
    "Energy Level": ["Hyperactive, exhausts quickly", "Intense, exhausts from excessive thinking", "Low, exhaustion due to excess weight"],
    "Sex Drive": ["Premature orgasm", "Painful sex", "Low libido"],
    "Liver & Spleen": ["Palpable (double normal size)", "Tender (Soft)", "Enlarged, fatty degenerative changes"],
    "Voice": ["Dry, exhausted, explosive, whispering, stuttering", "Sharp, penetrating, metallic", "Deep, hoarse, drum-like"],
    "Speech": ["Rapid, abrupt, unclear ideas", "Sharp, determined, premeditated", "Slow, uninterested"],
    "Breathing": ["Nervous, diaphragmatic (sympathetic nervous system)", "Aggressive, intercostals, tight in chest", "Slow, abdominal, apnea tendency"],
    "Allergies": ["Dry wheezing, breathlessness", "Hives, rashes, urticaria", "Congestion, runny nose"],
    "Sleep": ["Insomnia, broken", "Difficult entering, insufficient", "Excessive, drowsiness"],
    "Dreams": ["Plenty, active, fearful", "Fiery, violent", "Watery, romantic"],
    "Emotions": ["Anxiety, fear, loneliness", "Judgment, criticism, anger, hate, jealousy", "Attachment, greed, depression"],
    "Intellect": ["Fast but faulty response", "Abrupt but accurate response", "Slow but exact response"],
    "Memory": ["Short term good, Long term poor", "Moderate, distinct, effective", "Slow, Long term very good"]
}

dosha_scores_prakruti = {
    "VATA": 0,
    "PITTA": 0,
    "KAPHA": 0
}

dosha_scores_vikruti = {
    "VATA": 0,
    "PITTA": 0,
    "KAPHA": 0
}

if __name__ == '__main__':
    st.set_page_config(
        page_title="Prakruti & Vikruti Constitution Quiz",
        page_icon="✨",
        layout="wide"
    )

    st.title("Prakruti & Vikruti Constitution Quiz")

    st.sidebar.markdown(
    f'<div style="display: flex; flex-direction: column; align-items: center;">'
    f'<img src="https://i.imgur.com/7KSTJFb.png" alt="QR Code" width="300">'
    f'<p style="font-weight: bold; font-size: 16px; margin-top: 10px;">Scan to analyze your core Dosha</p>'
    f'</div>',
    unsafe_allow_html=True
)




    
     col1, col2 = st.columns(2)

    with col1:
        st.write("## Prakruti Observation")
        st.write("Fill these based on how you have felt throughout your life")
        user_answers_prakruti = {}
        for question, options in questions_prakruti.items():
            st.write(f"**{question}**")
            user_answers_prakruti[question] = st.checkbox(options[0])
            user_answers_prakruti[question] = st.checkbox(options[1])
            user_answers_prakruti[question] = st.checkbox(options[2])

    with col2:
        st.write("## Vikruti Observation")
        st.write("Fill these based on how you have felt recently. Ask a friend for an unbiased opinion")
        user_answers_vikruti = {}
        for question, options in questions_vikruti.items():
            st.write(f"**{question}**")
            user_answers_vikruti[question] = st.checkbox(options[0])
            user_answers_vikruti[question] = st.checkbox(options[1])
            user_answers_vikruti[question] = st.checkbox(options[2])

    predict_button = st.button("Predict Dosha Scores")

    if predict_button:
        dosha_scores_prakruti = {
            "VATA": 0,
            "PITTA": 0,
            "KAPHA": 0
        }

        dosha_scores_vikruti = {
            "VATA": 0,
            "PITTA": 0,
            "KAPHA": 0
        }

        # Calculate dosha scores based on user answers
        for question, user_answer in user_answers_prakruti.items():
            options = questions_prakruti[question]
            for option in options:
                if user_answer:
                    if option == options[0]:
                        dosha_scores_prakruti["VATA"] += 1
                    elif option == options[1]:
                        dosha_scores_prakruti["PITTA"] += 1
                    elif option == options[2]:
                        dosha_scores_prakruti["KAPHA"] += 1

        for question, user_answer in user_answers_vikruti.items():
            options = questions_vikruti[question]
            for option in options:
                if user_answer:
                    if option == options[0]:
                        dosha_scores_vikruti["VATA"] += 1
                    elif option == options[1]:
                        dosha_scores_vikruti["PITTA"] += 1
                    elif option == options[2]:
                        dosha_scores_vikruti["KAPHA"] += 1

        st.write("### Prakruti Dosha Scores:")
        for dosha, score in dosha_scores_prakruti.items():
            st.write(f"{dosha}: {score}")

        prakruti_dominant_dosha = max(dosha_scores_prakruti, key=dosha_scores_prakruti.get)
        st.write(f"### Prakruti Dominant Dosha: {prakruti_dominant_dosha}")

        prakruti_df = pd.DataFrame(list(dosha_scores_prakruti.items()), columns=["Dosha", "Prakruti Score"])
        st.bar_chart(prakruti_df.set_index("Dosha"))

        st.write("### Vikruti Dosha Scores:")
        for dosha, score in dosha_scores_vikruti.items():
            st.write(f"{dosha}: {score}")

        vikruti_dominant_dosha = max(dosha_scores_vikruti, key=dosha_scores_vikruti.get)
        st.write(f"### Vikruti Dominant Dosha: {vikruti_dominant_dosha}")

        vikruti_df = pd.DataFrame(list(dosha_scores_vikruti.items()), columns=["Dosha", "Vikruti Score"])
        st.bar_chart(vikruti_df.set_index("Dosha"))
