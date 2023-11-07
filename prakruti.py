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

advice_text = {
    "VATA": [
        "Favor warm, cooked, and easily digestible foods.",
        "Incorporate plenty of healthy fats such as ghee, coconut oil, and olive oil.",
        "Include nourishing and grounding foods like sweet potatoes, whole grains (cooked), cooked vegetables, and lentils.",
        "Drink warm herbal teas (non-caffeinated) like ginger, cinnamon, and licorice.",
        "Reduce raw foods, cold foods, and excessive caffeine."
    ],
    "PITTA": [
        "Favor cooling foods: Incorporate foods that have a cooling effect on the body.",
        "Include sweet, bitter, and astringent tastes: Focus on foods with these tastes to balance excess heat.",
        "Limit spicy, oily, and acidic foods: Reduce or avoid foods that can increase Pitta, such as hot spices, fried foods, and excessive sourness.",
        "Stay hydrated: Drink cool or room temperature water and herbal teas to balance the heat.",
        "Enjoy fresh, ripe, and sweet fruits: Opt for sweet fruits like melons, grapes, and sweet berries."
    ],
    "KAPHA": [
        "Warm and light soups with a variety of vegetables.",
        "Fresh fruits like apples, pears, berries, and pomegranates.",
        "Whole grains like quinoa, barley, and millet.",
        "Legumes such as lentils and mung beans.",
        "Lean proteins like fish and chicken (in moderation).",
        "Warm herbal teas and spices like ginger, black pepper, and turmeric."
    ]
}

