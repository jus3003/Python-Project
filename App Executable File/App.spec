from kivy_deps import sdl2, glew


# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['App.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

a.datas += [('Code\my.kv', 'C:\\Users\\jusxp\\Desktop\\UBC\\UT Grad School\\Python\\Git Project\\Python-Project\\App Executable File\my.kv', 'DATA')]

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='App',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,Tree ('C:\\Users\\jusxp\\Desktop\\UBC\\UT Grad School\\Python\\Git Project\\Python-Project\\App Executable File\\'), 
    a.binaries,     
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='App',
)
