from invisibleroads_macros_descriptor import cachedproperty, classproperty


class X(object):
    a_call_count = 0
    b_call_count = 0

    @classproperty
    def a(Class):
        Class.a_call_count += 1
        return Class.a_call_count

    @cachedproperty
    def b(Class):
        Class.b_call_count += 1
        return Class.b_call_count


def test_classproperty():
    assert X.a == 1
    assert X.a == 2


def test_cachedproperty():
    x = X()
    assert x.b == 1
    assert x.b == 1
