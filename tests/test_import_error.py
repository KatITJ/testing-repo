raise RuntimeError("🔥 Import Error: This module fails at import time on purpose.")


def test_should_never_run():
    # This test will NEVER run because the module crashes before collection.
    assert True
