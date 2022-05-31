from page.base_page import BasePage
import streamlit as st


class ExamplePage(BasePage):
    title = 'Example Page'

    def __init__(self, app_data, **kwargs):
        super().__init__(app_data, **kwargs)

    def run(self):
        st.title(ExamplePage.title)
        choice_selected = st.selectbox('choice:', [''] + ['a', 'b', 'c'])
        choice = self.app_url.sync_variable('choice', choice_selected, '')
        st.write(choice)

        choices_selected = st.multiselect('choices', ['', 'a', 'b', 'c', 'd'])
        choices = self.app_url.sync_variable_list('choice', choices_selected, [])
        st.write(choices)
