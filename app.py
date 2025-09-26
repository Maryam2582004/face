# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image
# import io

# st.title("توليد وجه بناءً على الصفات (مجاني)")

# # إدخال الصفات
# hair = st.selectbox("لون الشعر", ["بني", "أسود", "أشقر"])
# eyes = st.selectbox("لون العيون", ["أزرق", "بني", "خضر"])
# skin = st.selectbox("لون البشرة", ["فاتح", "متوسط", "غامق"])

# # Hugging Face API Token
# HF_API_TOKEN = "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"
# client = InferenceClient(token=HF_API_TOKEN)

# if st.button("توليد الصورة"):
#     prompt = f"فتاة شعر {hair}، عينين {eyes}، بشرة {skin}، وجه واقعي"

#     st.write("جاري توليد الصورة… انتظري قليلاً")

#     # توليد الصورة عبر Hugging Face Inference API
#     image_bytes = client.text_to_image(
#     model="stabilityai/stable-diffusion-2",
#     prompt=prompt
# )


    
#     # تحويل الصورة لعرضها في Streamlit
#     image = Image.open(io.BytesIO(image_bytes))
#     st.image(image, caption=f"الصورة المولدة من الوصف: {prompt}")


import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io

st.set_page_config(page_title="توليد وجه من الصفات", layout="centered")
st.title("توليد وجه شخص بناءً على الصفات")

# -------------------------
# إعداد Hugging Face API
# -------------------------
HF_API_TOKEN = "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"  # ضعي هنا التوكن الخاص بك
client = InferenceClient(token=HF_API_TOKEN)

# -------------------------
# إدخال الصفات
# -------------------------
hair = st.selectbox("لون الشعر", ["بني", "أسود", "أشقر", "أحمر"])
eyes = st.selectbox("لون العيون", ["أزرق", "بني", "خضر", "رمادي"])
skin = st.selectbox("لون البشرة", ["فاتح", "متوسط", "غامق"])
age = st.selectbox("العمر التقريبي", ["طفل", "شاب", "بالغ", "كبير في السن"])
gender = st.selectbox("الجنس", ["ذكر", "أنثى"])

if st.button("توليد الصورة"):
    prompt = f"{gender}، عمر {age}، شعر {hair}، عيون {eyes}، بشرة {skin}، وجه واقعي، صورة عالية الجودة"
    
    st.write("جاري توليد الصورة… انتظري قليلاً")

    try:
        # توليد الصورة عبر Hugging Face Stable Diffusion
        image_bytes = client.text_to_image(
            model="stabilityai/stable-diffusion-2",
            prompt=prompt
        )

        # تحويل الصورة لعرضها في Streamlit
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption=f"الصورة المولدة من الوصف: {prompt}")

    except Exception as e:
        st.error(f"حدث خطأ أثناء توليد الصورة: {e}")