product_links = {
    "VATA": [
        "https://www.amazon.in/BIO-RESURGE-VATA-CARE-Tablet/dp/B07JF24CB4?th=1",
        "https://www.amazon.in/Resurge-Life-Ayurveda-Dosha-Medicine/dp/B09QSVJ629",
        "https://www.amazon.com/Ayurvedic-Meal-Planner-Vata-Dosha/dp/B097C4KY34/ref=sr_1_3?keywords=vata+dosha&qid=1699205366&sr=8-3",
        "https://www.amazon.com/Banyan-Botanicals-Healthy-Vata-Nourishing/dp/B004QC1890/ref=sr_1_1?keywords=vata+dosha&qid=1699205366&sr=8-1"
    ],
    "PITTA": [
        "https://www.amazon.in/BIO-RESURGE-PITTA-CARE-Tablet/dp/B07JDF44LW/ref=sr_1_1?crid=1NN25H8699IR8&keywords=BIO%2BRESURGE%2BLIFE%2BAyurveda%2BPitta%2BBalance%2BMedicine%2B100%25%2BNatural%2Band%2BOrganic&nsdOptOutParam=true&qid=1699205601&s=hpc&sprefix=bio%2Bresurge%2Blife%2Bayurveda%2Bpitta%2Bbalance%2Bmedicine%2B100%25%2Bnatural%2Band%2Borganic%2Chpc%2C268&sr=1-1&th=1",
        "https://www.amazon.in/Ksheerabala-Ayurvedic-Formulation-Imbalance-Effectively/dp/B08BTT5BMP/ref=sr_1_3_sspa?keywords=pitta+balance&nsdOptOutParam=true&qid=1699205556&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A360J6YC387ZBZ",
        "https://www.amazon.in/DR-TALATS-Heartburn-Free-Caps/dp/B0BQHY7YWN/ref=sr_1_4_sspa?keywords=pitta%2Bbalance&nsdOptOutParam=true&qid=1699205556&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "https://www.amazon.in/TEACURRY-Pitta-Dosha-Month-Pack/dp/B0C3MQPL3T/ref=sr_1_11?keywords=pitta+balance&nsdOptOutParam=true&qid=1699205556&sr=8-11"
    ],
    "KAPHA": [
        "https://www.amazon.in/Resurge-Life-Ayurveda-Dosha-Medicine/dp/B09QSVJ629/ref=sr_1_2_sspa?keywords=kapha+dosha+medicine&qid=1699205659&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "https://www.amazon.in/Zandu-Ashwagandha-Capsules-Goodness-Extracts/dp/B08TPPZCPJ/ref=sr_1_3_sspa?keywords=kapha+dosha+medicine&qid=1699205659&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "https://www.amazon.in/Balancing-Ginger-Maintains-Immunity-Cough-30/dp/B07JMDLPXH/ref=sr_1_7?keywords=kapha%2Bdosha%2Bmedicine&qid=1699205659&sr=8-7&th=1",
        "https://www.amazon.in/Balance-medicine-ayurvedic-balance-Tablets/dp/B0CD7NB3R7/ref=sr_1_6?keywords=kapha+dosha+medicine&qid=1699205659&sr=8-6"
    ]
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
        f'<p style="font-weight: bold; font-size: 16px; margin-top: 10px;">Want to delve into more detail about your dosha and get personalized advice? Scan and find out.</p>'
        f'</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([2, 2, 0.5])

    with col1:
        st.write("## Prakruti Observation")
        st.write("###### In the enchanting tapestry of your existence, Nature has woven a masterpiece, casting you as the singular masterpiece of Prakruti. Your essence, an exquisite fusion of vata, pitta, and kapha, is a symphony only you possess. When you came into being, your genes and karma, a realm unto themselves, conspired to create your Prakruti – the divine alchemy of the tridosha. It's the very essence that molds you, from the graceful contours of your body to the intricate patterns of your thoughts and emotions.")
        st.write("Fill these based on how you have felt throughout your life")

        for question, options in questions_prakruti.items():
            st.write(f"**{question}**")
            user_answers = [st.checkbox(option) for option in options]
            for option, selected in zip(options, user_answers):
                if selected:
                    if option == options[0]:
                        dosha_scores_prakruti["VATA"] += 1
                    elif option == options[1]:
                        dosha_scores_prakruti["PITTA"] += 1
                    elif option == options[2]:
                        dosha_scores_prakruti["KAPHA"] += 1
                    st.success(f'Your answer for {question} is: {option}')

        prakruti_dominant_dosha = max(dosha_scores_prakruti, key=dosha_scores_prakruti.get)

        predict_prakruti = st.button("Predict Prakruti Dosha")
        if predict_prakruti:
            st.write(f"### Prakruti Dosha Scores:")
            st.write(f"VATA: {dosha_scores_prakruti['VATA']}")
            st.write(f"PITTA: {dosha_scores_prakruti['PITTA']}")
            st.write(f"KAPHA: {dosha_scores_prakruti['KAPHA']}")
            st.write(f"### Prakruti Dominant Dosha: {prakruti_dominant_dosha}")

            # Add advice based on the most dominant dosha
            st.write("##### Nutrition advice for Prakruti Dominance:")
            for line in advice_text[prakruti_dominant_dosha]:
                st.write(line)

    with col2:
        st.write("## Vikruti Observation")
        st.write("###### And then, we delve into the captivating realm of Vikruti, your current blend of the tridosha – an intriguing twist in the tale, quite possibly veering away from your Prakruti's perfect harmony. Imbalanced doshas signify a delicate disarray within, where the exquisite balance of your physical, mental, and spiritual well-being is somewhat awry.")
        st.write("Fill these based on how you have felt recently. Ask a friend for an unbiased opinion")

        for question, options in questions_vikruti.items():
            st.write(f"**{question}**")
            user_answers = [st.checkbox(option) for option in options]
            for option, selected in zip(options, user_answers):
                if selected:
                    if option == options[0]:
                        dosha_scores_vikruti["VATA"] += 1
                    elif option == options[1]:
                        dosha_scores_vikruti["PITTA"] += 1
                    elif option == options[2]:
                        dosha_scores_vikruti["KAPHA"] += 1
                    st.success(f'Your answer for {question} is: {option}')

        vikruti_dominant_dosha = max(dosha_scores_vikruti, key=dosha_scores_vikruti.get)

        predict_vikruti = st.button("Predict Vikruti Dosha")
        if predict_vikruti:
            st.write(f"### Vikruti Dosha Scores:")
            st.write(f"VATA: {dosha_scores_vikruti['VATA']}")
            st.write(f"PITTA: {dosha_scores_vikruti['PITTA']}")
            st.write(f"KAPHA: {dosha_scores_vikruti['KAPHA']}")
            st.write(f"### Vikruti Dominant Dosha: {vikruti_dominant_dosha}")
            vikruti_calculations_done = True

            st.write("##### Nutrition advice for Vikruti Dominance:")
            for line in advice_text[vikruti_dominant_dosha]:
                st.write(line)

with col3:
        if predict_vikruti:
            st.write("###### Recommended Products for Vikruti Dominance:")
            for link in product_links[vikruti_dominant_dosha]:
                st.write(link)

# Create vertical lines at the end of columns
col1.markdown("""
        <style>
        .st-ax {
            border-right: 2px solid red;
            padding-right: 12px;
            padding-left: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

col2.markdown("""
        <style>
        .st-ax {
            border-right: 2px solid red;
            padding-right: 12px;
            padding-left: 12px;
        }
        </style>
    """, unsafe_allow_html=True)


col1.markdown("<style>.st-ax { max-width: 30%; }</style>", unsafe_allow_html=True)
col2.markdown("<style>.st-ax { max-width: 40%; }</style>", unsafe_allow_html=True)
    




