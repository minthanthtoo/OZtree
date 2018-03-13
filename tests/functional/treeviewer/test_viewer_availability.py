# -*- coding: utf-8 -*-
"""
Test the various tree views (linnean.html, AT.html, etc)
"""
import os.path
import shutil
from nose import tools
from time import sleep

from ...util import base_url, web2py_app_dir, humanOTT
from ..functional_tests import FunctionalTest


class TestViewerAvailability(FunctionalTest):
    """
    Test whether the embedding functions work
    """
    
    @classmethod
    def setUpClass(self):
        print("Running {}".format(os.path.basename(__file__)))
        super().setUpClass()

    @tools.nottest
    def test_available(self, controller, base=base_url):
        self.browser.get(base + controller)
        assert self.element_by_tag_name_exists('canvas'), "{} tree should always have a canvas element".format(controller)
        assert not self.element_by_class_exists('OneZoom_error'), "{} tree should not show the error text".format(controller)
    
    def test_life_available(self):
        """
        The default tree viewer should be available
        """
        self.test_available("life")
        assert self.element_by_class_exists('text_tree_root'), "Should have the text tree underlying the canvas"

    def test_life_MD_available(self):
        """
        The museum display viewer should be available
        """
        self.test_available("life_MD")

    def test_expert_mode_available(self):
        """
        The expert mode viewer (e.g. with screenshot functionality) should be available
        """
        self.test_available("life_expert")

    def test_AT_available(self):
        """
        The Ancestor's Tale tree (different colours) should be available
        """
        self.test_available("AT")

    def test_trail2016_available(self):
        """
        The Ancestor's Trail tree (different sponsorship details) should be available
        """
        self.test_available("trail2016")

    def test_linnean_available(self):
        """
        The Linnean Soc tree (different sponsorship details) should be available
        """
        self.test_available("linnean")

    def test_text_tree_available(self):
        """
        The root of the text-only tree should be viewable
        """
        self.browser.get(base_url + "life_text")
        assert self.element_by_class_exists('text_tree'), "Should have the text tree in a labelled div"
        assert self.element_by_class_exists('text_tree_root'), "Should have the root of the text tree in a labelled ul"

    def test_text_tree_leaves_available(self):
        """
        Leaves of the text-only tree should be viewable
        """
        self.browser.get(base_url + "life_text/@={}".format(humanOTT))
        assert self.element_by_class_exists('text_tree'), "Should have the text tree in a labelled div"
        assert self.element_by_class_exists('species'), "Should have the species in a labelled div"


    def test_minlife_available(self):
        """
        The minlife view for restricted installation should be should be available on the site
        """
        self.test_available("treeviewer/minlife")

    def test_minlife_static(self):
        """
        The minlife view should exist as a plain html file in static for restricted installation
        """
        #here we should also test whether the 
        f = "minlife.html"
        if os.path.isfile(os.path.join(web2py_app_dir, 'static', f)):
            self.test_available(f, "file://" + web2py_app_dir + "/static/")
        else:
            raise FileNotFoundError("To mun this test you need to create minlife.html by running `grunt partial-install`")