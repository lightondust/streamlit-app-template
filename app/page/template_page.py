from page.base_page import BasePage
import streamlit as st
from auth.login import login_component


class TemplatePage(BasePage):
    title = 'Template Page'

    def __init__(self, app_data, **kwargs):
        super().__init__(app_data, **kwargs)

    def run(self):
        st.title(TemplatePage.title)
        if_login = login_component(st)
        if if_login:
            st.write('hello: {}'.format(st.session_state.get('user')))
