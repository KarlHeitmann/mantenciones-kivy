
TIPO_DE_DATO = {
    "voltaje":[],"frecuencia":[],"horas":[],"temperatura_precision":[],
    "temperatura":["frio","tibio","caliente"],
    "valoracion":["malo","medio","bien", "N/A"],
    "nivel":["rellenado","normal","demasiado","alerta"],
    "consumible":["vacio","bajo","medio","alto"],
    "apriete":["reapretado","limpiado","ok"],
    "boolean":["si","no"],
    "falla":["alerta","ok"],
    "pintura":["repintado","medio","ok"],
    "colorbateria":["blanco", "negro", "verde"],
    "ok_falla": ["falla", "ok"],
    "ok_falla_no_tiene": ["falla", "ok", "no tiene"]
}

ITEMS_PRUEBA_MANTENIMIENTO = {
    "prueba_en_reposo" :{
        'apreciacion_general': {
            "label": "Apreciación General",
            "tipo": "valoracion",
            "value": None
        },
        "limpieza_general" : { "label" : 'Limpieza general', "tipo" : 'valoracion', "value" : None},
        "verificar_encendido_de_los_testigos_del_motor" : {
            "label": "Verificar encendido de los testigos del motor",
            "tipo" : 'falla',
            "value" : None
        },
        "nivel_aceite" : {"label" : 'Nivel aceite', "tipo" : 'nivel', "value" : None},
        "nivel_radiador" : {"label" : 'Nivel radiador', "tipo" : 'nivel', "value" : None},
        "nivel_petroleo" : {"label" : 'Nivel petroleo', "tipo" : 'consumible', "value" : None},
        "estado_bateria_1": {
            "label": "Estado de batería 1",
            "tipo": "colorbateria",
            "value": None
        },
        "estado_bateria_2": {
            "label": "Estado de batería 2",
            "tipo": "colorbateria",
            "value": None
        },
        "relleno_bateria": {
            "label": "Relleno de batería",
            "tipo": "nivel",
            "value": None
        },
        "calefactor_motor" : {"label" : 'Calefactor motor', "tipo" : 'temperatura', "value" : None},
        "horas_de_operacion" : {"label" : 'Horas de operacion', "tipo" : 'horas', "value" : None},
        "aprete_cables_y_limpieza_bornes_bateria" : {"label" : 'Aprete cables y limpieza bornes bateria', "tipo" : 'apriete', "value" : None},
        "voltaje_bateria_en_reposo" : {"label" : 'Voltajes bateria reposo', "tipo" : 'arreglo', "lista" : [
            {"label": "Voltaje bateria A en reposo", "tipo": 'voltaje' , "value" : None},
            {"label": "Voltaje bateria B en reposo", "tipo": 'voltaje' , "value" : None},
        ]},
        "estado_motor" : {"label" : 'Estado motor', "tipo" : 'valoracion', "value" : None},
        "estado_cables" : {"label" : 'Estado cables', "tipo" : 'valoracion', "value" : None},
        "eficiencia_radiador_limpieza" : {"label" : 'Eficiencia radiador (limpieza)', "tipo" : 'valoracion', "value" : None},
        "chequeo_termostato" : {"label" : 'Chequeo termostato', "tipo" : 'falla', "value" : None},
        "pintura" : {"label" : 'Pintura', "tipo" : 'pintura', "value" : None},
        "chequeo_pernos" : {"label" : 'Chequeo pernos', "tipo" : 'apriete', "value" : None},
        "estado_generador" : {"label" : 'Estado generador', "tipo" : 'valoracion', "value" : None},
        "verificar_apriete_conexiones" : {"label" : 'Verificar apriete conexiones', "tipo" : 'apriete', "value" : None},
        "cables_de_potencia" : {"label" : 'Cables de potencia', "tipo" : 'apriete', "value" : None}
    },
    "prueba_manual" : {
        "operacion_controles" : {"label": "Operacion controles", "tipo": 'falla', "value" : None},
        "voltaje_R_N" : {"label": "Voltaje R-N", "tipo" : 'voltaje', "value" : None},
        "voltaje_S_N" : {"label": "Voltaje S-N", "tipo" : 'voltaje', "value" : None},
        "voltaje_T_N" : {"label": "Voltaje T-N", "tipo" : 'voltaje', "value" : None},
        "voltaje_R_S" : {"label": "Voltaje R-S", "tipo" : 'voltaje', "value" : None},
        "voltaje_R_T" : {"label": "Voltaje R-T", "tipo" : 'voltaje', "value" : None},
        "voltaje_S_T" : {"label": "Voltaje S-T", "tipo" : 'voltaje', "value" : None},
        "frecuencia" : {"label": "Frecuencia", "tipo" : 'frecuencia', "value" : None},
        "voltaje_bateria_minimo_al_partir" : {"label" : 'Voltajes bateria minimo al partir', "tipo" : 'voltaje', "value" : None},
        "voltaje_bateria_en_operacion" : {"label" : 'Voltajes baterias en operacion', "tipo" : 'voltaje', "value" : None },
        "relleno_bateria" : {"label" : 'Fue necesario hacer \n relleno bateria?', "tipo" : 'boolean', "value" : None},
        "tiene_fugas": { "label": 'Tiene fugas?', "tipo": "boolean"}
    },

    "prueba_automatico" : {
        "encendido_motor_corte_energia" : {
            "label": 'Encendido de motor ante corte de energia',
            "tipo": 'ok_falla',
            "value" : None
        },
        "conexion_grupo_planta" : {
            "label": 'Conexion del grupo a planta',
            "tipo": 'ok_falla',
            "value" : None
        },
        "planta_conectada_grupo" : {
            "label": 'Planta conectada a grupo por 5 minutos',
            "tipo": 'ok_falla',
            "value" : None
        },
        "transferencia_carga_ante_vuelta_red" : {
            "label": 'Transferencia de carga ante vuelta de red',
            "tipo": 'ok_falla',
            "value" : None
        },
        "cooldown" : {
            "label": 'Cooldown 2 minutos',
            "tipo": 'ok_falla_no_tiene',
            "value" : None
        }
    }
}


