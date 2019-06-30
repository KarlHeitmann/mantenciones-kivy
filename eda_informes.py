
TIPO_DE_DATO = {
    "voltaje":[],"frecuencia":[],"horas":[],"temperatura_precision":[],
    "temperatura":["frio","tibio","caliente"],
    "valoracion":["malo","medio","bien"],
    "nivel":["rellenado","normal","demasiado","alerta"],
    "consumible":["vacio","bajo","medio","alto"],
    "apriete":["reapretado","limpiado","ok"],
    "boolean":["si","no"],
    "falla":["alerta","ok"],
    "pintura":["repintado","medio","ok"]
}

ITEMS_PRUEBA_MANTENIMIENTO = {
    "prueba_en_reposo" :{
        "limpieza_general" : { "label" : 'Limpieza general', "tipo" : 'valoracion', "value" : None},
        "nivel_aceite" : {"label" : 'Nivel aceite', "tipo" : 'nivel', "value" : None},
        "nivel_radiador" : {"label" : 'Nivel radiador', "tipo" : 'nivel', "value" : None},
        "nivel_petroleo" : {"label" : 'Nivel petroleo', "tipo" : 'consumible', "value" : None},
        "calefactor_motor" : {"label" : 'Calefactor motor', "tipo" : 'temperatura', "value" : None},
        "horas_de_operacion" : {"label" : 'Horas de operacion', "tipo" : 'horas', "value" : None},
        "aprete_cables_y_limpieza_bornes_bateria" : {"label" : 'Aprete cables y limpieza bornes bateria', "tipo" : 'apriete', "value" : None},
        "voltaje_bateria_en_reposo" : {"label" : 'Voltajes bateria reposo', "tipo" : 'arreglo', "lista" : [
            {"label": "Voltaje bateria A en reposo", "tipo": 'voltaje' , "value" : None},
            {"label": "Voltaje bateria B en reposo", "tipo": 'voltaje' , "value" : None},
            {"label": "Voltaje bateria C en reposo", "tipo": 'voltaje' , "value" : None}
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
        "frecuencia" : {"label": "Frecuencia", "tipo" : 'frecuencia', "value" : None},
        "voltaje_bateria_en_operacion" : {"label" : 'Voltajes baterias en operacion', "tipo" : 'arreglo', "lista" : [
            {"label": "Voltaje bateria A en reposo", "tipo": 'voltaje' , "value" : None},
            {"label": "Voltaje bateria B en reposo", "tipo": 'voltaje' , "value" : None},
            {"label": "Voltaje bateria C en reposo", "tipo": 'voltaje' , "value" : None}
        ]},
        "voltaje_bateria_minimo_al_partir" : {"label" : 'Voltajes baterias reposo', "tipo" : 'arreglo', "lista" : [
            {"label": "Voltaje bateria A en reposo", "tipo": 'voltaje' , "value" : None},
            {"label": "Voltaje bateria B en reposo", "tipo": 'voltaje' , "value" : None},
            {"label": "Voltaje bateria C en reposo", "tipo": 'voltaje' , "value" : None}
        ]},
        "relleno_bateria" : {"label" : 'Relleno bateria', "tipo" : 'boolean', "value" : None}
    },
    "prueba_automatico" : {
        "verificar_encendido_de_los_testigos_del_motor" : {
            "label": "Verificar encendido de los testigos del motor",
            "tipo" : 'falla',
            "value" : None
        }
    }
}


