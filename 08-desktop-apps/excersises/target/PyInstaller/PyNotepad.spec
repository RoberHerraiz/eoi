# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/herraiz/Proyectos/eoi/08-desktop-apps/excersises/src/main/python/main.py'],
             pathex=['/home/herraiz/Proyectos/eoi/08-desktop-apps/excersises/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/home/herraiz/.virtualenvs/qvenv/lib/python3.8/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/home/herraiz/Proyectos/eoi/08-desktop-apps/excersises/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='PyNotepad',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='PyNotepad')
