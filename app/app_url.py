import streamlit as st
import urllib


class AppURL(object):
    def __int__(self):
        pass

    @property
    def query_params(self):
        query_params = st.experimental_get_query_params()
        return query_params

    @property
    def page(self):
        return self.query_params.get('page', [''])[0]

    @property
    def token(self):
        return self.query_params.get('token', [''])[0]

    @property
    def tag(self):
        return self.query_params.get('tag', [''])[0]

    def set_query_params(self, key, value):
        params = self.query_params
        params[key] = value
        st.experimental_set_query_params(**params)

    def internal_link(self, **params):
        params_new = self.query_params
        for k, v in params.items():
            params_new[k] = v
        d_qs = urllib.parse.urlencode(params, doseq=True)
        return './?{}'.format(d_qs)
