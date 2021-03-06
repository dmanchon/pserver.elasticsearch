# -*- coding: utf-8 -*-

from plone.server.testing import PloneBaseLayer, TESTING_SETTINGS
from plone.server.content import load_cached_schema
from plone.server.interfaces import ICatalogUtility
from zope.component import getUtility
import requests

import unittest


TESTING_SETTINGS['applications'] = ['pserver.elasticsearch']

TESTING_SETTINGS['elasticsearch'] = {
    "bulk_size": 50,
    "index_name_prefix": "plone-",
    "connection_settings": {
        "endpoints": ["localhost:9200"],
        "sniffer_timeout": 0.5
    },
    "index": {},
    "mapping_overrides": {
        "*": {
        }
    }
}


class ElasticSearchLayer(PloneBaseLayer):

    def _get_site(self):
        """
        sometimes the site does not get updated data from zodb
        this seems to make it
        """
        return self.layer.new_root()['plone']

    @classmethod
    def setUp(cls):
        pass

    @classmethod
    def testSetUp(cls):
        pass

    @classmethod
    def testTearDown(cls):
        requests.delete('http://localhost:9200/plone-plone')

    @classmethod
    def tearDown(cls):
        pass


class ElasticSearchTestCase(unittest.TestCase):
    ''' Adding the OAuth utility '''
    layer = ElasticSearchLayer
