def test_import_tmos_ui_StaticPage():
    """Test that the tmos_ui StaticPage module can be imported."""
    from lib.tmos.tmos_ui import StaticPage
    assert StaticPage is not None

def test_import_tmos_ui_WindowManager():
    """Test that the tmos_ui WindowManager module can be imported."""
    from lib.tmos.tmos_ui import WindowManager
    assert WindowManager is not None

def test_import_tmos_ui_to_screen():
    """Test that the tmos_ui to_screen module can be imported."""
    from lib.tmos.tmos_ui import to_screen
    assert to_screen is not None