# Modelos de WoldVirtual Crypto 3D

Este directorio contiene los modelos de datos principales del metaverso WoldVirtual Crypto 3D.

## Estructura del Directorio

```
models/
├── user.py          # Modelo de usuario
├── asset.py         # Modelo de activo digital
├── scene.py         # Modelo de escena 3D
└── transaction.py   # Modelo de transacción
```

## Modelos Principales

### 1. Usuario (`user.py`)
- Información básica del usuario
- Credenciales y autenticación
- Preferencias y configuración
- Inventario y posesiones
- Estadísticas y reputación

#### Atributos Principales
- `username`: Nombre de usuario único
- `email`: Correo electrónico
- `wallet_address`: Dirección de wallet
- `created_at`: Fecha de creación
- `is_active`: Estado de la cuenta
- `is_verified`: Estado de verificación
- `avatar_url`: URL del avatar
- `theme`: Preferencia de tema
- `language`: Idioma preferido
- `owned_assets`: Lista de activos poseídos
- `created_scenes`: Lista de escenas creadas
- `total_transactions`: Total de transacciones
- `reputation_score`: Puntuación de reputación

### 2. Activo Digital (`asset.py`)
- Metadatos del activo
- Propiedades 3D
- Información de blockchain
- Historial de propiedad

#### Atributos Principales
- `name`: Nombre del activo
- `description`: Descripción detallada
- `type`: Tipo de activo
- `format`: Formato del archivo
- `file_url`: URL del archivo
- `thumbnail_url`: URL de la miniatura
- `price`: Precio en tokens
- `owner`: Propietario actual
- `creator`: Creador original
- `created_at`: Fecha de creación
- `updated_at`: Fecha de actualización
- `token_id`: ID del token NFT
- `contract_address`: Dirección del contrato
- `properties`: Propiedades personalizadas
- `tags`: Etiquetas de categorización

### 3. Escena 3D (`scene.py`)
- Configuración de la escena
- Elementos 3D
- Interactividad
- Permisos y acceso

#### Atributos Principales
- `name`: Nombre de la escena
- `description`: Descripción detallada
- `creator`: Creador de la escena
- `created_at`: Fecha de creación
- `updated_at`: Fecha de actualización
- `is_public`: Visibilidad pública
- `thumbnail_url`: URL de la miniatura
- `scene_data`: Datos de la escena
- `assets`: Activos utilizados
- `settings`: Configuración de la escena
- `permissions`: Permisos de acceso
- `tags`: Etiquetas de categorización
- `views`: Número de visitas
- `likes`: Número de me gusta

### 4. Transacción (`transaction.py`)
- Registro de transacciones
- Información de blockchain
- Estado y confirmación
- Historial de cambios

#### Atributos Principales
- `transaction_hash`: Hash de la transacción
- `type`: Tipo de transacción
- `from_address`: Dirección de origen
- `to_address`: Dirección de destino
- `amount`: Cantidad de tokens
- `asset_id`: ID del activo (si aplica)
- `scene_id`: ID de la escena (si aplica)
- `status`: Estado de la transacción
- `created_at`: Fecha de creación
- `confirmed_at`: Fecha de confirmación
- `block_number`: Número de bloque
- `gas_used`: Gas utilizado
- `gas_price`: Precio del gas
- `metadata`: Metadatos adicionales

## Relaciones entre Modelos

1. **Usuario - Activo**
   - Un usuario puede poseer múltiples activos
   - Un activo pertenece a un usuario
   - Relación muchos a uno

2. **Usuario - Escena**
   - Un usuario puede crear múltiples escenas
   - Una escena pertenece a un usuario
   - Relación muchos a uno

3. **Escena - Activo**
   - Una escena puede contener múltiples activos
   - Un activo puede ser usado en múltiples escenas
   - Relación muchos a muchos

4. **Transacción - Usuario**
   - Un usuario puede tener múltiples transacciones
   - Una transacción involucra a dos usuarios
   - Relación muchos a muchos

## Validaciones

1. **Usuario**
   - Username único
   - Email válido
   - Wallet address válida
   - Contraseña segura

2. **Activo**
   - Nombre único
   - Formato de archivo válido
   - Precio positivo
   - Token ID único

3. **Escena**
   - Nombre único por usuario
   - Configuración válida
   - Permisos válidos

4. **Transacción**
   - Hash único
   - Direcciones válidas
   - Monto positivo
   - Estado válido

## Métodos Comunes

1. **Creación**
   - Validación de datos
   - Generación de IDs
   - Registro de timestamps

2. **Actualización**
   - Validación de cambios
   - Registro de modificaciones
   - Notificaciones

3. **Eliminación**
   - Verificación de permisos
   - Limpieza de relaciones
   - Registro de eliminación

4. **Búsqueda**
   - Filtrado por atributos
   - Ordenamiento
   - Paginación 