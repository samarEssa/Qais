import streamlit as st
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
import streamlit as st
from sklearn.preprocessing import LabelEncoder

st.markdown("<h2 style='text-align: center;'> منظمة قائس </h2>", unsafe_allow_html=True)

import pandas as pd
data = pd.read_csv('Ds.csv')
data1 = pd.read_csv('Ds2.csv')


label = LabelEncoder()
data['label'] = label.fit_transform(data['التقييم'])      
label = LabelEncoder()
data1['label1'] = label.fit_transform(data1['التقييم'])    
st.sidebar.image("قائس.png", use_column_width=True)

pt= st.sidebar.selectbox(
        "اختر من القائمة:", ("بيانات المؤسسة والخطابات ", "بيانات المؤسسة", "الخطابات","عرض البيانات","بيانات التسجيل")
    )
            
# pt =st.sidebar.radio("اختر البيانات التي تريد عرضها" , options=("بيانات المؤسسة والخطابات", "بيانات المؤسسة", "الخطابات","عرض البيانات"))     

if pt =="بيانات المؤسسة":
    colors = ['#A9CCE3', '#D4E6F1', '#EAF2F8', '#DAF7A6', '#FFC300']
    col1, col2 = st.columns(2)

# Plotting the value counts as a pie chart in the first column
    with col1:
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        data['label'].value_counts().plot.pie(autopct='%1.1f%%', colors=colors, ax=ax1)
        xtit = arabic_reshaper.reshape('بيانات المؤسسة ')
        ax1.set_title(get_display(arabic_reshaper.reshape(xtit)))
        ax1.set_ylabel('')  # Remove the ylabel
        st.pyplot(fig1)

    # Plotting the value counts as a bar chart in the second column
    with col2:
        xlbl = 'التقييم'
        ylbl = 'عدد بيانات المؤسسة'
        xtit = 'بيانات المؤسسة'

        # Define data for the bar chart
        values = data['label'].value_counts().sort_index()  # Ensure the order is consistent

        fig2, ax2 = plt.subplots(figsize=(4, 4))
        ax2.bar(values.index, values.values, color=colors)
        ax2.set_xlabel(get_display(arabic_reshaper.reshape(xlbl)))
        ax2.set_ylabel(get_display(arabic_reshaper.reshape(ylbl)))
        ax2.set_title(get_display(arabic_reshaper.reshape(xtit)))
        st.pyplot(fig2)

elif pt =="الخطابات":
    
    
    col1, col2 = st.columns(2)

    # First column
    with col1:
        colors = ['#A9CCE3', '#D4E6F1']
        # Plotting the value counts as a pie chart
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        data1['label1'].value_counts().plot.pie(autopct='%1.1f%%', colors=colors, ax=ax1)
        xtit = arabic_reshaper.reshape('الخطابات ')
        ax1.set_title(get_display(arabic_reshaper.reshape(xtit)))
        ax1.set_ylabel('')  # Remove the ylabel
        st.pyplot(fig1)

    # Second column
    with col2:
        colors = ['#A9CCE3', '#D4E6F1']
        values = data1['label1'].value_counts().sort_index()  
        # Plotting the value counts as a pie chart
        fig2, ax2 = plt.subplots(figsize=(4, 4))
        ax2.bar(values.index, values.values, color=colors)
        xtit = arabic_reshaper.reshape('الخطابات ')
        ax2.set_title(get_display(arabic_reshaper.reshape(xtit)))
        st.pyplot(fig2)
   
elif pt =="بيانات المؤسسة والخطابات ":
    
    combined_counts = pd.concat([data['label'].value_counts(), data1['label1'].value_counts()], axis=1)
    combined_counts = pd.concat([data['label'].value_counts(), data1['label1'].value_counts()], axis=1)
    reshaped_columns = [get_display(arabic_reshaper.reshape(col)) for col in ['بيانات المؤسسة', 'الخطابات']]
    combined_counts.columns = reshaped_columns

    # Specify colors for each category
    colors = ['#A9CCE3', '#D4E6F1', '#EAF2F8', '#DAF7A6', '#FFC300']

    # Create a figure with a single subplot
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plotting the value counts as bar charts with specified colors
    combined_counts.plot(kind='bar', color=colors, ax=ax)

    # Set the title, xlabel, and ylabel
    ax.set_title(get_display(arabic_reshaper.reshape('مخطط الشريط المجمع لتوزيع العلامات')))
    ax.set_xlabel(get_display(arabic_reshaper.reshape('العلامة')))
    ax.set_ylabel(get_display(arabic_reshaper.reshape('التقييم')))

    # Display the plot in Streamlit
    st.pyplot(fig)
    # Example usage


elif pt =="عرض البيانات":  
    st.write(data)
    st.write(data1)


