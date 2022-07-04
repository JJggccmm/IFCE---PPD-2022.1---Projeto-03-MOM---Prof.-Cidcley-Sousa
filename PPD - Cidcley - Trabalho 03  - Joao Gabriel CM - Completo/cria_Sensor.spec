# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['cria_Sensor.py'],
             pathex=[],
             binaries=[],
             datas=[('recursos/icone.ico','recursos'),('recursos/gifs/sensor_title_GIF.gif','recursos/gifs'),('recursos/gifs/sensor_main_GIF.gif','recursos/gifs'),('recursos/bg_janela_Inicial_sensor.png','recursos'),('recursos/botao_gerar_Sensor.png','recursos'),('recursos/botao_criar.png','recursos'),('recursos/bg_configurar_Sensor.png','recursos'),('recursos/bg_Sensor.png','recursos'),('recursos/configura_sensor_opcao_umidade.png','recursos'),('recursos/configura_sensor_opcao_temperatura.png','recursos'),('recursos/configura_sensor_opcao_velocidade.png','recursos'),('recursos/label_temperatura.png','recursos'),('recursos/label_umidade.png','recursos'),('recursos/label_velocidade.png','recursos'),('recursos/configura_sensor_opcao_umidade_on.png','recursos'),('recursos/configura_sensor_opcao_temperatura_on.png','recursos'),('recursos/configura_sensor_opcao_velocidade_on.png','recursos'),('recursos/label_temperatura_ON.png','recursos'),('recursos/label_umidade_ON.png','recursos'),('recursos/label_velocidade_ON.png','recursos'),('recursos/indicador_sensor_temperatura.png','recursos'),('recursos/indicador_sensor_umidade.png','recursos'),('recursos/indicador_sensor_velocidade.png','recursos'),('recursos/indicador_sensor_limite_on.png','recursos'),('recursos/indicador_sensor_limite_off.png','recursos')],
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
          name='cria_Sensor',
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
