import streamlit as st
import json

# st.title("Restart: Write our resume")
MAX_LINE_LEN = 100
@st.cache
def load_df():
    with open('resume.json') as jsonfile:
        loaded_obj = json.load(jsonfile)
    # loaded_obj['Sections'] = loaded_obj['Sections'][:-2]
    return loaded_obj


resume = load_df() # resume as dict from json
# resume['Sections'] = resume['Sections'][:-2]

# print(resume['Education']['GPA'])
st.sidebar.markdown("""## Welcome!  \nRestart the resume process. 
                    You should have a personalized version of my resume - after all, you know 
                    what's relevant best. Start typing in the fields below to generate a resume.""")
st.markdown(f'# {resume["Name"]}')
# form = st.sidebar.form(key='arbitrary_string')
selected_sections = st.sidebar.multiselect('Sections', resume['Sections'], resume['Sections'])
for section in selected_sections:
    st.markdown(f'## {section}')

    # make sections selectable
    section_expander = st.sidebar.expander(section)
    selected_subsections = section_expander.multiselect(f'In {section}, see:',
                                                        options=resume[section],
                                                        default=list(resume[section].keys())[0],
                                                        key=f'{section}_disregard')
    num_columns = section_expander.selectbox('Columns', [1, 2, 3], index=0, key=f'{section}_disregard2')

    columns = st.columns(num_columns)
    column_counter = 0
    current_column = columns[column_counter]
    for subsection in selected_subsections:
        # handle list of items like languages
        content = resume[section][subsection]
        if type(resume[section][subsection]) == list:
            first_n_items = section_expander.slider(f'Number of items in {subsection}',
                                    min_value=1,
                                    max_value=len(resume[section][subsection]),
                                    value=len(resume[section][subsection]),
                                    step=1)
            maxlen = 0
            for item in content:
                if len(item) > maxlen:
                    maxlen = len(item)
            if maxlen < MAX_LINE_LEN:
                content = ', '.join(resume[section][subsection][:first_n_items])
            else:
                content = ' '.join(resume[section][subsection][:first_n_items])

        # if st.sidebar.checkbox(f'Show {subsection}'):
        if len(subsection + str(resume[section][subsection])) < MAX_LINE_LEN:
            current_column.markdown(f'**{subsection}:** {content}')
        else:
            current_column.markdown(f'**{subsection}:**  \n{content}')
        # print(subsection, obj[section][subsection])
        column_counter = (column_counter + 1) % len(columns)
        current_column = columns[column_counter]

# form.form_submit_button('Write resume')