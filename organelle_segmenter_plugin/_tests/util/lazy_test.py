import pytest

from organelle_segmenter_plugin.util.lazy import lazy_property


class TestLazy:
    def test_lazy_property(self):
        class TestObject:
            @lazy_property
            def property1(self):
                return object()

        test_obj = TestObject()
        obj_id = id(test_obj.property1)
        for i in range(10):
            assert obj_id == id(test_obj.property1)
