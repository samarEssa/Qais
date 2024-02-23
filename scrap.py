import streamlit as st
import requests
from bs4 import BeautifulSoup
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



# عنصر اختيار مع اظهار علامة صح عند الاختيار
# answer = st.radio('هل ترغب في التسجيل؟', ('نعم', 'لا'))
# if answer == 'نعم':
#     st.success('لقد اخترت التسجيل!')
# else:
#     st.warning('لم تختر التسجيل!')





# Create space
# st.empty()
# st.empty()
# st.empty()

# def create_square_with_text(text):
#     square_width = 150
#     square_height = 150

#     # Apply styling to the square
#     style = f"""
#         background-color: #F0F8FF;
#         width: {square_width}px;
#         height: {square_height}px;
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         border-radius: 10px;
#         border: 1px solid black;
#     """

#     # Create a div element with the text and styling
#     div_element = f"<div style='{style}'>{text}</div>"

#     # Display the div element using st.write
#     st.write(div_element, unsafe_allow_html=True)

# # Create four squares with text in the same row
# cols = st.columns(4)
# with cols[3]:
#     create_square_with_text("بيانات أساسية")
# with cols[2]:
#     create_square_with_text("بيانات فرعية")
# with cols[1]:
#     create_square_with_text("بيانات مؤسسية")
# with cols[0]:
#     create_square_with_text("خطاب المتطلبات")
# def get_inputs(input_id: int):
#     with st.expander(f"Dummy Section {input_id}", expanded=True):
#         with st.form(f"form_{input_id}", clear_on_submit=False):
#             value_1 = st.number_input(f"Dummy Input {input_id} Value 1")
#             value_2 = st.number_input(f"Dummy Input {input_id} Value 2")
#             value_3 = st.number_input(f"Dummy Input {input_id} Value 3")

#             submitted = st.form_submit_button(label=f"Submit Input 1")

#             if not submitted:
#                 st.warning("Please enter valid inputs before proceeding")
#                 st.stop()
#             else:
#                 return {"value_1": value_1, "value_2": value_2, "value_3": value_3}


# def dummy_main_logic(*args):
#     print(args)


# st.title("Dummy Title")

# inputs_1 = get_inputs(1)
# inputs_2 = get_inputs(2)
# inputs_3 = get_inputs(3)

# dummy_main_logic(inputs_1, inputs_2, inputs_3)




# import streamlit as st

# st.title("Test")

# # Define a custom CSS style to align form elements to the right
# right_aligned_style = """
#     <style>
#         .form-container {
#             display: flex;
#             flex-direction: column;
#             align-items: flex-end;
#         }
#     </style>
# """

# # Apply the custom CSS style
# st.markdown(right_aligned_style, unsafe_allow_html=True)

# # Create a container for all forms and apply the custom CSS style to each form
# with st.form("form-1"):
#     text_input_1 = st.text_input("Enter Text 1")
#     choice_1 = st.selectbox("Choose Option 1", ["Option A", "Option B"])
#     submitted_1 = st.form_submit_button(label="Submit")
#     if submitted_1:
#         st.write("1")
#         st.write("Text 1:", text_input_1)
#         st.write("Choice 1:", choice_1)

# with st.form("form-2"):
#     text_input_2 = st.text_input("Enter Text 2")
#     text_input_21 = st.text_input("Enter Text 21")
#     choice_2 = st.selectbox("Choose Option 2", ["Option X", "Option Y"])
#     choice_32 = st.selectbox("Choose Option 3", ["Option X", "Option Y"])
#     choice_42 = st.selectbox("Choose Option 4", ["Option X", "Option Y"])
#     choice_52 = st.selectbox("Choose Option 5", ["Option X", "Option Y"])
#     choice_62 = st.selectbox("Choose Option 6", ["Option X", "Option Y"])
#     choice_72 = st.selectbox("Choose Option 7", ["Option X", "Option Y"])
#     choice_82 = st.selectbox("Choose Option 8", ["Option X", "Option Y"])
#     submitted_2 = st.form_submit_button(label="Submit")
#     if submitted_2:
#         st.write("2")
#         st.write("Text 2:", text_input_2)
#         st.write("Choice 2:", choice_2)
#         st.write("Choice 3:", choice_32)
#         st.write("Choice 4:", choice_42)
#         st.write("Choice 5:", choice_52)
#         st.write("Choice 6:", choice_62)
#         st.write("Choice 7:", choice_72)
#         st.write("Choice 8:", choice_82)

# with st.form("form-3"):
#     text_input_3 = st.text_input("Enter Text 3")
#     choice_3 = st.selectbox("Choose Option 3", ["Option P", "Option Q"])
#     submitted_3 = st.form_submit_button(label="Submit")
#     if submitted_3:
#         st.write("3")
#         st.write("Text 3:", text_input_3)
#         st.write("Choice 3:", choice_3)

# with st.form("form-4"):
#     text_input_4 = st.text_input("Enter Text 4")
#     choice_4 = st.selectbox("Choose Option 4", ["Option M", "Option N"])
#     submitted_4 = st.form_submit_button(label="Submit")
#     if submitted_4:
#         st.write("4")
#         st.write("Text 4:", text_input_4)
#         st.write("Choice 4:", choice_4)
        
# import streamlit as st

# if "name" not in st.session_state:
#     st.session_state["name"] = ""

# def goto_level_3():
#     st.session_state["stage"] = "level_3"

# def goto_level_2():
#     st.session_state["stage"] = "level_2"

# def goto_level_1():
#     st.session_state["stage"] = "level_1"

# if "stage" not in st.session_state:
#     st.session_state["stage"] = "level_3"

# if st.session_state["stage"] == "level_3":
#     with st.form("level_3_form"):
#         st.caption("Level 3")
#         name = st.text_input("name", st.session_state['name'] )
#         st.session_state['name'] = name
        
#         submitted = st.form_submit_button(
#             "Generate level 2", on_click=goto_level_2
#         )

# if st.session_state["stage"] == "level_2":
#     with st.form("level_2_form"):
#         st.caption("Level 2")
#         st.write(st.session_state['name'])
#         b = st.text_input("lastname")
        
#         submitted = st.form_submit_button(
#             "Generate level 1", on_click=goto_level_1
#         )
# if st.session_state["stage"] == "level_1":
#     with st.form("level_1_form"):
#         st.caption("Level 1")
#         submitted = st.form_submit_button(
#             "Back to 3", on_click=goto_level_3
#         )


    
    
    # ... (rest of your form code with form-container class)


# with st.form("Search"):
#     keyword = st.text_input("Enter Your Keyword")
#     Search = st.form_submit_button("Search")
# placeholder=st.empty()
# if Search:
       
#         page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
#         soup = BeautifulSoup(page.content, 'lxml')
#         rows = soup.find_all("div", class_="ripi6")
#         col1,col2=placeholder.columns(2)
#         for row in rows:
#             figures = row.find_all("figure")
#             for i in range(2):
#                 img = figures[i].find("img", class_="YVj9w")
#                 list= img["srcset"]
#                 if i==0:
#                     col1.image(list[0])
#                 else:
                    # col2.image(list[0])
                    

        