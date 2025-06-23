def test_import_tmos():
    """Test that the tmos module can be imported."""
    from lib.tmos.tmos import OS
    assert OS is not None