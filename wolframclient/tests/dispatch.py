# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from wolframclient.tests.utils.base import TestCase as BaseTestCase
from wolframclient.utils.dispatch import ClassDispatch, Dispatch

import math

class TestCase(BaseTestCase):

    def test_dispatch(self):

        dispatcher = Dispatch()

        @dispatcher.default()
        def normalizer(o):
            return o

        @dispatcher.multi((int, float))
        def normalizer(o):
            return o * 2

        @dispatcher.multi(unicode)
        def normalizer(o):
            return 'Hello %s' % o

        self.assertEqual(normalizer('Ric'), 'Hello Ric')
        self.assertEqual(normalizer(2),     4)
        self.assertEqual(normalizer(None),  None)

    def test_dispatch_multi(self):

        dispatcher = Dispatch()

        @dispatcher.default()
        def normalizer(a, b):
            return (a, b)

        @dispatcher.multi(int, int)
        def normalizer(a, b):
            return a + b

        @dispatcher.multi(int, float)
        def normalizer(a, b):
            return a + int(math.floor(b))

        @dispatcher.multi(float, float)
        def normalizer(a, b):
            return a + b

        self.assertEqual(normalizer("a", "b"), ("a", "b"))
        self.assertEqual(normalizer(1,   2  ), 3)
        self.assertEqual(normalizer(1,   4.5), 5)
        self.assertEqual(normalizer(1.2, 4.5), 5.7)

    def test_class_dispatch(self):

        dispatcher = ClassDispatch()

        class Foo(object):

            @dispatcher.default()
            def normalizer(self, o):
                return o

            @dispatcher.multi(unicode)
            def normalizer(self, o):
                return 'Hello %s' % o

            @dispatcher.multi(int)
            def normalizer(self, o):
                return o * 2

        self.assertEqual(Foo().normalizer('Ric'), 'Hello Ric')
        self.assertEqual(Foo().normalizer(2),     4)
        self.assertEqual(Foo().normalizer(None),  None)