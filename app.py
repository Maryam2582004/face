import streamlit as st

st.title("توليد وجه بناءً على الصفات (مجاني)")

st.write("ادخلي الصفات وسيتم توليد الصورة باستخدام Hugging Face Stable Diffusion Demo")

# إدخال الصفات
hair = st.selectbox("لون الشعر", ["بني", "أسود", "أشقر"])
eyes = st.selectbox("لون العيون", ["أزرق", "بني", "خضر"])
skin = st.selectbox("لون البشرة", ["فاتح", "متوسط", "غامق"])

if st.button("توليد الصورة"):
    prompt = f"فتاة شعر {hair}، عينين {eyes}، بشرة {skin}، وجه واقعي"
    
    st.write("جاري توليد الصورة… انتظري قليلاً")
    
    # عرض واجهة Hugging Face مباشرة باستخدام iframe
    st.components.v1.html(
        f"""
        <iframe src="https://huggingface.co/spaces/stabilityai/stable-diffusion?__theme=light"
        width="800" height="600"></iframe>
        """,
        height=650
    )

    st.write(f"الوصف المستخدم لتوليد الصورة: {prompt}")
