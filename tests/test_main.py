from main import SimplePage

def test_simple_page_initialization():
    """Test that SimplePage initializes with correct attributes."""
    page = SimplePage("Test Page", "This is a test page.", bg=0xFF0000)
    assert page.title == "Test Page"
    assert page.text == "This is a test page."
    assert page.bg == 0xFF0000