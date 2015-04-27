--------------------------------------------------------
--  DDL for View AAD_AUDITORIA
--------------------------------------------------------

  CREATE OR REPLACE FORCE VIEW "ICEBERG_PRE"."AAD_AUDITORIA" ("SEC_AUDITORIA", "INSTANTE", "TABLA", "SEC_REGISTRO", "OPERACION", "SEC_CUENTA_ICEBERG", "SEC_EJECUTABLE", "REGISTRO_ANTERIOR", "REGISTRO_NUEVO") AS 
  SELECT 
    AUD.SEC_Auditoria,
    AUD.Instante,
    AUD.Tabla,
    AUD.SEC_Registro,
    AUD.Operacion,
    AUD.SEC_Cuenta_ICEBERG,
    AUD.SEC_Ejecutable,
    AUD.Registro_Anterior,
    AUD.Registro_Nuevo
FROM AAT_Auditoria Aud
 ;
