# Carpeta Utils

## Descripción
Esta carpeta contiene utilidades, helpers y constantes que se utilizan en toda la aplicación.

## Estructura de Archivos

### `constants.py`
- Constantes globales
- Configuraciones
- Valores por defecto
- Enumeraciones

### `helpers.py`
- Funciones de utilidad
- Helpers de formato
- Conversiones
- Validaciones

### `web3_utils.py`
- Utilidades para Web3
- Funciones de wallet
- Helpers de blockchain
- Conversiones de unidades

### `three_utils.py`
- Utilidades para Three.js
- Helpers de geometría
- Funciones de materiales
- Utilidades de renderizado

## Uso

### Constantes
```python
from utils.constants import (
    DEFAULT_SCENE,
    CAMERA_SETTINGS,
    NETWORK_CONFIG
)
```

### Helpers
```python
from utils.helpers import (
    format_address,
    validate_input,
    convert_units
)
```

### Web3 Utils
```python
from utils.web3_utils import (
    connect_wallet,
    get_balance,
    send_transaction
)
```

### Three.js Utils
```python
from utils.three_utils import (
    create_material,
    setup_lighting,
    optimize_model
)
```

## Convenciones
- Funciones deben ser puras cuando sea posible
- Documentar todos los parámetros y retornos
- Incluir ejemplos de uso
- Mantener las funciones pequeñas y enfocadas

## Testing
- Cada utilidad debe tener tests unitarios
- Cubrir casos de borde
- Incluir mocks cuando sea necesario
- Mantener la cobertura de tests alta 