elif pt =="بيانات التسجيل":  

    
 with st.form("form-0"):
    st.markdown("<h2 style='text-align: center;'> البيانات الأساسية</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        text_input_1 = st.text_input("اسم المنظمة")
        text_input_2 = st.text_input("التعريف بالمنظمة")
        text_input_3 = st.text_input("تصنيف المنظمة")
        text_input_4 = st.text_input("المرجعية الإدارية")
        text_input_5 = st.text_input("تاريخ التأسيس")
        text_input_6 = st.text_input("رقم التصريح")
        text_input_7 = st.text_input("تاريخ الانتهاء")
    
    with col2:
        text_input_8 = st.text_input("عدد فروع المنظمة")
        text_input_9 = st.text_input("وجود قسم نسائي")
        text_input_10 = st.text_input("نوعه")
        text_input_11 = st.text_input("هاتف المنظمة")
        text_input_12 = st.text_input("الموقع على الخريطة")
        text_input_13 = st.text_input("الموقع الالكتروني")
        text_input_14 = st.text_input("البريد الالكتروني")
        text_input_15 = st.text_input("المديرالتنفيذي")
        text_input_16 = st.text_input("رقم التواصل")

    submitted_0 = st.form_submit_button(label="Submit")

    if submitted_0:
        st.write("ملخص البيانات الأساسية")
        st.write(text_input_1)
        st.write(text_input_2)
        st.write(text_input_3)
        st.write(text_input_4)
        st.write(text_input_5)
        st.write(text_input_6)
        st.write(text_input_7)
        st.write(text_input_8)
        st.write(text_input_9)
        st.write(text_input_10)
        st.write(text_input_11)
        st.write(text_input_12)
        st.write(text_input_13)
        st.write(text_input_14)
        st.write(text_input_15)
        st.write(text_input_16)

 with st.form("form-1"):
        st.markdown("<h2 style='text-align: center;'> بيانات المؤسسة </h2>", unsafe_allow_html=True)
        choice_11 = st.selectbox("وجود خطة استراتيجية", ["نعم ومفعل ", "لايوجد", "نعم ومفعل جزئياً"])
        choice_12 = st.selectbox("وجود خطة تشغلية", ["نعم ومفعل ", "لايوجد", "نعم ومفعل جزئياً"])
        choice_13 = st.selectbox("وجود خطط المشاريع ", ["نعم ومفعل ", "لايوجد", "نعم ومفعل جزئياً"])
        choice_14 = st.selectbox("وجود مجلس إدارة أو تنفيذها", ["نعم ومفعل ", "لايوجد", "نعم ومفعل جزئياً"])
        choice_15 = st.selectbox("وجود هيكل تنظيمي", ["نعم ومفعل ", "لايوجد", "نعم ومفعل جزئياً"])
        choice_16 = st.selectbox("وجود وصف وظيفي ", ["نعم ومفعل ", "لايوجد", "نعم ومفعل جزئياً"])
        choice_17 = st.selectbox(" وجود نظام إداري ", ["نعم ومفعل ", "لايوجد", "نعم ومفعل جزئياً"])
        submitted_1 = st.form_submit_button("تأكيد")

        if submitted_1:
            if choice_11 == "نعم ومفعل " and choice_12 == "نعم ومفعل " and choice_13 == "نعم ومفعل " and choice_14 == "نعم ومفعل " and choice_15 == "نعم ومفعل " and choice_16 == "نعم ومفعل " and choice_17 == "نعم ومفعل ":
                st.success('المتطلبات كاملة')
            else:
                st.warning('المتطلبات ناقصة')

 with st.form("form-2"):
        st.markdown("<h2 style='text-align: center;'> الخطابات</h2>", unsafe_allow_html=True)
        choice_11 = st.selectbox("  خطة استراتيجية محدثة", ["يوجد ", "لايوجد"])
        choice_12 = st.selectbox("خطة تشغيلية محدثة",  ["يوجد ", "لايوجد"])
        choice_13 = st.selectbox("نسخة من خطط ووثائق",  ["يوجد ", "لايوجد"])
        choice_14 = st.selectbox("  نسخة من خطط ووثائق مشاريع المنظة",  ["يوجد ", "لايوجد"])
        choice_15 = st.selectbox("قرار تشكيل مجلس إدارة أو مجلس تنفيذي",  ["يوجد ", "لايوجد"])
        choice_16 = st.selectbox(" قرار اعتماد الهيكل التنظيمي  ",  ["يوجد ", "لايوجد"])
        choice_17 = st.selectbox("   دليل الأوصاف الوظيفية ",  ["يوجد ", "لايوجد"])
        submitted_2 = st.form_submit_button("تأكيد")

        if submitted_2:
            if choice_11 == "يوجد " and choice_12 == "يوجد " and choice_13 == "يوجد " and choice_14 == "يوجد " and choice_15 == "يوجد " and choice_16 == "يوجد " and choice_17 == "يوجد ":
                st.success('المتطلبات كاملة')
            else:
                st.warning('المتطلبات ناقصة')




                    

        