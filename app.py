import streamlit as st
from PIL import Image, ImageDraw

st.title("وجه كرتوني محسّن من الصفات")

# اختيار الصفات
hair_color = st.selectbox("لون الشعر", ["brown", "black", "blonde"])
eye_color = st.selectbox("لون العيون", ["blue", "brown", "green"])
skin_color = st.selectbox("لون البشرة", ["light", "medium", "dark"])

# ألوان RGB
skin_map = {"light": (255, 224, 189), "medium": (205, 133, 63), "dark": (101, 67, 33)}
hair_map = {"brown": (101, 67, 33), "black": (0,0,0), "blonde": (255, 224, 102)}
eye_map = {"blue": (0, 102, 204), "brown": (101, 67, 33), "green": (0, 153, 0)}

if st.button("عرض الوجه"):
    img = Image.new("RGB", (400, 400), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # رأس الوجه (شكل بيضاوي أكثر طبيعية)
    draw.ellipse((100, 80, 300, 350), fill=skin_map[skin_color])

    # الشعر (منحنيات بسيطة)
    draw.polygon([(100, 80), (300, 80), (320, 150), (80, 150)], fill=hair_map[hair_color])

    # العيون (بيضاوي)
    draw.ellipse((150, 160, 180, 190), fill=eye_map[eye_color])
    draw.ellipse((220, 160, 250, 190), fill=eye_map[eye_color])
    # بؤبؤ أسود صغير
    draw.ellipse((165, 170, 170, 175), fill=(0,0,0))
    draw.ellipse((235, 170, 240, 175), fill=(0,0,0))

    # الحاجبين
    draw.line((145, 150, 185, 155), fill=(50,25,0), width=3)
    draw.line((215, 155, 255, 150), fill=(50,25,0), width=3)

    # الفم (منحنى بسيط)
    draw.arc((160, 250, 240, 280), start=0, end=180, fill=(255,0,0), width=3)

    st.image(img, caption="وجه كرتوني محسّن")
