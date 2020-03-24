# -*- coding: utf-8 -*-

from urllib.parse import urljoin
from typing import Optional
from abc import ABCMeta

import requests


class BaseAPI(metaclass=ABCMeta):
    _session: Optional[requests.Session] = None

    url: str
    project: str

    email: Optional[str]
    password: Optional[str]

    def __init__(
        self,
        url: str,
        project: str,
        email: Optional[str] = None,
        password: Optional[str] = None,
    ):
        self.url = url
        self.project = project
        self.email = email
        self.password = password

    @property
    def session(self) -> requests.Session:
        if self._session is None:
            self._session = requests.Session()
        return self._session

    def _enpoint_url(self, endpoint: str):
        """
        Join base url, with an endpoint
        """
        return urljoin(self.url, endpoint.format(project=self.project))

    def post(self, url, **kwargs):
        return self.session.post(self._enpoint_url(url), **kwargs)
