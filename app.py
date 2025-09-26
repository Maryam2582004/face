import streamlit as st
import numpy as np
import cv2

st.title("تلوين وجه كرتوني باستخدام OpenCV")

# اختيار الصفات
hair_color = st.selectbox("لون الشعر", ["brown", "black", "blonde"])
eye_color = st.selectbox("لون العيون", ["blue", "brown", "green"])
skin_color = st.selectbox("لون البشرة", ["light", "medium", "dark"])

# تحويل الألوان ل BGR (OpenCV)
skin_map = {"light": (189, 224, 255), "medium": (63, 133, 205), "dark": (33, 67, 101)}
hair_map = {"brown": (33, 67, 101), "black": (0,0,0), "blonde": (102, 224, 255)}
eye_map = {"blue": (204, 102, 0), "brown": (33, 67, 101), "green": (0, 153, 0)}

if st.button("عرض الوجه"):
    # إنشاء صورة فارغة
    img = np.ones((400, 400, 3), dtype=np.uint8) * 255

    # رسم الوجه (دائرة للبشرة)
    cv2.ellipse(img, (200, 200), (100, 150), 0, 0, 360, skin_map[skin_color], -1)

    # رسم الشعر (مستطيل منحني فوق الرأس)
    pts = np.array([[100,80], [300,80], [320,150], [80,150]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img, [pts], hair_map[hair_color])

    # رسم العيون (دوائر)
    cv2.ellipse(img, (165, 175), (15, 10), 0, 0, 360, eye_map[eye_color], -1)
    cv2.ellipse(img, (235, 175), (15, 10), 0, 0, 360, eye_map[eye_color], -1)

    # بؤبؤ أسود صغير
    cv2.circle(img, (165, 175), 3, (0,0,0), -1)
    cv2.circle(img, (235, 175), 3, (0,0,0), -1)

    # رسم الفم (قوس)
    cv2.ellipse(img, (200, 260), (40, 20), 0, 0, 180, (0,0,255), 3)

    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="وجه كرتوني ملون باستخدام OpenCV")
