import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="توليد وجه كرتوني", layout="centered")
st.title("توليد وجه شخص كرتوني من الصفات")

# اختيار الصفات
hair_color = st.selectbox("لون الشعر", ["brown", "black", "blonde"])
eye_color = st.selectbox("لون العيون", ["blue", "brown", "green"])
skin_color = st.selectbox("لون البشرة", ["light", "medium", "dark"])

# تحديد ألوان RGB لكل خيار
skin_map = {"light": (255, 224, 189), "medium": (205, 133, 63), "dark": (101, 67, 33)}
hair_map = {"brown": (101, 67, 33), "black": (0,0,0), "blonde": (255, 224, 102)}
eye_map = {"blue": (0, 102, 204), "brown": (101, 67, 33), "green": (0, 153, 0)}

if st.button("عرض الوجه"):
    # إنشاء صورة فارغة
    img = Image.new("RGB", (400, 400), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # رسم الوجه (دائرة للبشرة)
    draw.ellipse((100, 50, 300, 350), fill=skin_map[skin_color])

    # رسم الشعر (مستطيل فوق الرأس)
    draw.rectangle((100, 30, 300, 150), fill=hair_map[hair_color])

    # رسم العيون (دوائر صغيرة)
    draw.ellipse((150, 150, 180, 180), fill=eye_map[eye_color])
    draw.ellipse((220, 150, 250, 180), fill=eye_map[eye_color])

    # رسم الفم (خط بسيط)
    draw.line((170, 250, 230, 250), fill=(255,0,0), width=3)

    st.image(img, caption="وجه كرتوني مبسط من الصفات")
