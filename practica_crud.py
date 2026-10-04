import sqlite3

DB = "quantum_wallet.db"


# ============================================================
# CREATE (C)
# Inserta un nuevo contacto para el usuario indicado.
# ============================================================
def crear_contacto(nombre, alias, id_usuario):
    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO contactos (nombre, apodo, id_usuario)
        VALUES (?, ?, ?)
    """, (nombre, alias, id_usuario))

    conexion.commit()
    id_contacto = cursor.lastrowid
    conexion.close()

    print(f"[C] Contacto creado correctamente: ID {id_contacto} - {nombre} ({alias})")
    return id_contacto


# ============================================================
# READ (R)
# Lee y muestra todos los contactos pertenecientes al usuario.
# ============================================================
def leer_contactos(id_usuario):
    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_contacto, nombre, apodo, id_usuario
        FROM contactos
        WHERE id_usuario = ?
        ORDER BY id_contacto
    """, (id_usuario,))

    contactos = cursor.fetchall()
    conexion.close()

    print("\n[R] Contactos del usuario", id_usuario)
    for contacto in contactos:
        print(contacto)

    print(f"[R] Lectura completada correctamente. Registros encontrados: {len(contactos)}")
    return contactos


# ============================================================
# UPDATE (U)
# Cambia el alias/apodo de un contacto.
# ============================================================
def actualizar_alias(id_contacto, nuevo_alias):
    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE contactos
        SET apodo = ?
        WHERE id_contacto = ?
    """, (nuevo_alias, id_contacto))

    conexion.commit()
    filas_afectadas = cursor.rowcount
    conexion.close()

    if filas_afectadas:
        print(f"[U] Alias actualizado correctamente. Contacto ID {id_contacto}: {nuevo_alias}")
    else:
        print(f"[U] No se encontró el contacto con ID {id_contacto}")

    return filas_afectadas


# ============================================================
# DELETE (D)
# Elimina un contacto mediante su ID.
# ============================================================
def eliminar_contacto(id_contacto):
    conexion = sqlite3.connect(DB)
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM contactos
        WHERE id_contacto = ?
    """, (id_contacto,))

    conexion.commit()
    filas_afectadas = cursor.rowcount
    conexion.close()

    if filas_afectadas:
        print(f"[D] Contacto con ID {id_contacto} eliminado correctamente.")
    else:
        print(f"[D] No se encontró el contacto con ID {id_contacto}")

    return filas_afectadas


# ============================================================
# PRUEBA DE LAS 4 OPERACIONES CRUD
# ============================================================
if __name__ == "__main__":

    print("========== PRACTICA CRUD ==========")

    # CREATE: crear el contacto que se mostrará en la captura "Antes".
    id_nuevo = crear_contacto(
        "Daniel Dev",
        "Dani",
        1
    )

    # READ: mostrar los contactos del usuario 1.
    leer_contactos(1)

    # UPDATE: cambiar el alias del contacto recién creado.
    actualizar_alias(
        id_nuevo,
        "Dani Pro"
    )

    print("\nDespués del UPDATE:")
    leer_contactos(1)

    # DELETE: eliminar el contacto con ID 2, como solicita la actividad.
    eliminar_contacto(2)

    print("\nDespués del DELETE:")
    leer_contactos(1)

    print("\n========== CRUD COMPLETADO ==========")
