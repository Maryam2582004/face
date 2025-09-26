import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io

st.title("توليد وجه بناءً على الصفات (مجاني)")

# إدخال الصفات
hair = st.selectbox("لون الشعر", ["بني", "أسود", "أشقر"])
eyes = st.selectbox("لون العيون", ["أزرق", "بني", "خضر"])
skin = st.selectbox("لون البشرة", ["فاتح", "متوسط", "غامق"])

# Hugging Face API Token
HF_API_TOKEN = "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"
client = InferenceClient(token=HF_API_TOKEN)

if st.button("توليد الصورة"):
    prompt = f"فتاة شعر {hair}، عينين {eyes}، بشرة {skin}، وجه واقعي"

    st.write("جاري توليد الصورة… انتظري قليلاً")

    # توليد الصورة عبر Hugging Face Inference API
    image_bytes = client.text_to_image(
    model="stabilityai/stable-diffusion-2",
    prompt=prompt
)


    
    # تحويل الصورة لعرضها في Streamlit
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, caption=f"الصورة المولدة من الوصف: {prompt}")
