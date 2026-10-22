import invincible


def test_package_imports():
    assert invincible.__file__.endswith("something_else.py")
