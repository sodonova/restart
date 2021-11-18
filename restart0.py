import streamlit as st
import json

# st.title("Restart: Write our resume")

with open('resume.json') as jsonfile:
    obj = json.load(jsonfile)
# print(obj['Education']['GPA'])
obj['Sections'] = obj['Sections'][:-2]
st.markdown(f'# {obj["Name"]}')
# form = st.sidebar.form(key='arbitrary_string')
for section in obj['Sections']:
    st.markdown(f'## {section}')
    # selected_sections = form.multiselect(f'In {section}, see:',obj[section])
    selected_sections = st.sidebar.multiselect(f'In {section}, see:',obj[section])
    for subsection in selected_sections:
        if type(obj[section][subsection]) == list:
            obj[section][subsection] = ', '.join(obj[section][subsection])
        # if st.sidebar.checkbox(f'Show {subsection}'):
        if len(subsection + str(obj[section][subsection])) < 100:
            st.markdown(f'**{subsection}:** {obj[section][subsection]}')
        else:
            st.markdown(f'**{subsection}:**  \n{obj[section][subsection]}')
        # print(subsection, obj[section][subsection])    
# form.form_submit_button('Write resume')