import streamlit as st
st.set_page_config(
    page_title="BMI Calclulator",
    page_icon="💡",
)

if "weight" not in st.session_state:
    st.session_state.weight=0
if "height" not in st.session_state:
    st.session_state.height=0
col1, col2=st.columns([3,10], gap="xsmall", vertical_alignment="center")
with col1:
    st.image("images/favpng_7d1161465538a1c0897ab46880a7ca8b.png",width=150)
with col2:    
    st.title("BMI Calculator")

cl1, cl2 = st.columns(2)
with cl1:
    Wei=st.number_input("Weight",step=5, min_value=0)
with cl2:
    unitw= st.segmented_control("",["Kg","Pounds"])

if unitw=="Kg":
    st.session_state.weight=Wei
elif unitw=="Pounds":
    st.session_state.weight=Wei*0.45359237
else:
    st.session_state.weight=0

st.write("")
c1, c2= st.columns([1,10],vertical_alignment="center")
with c1:
    st.write("Height")
with c2:
    v=st.toggle("Inch System")
a1, a2=st.columns(2, vertical_alignment="center")
if v==False:
    a1, a2=st.columns(2, vertical_alignment="center")
    with a1:
        hm=st.number_input(label="hight", step=5, label_visibility="collapsed", min_value=0)
    with a2:
        st.text("cm")
    st.session_state.height=hm
else:
    b1, b2, b3, b4= st.columns(4,vertical_alignment="center")
    with b1:
        hightfee=st.number_input(label="hightfee", step=5, label_visibility="collapsed",min_value=0)
    with b2:
        st.text("feet")
    with b3:
        hightin=st.number_input(label="hightin", step=5, label_visibility="collapsed", min_value=0)
    with b4:
        st.text("inches")

    hight= (hightfee*30.48)+(hightin*2.54)
    st.session_state.height=hight
if "BMI" not in st.session_state:
    st.session_state.BMI=0
if st.button("Calculate") and st.session_state.height != 0 and st.session_state.weight != 0:
    st.session_state.BMI=int(st.session_state.weight/(st.session_state.height/100)**2)
    
if st.session_state.BMI==0:
    pass
elif st.session_state.BMI<18.5:
    st.info(f"Underweight, BMI is {st.session_state.BMI}")
elif st.session_state.BMI<25:
    st.success(f"Healthy Weight, BMI is {st.session_state.BMI}")
elif st.session_state.BMI<30:
    st.warning(f"Overweight, BMI is {st.session_state.BMI}")
else:
    st.error(f"Obesity, BMI is {st.session_state.BMI}")
    
