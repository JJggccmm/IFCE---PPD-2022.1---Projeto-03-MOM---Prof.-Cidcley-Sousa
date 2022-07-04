# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['cria_Cliente.py'],
             pathex=[],
             binaries=[],
             datas=[('recursos/icone.ico','recursos'),('recursos/gifs/cliente_title_GIF.gif','recursos/gifs'),('recursos/gifs/cliente_main_GIF.gif','recursos/gifs'),('recursos/bg_janela_Inicial_cliente.png','recursos'),('recursos/botao_gerar_Cliente.png','recursos'),('recursos/botao_criar.png','recursos'),('recursos/bg_configurar_Cliente.png','recursos'),('recursos/bg_Cliente.png','recursos')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='cria_Cliente',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
