import streamlit as st

from app_url import AppURL
from page.template_page import TemplatePage
from page.example_page import ExamplePage
from page.main_page import MainPage
from app_data import get_app_data
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%m/%d/%Y %X")

st.set_page_config(layout='wide', page_title='streamlit apps template', page_icon='./favico_s_t.png')


@st.cache(allow_output_mutation=True)
def _get_app_data(page_class):
    return get_app_data(page_class)


page_class_list = [MainPage, ExamplePage, TemplatePage]
page_class = {p.title: p for p in page_class_list}
page_selected = st.sidebar.radio('page:', list(page_class.keys())+[''], index=len(page_class))

app_data = _get_app_data(page_class)
app_url = AppURL()
page = app_url.sync_variable('page', page_selected, MainPage.title)

page_obj = page_class[page](app_data=app_data, app_url=app_url)
page_obj.run()
