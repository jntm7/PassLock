import pytest
import passlock
import tkinter as tk

@pytest.fixture
# CREATE APP INSTANCE

def app():
    test_app = passlock.create_app()
    yield test_app
    # CLEANUP
    test_app.destroy()

# GET SUBMENU BY LABEL

def _get_submenu_by_label(root_menu, app, label):
    end_index = root_menu.index('end')
    if end_index is None:
        return None
    for i in range(end_index + 1):
        try:
            if root_menu.entrycget(i, "label") == label:
                menu_name = root_menu.entrycget(i, "menu")
                if menu_name:
                    return app.nametowidget(menu_name)
        except tk.TclError:
            continue
    return None

# ===============================================================
# TEST: MENUBAR TOP-LEVEL LABELS

def test_menubar_top_level_labels(app):
    menubar = passlock.menubar
    end_index = menubar.index('end')

    labels = []
    for i in range(end_index + 1):
        try:
            menu_type = menubar.type(i)
            # CHECK ONLY CASCADE MENUS
            if menu_type == 'cascade':
                label = menubar.entrycget(i, 'label')
                labels.append(label)
        except tk.TclError:
            continue

    expected = {"File", "Options", "Themes", "Password", "Tools", "Help"}
    assert expected.issubset(set(labels))

# ===============================================================
# TEST: THEME OPTIONS MATCHES JSON

def test_themes_menu_matches_themes_json(app):
    menubar = passlock.menubar
    themes_menu = _get_submenu_by_label(menubar, app, "Themes")
    assert themes_menu is not None
    
    # GET MENU THEMES
    end_index = themes_menu.index('end')
    menu_themes = []
    for i in range(end_index + 1):
        try:
            label = themes_menu.entrycget(i, "label")
            if label and label not in ["Dark Mode (On/Off)", ""]:
                menu_themes.append(label)
        except tk.TclError:
            continue
    
    # COMPARE WITH JSON
    expected_themes = set(passlock.themes.keys())
    actual_themes = set(menu_themes)
    assert expected_themes == actual_themes