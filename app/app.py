import streamlit as st

from app_url import AppURL
from page.template_page import TemplatePage
from page.main_page import MainPage
from app_data import get_app_data
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%m/%d/%Y %X")

st.set_page_config(layout='wide', page_title='top2vec', page_icon='./favico_s_t.png')


@st.cache(allow_output_mutation=True)
def _get_app_data(page_class):
    return get_app_data(page_class)


page_class = {
    'Main page': MainPage,
    'Template page': TemplatePage
}
page_selected = st.sidebar.radio('page:', list(page_class.keys())+[''], index=len(page_class))

app_data = _get_app_data(page_class)
app_url = AppURL()

if page_selected:
    app_url.set_query_params('page', page_selected)
    page = page_selected
else:
    if app_url.page:
        page = app_url.page
    else:
        page = 'Main page'

page_obj = page_class[page](app_data=app_data, app_url=app_url)
page_obj.run()
