# WoldVirtual Crypto 3D - Metaverso Descentralizado

## 🚀 Descripción
WoldVirtual es un metaverso cripto 3D descentralizado y de código abierto que permite a los usuarios crear, explorar y monetizar experiencias virtuales. Construido con Reflex y Three.js, ofrece una plataforma completa para la creación de mundos virtuales.

## 🏗️ Arquitectura del Proyecto

### Estructura de Carpetas
```
WoldVirtual_Crypto_3D/
├── components/          # Componentes reutilizables
│   ├── scene.py        # Escena 3D con Three.js
│   └── ui.py           # Componentes de interfaz
├── assets/             # Recursos estáticos
│   ├── models/         # Modelos 3D
│   ├── textures/       # Texturas
│   └── sounds/         # Audio
├── utils/              # Utilidades
│   ├── constants.py    # Constantes globales
│   ├── helpers.py      # Funciones de ayuda
│   └── web3_utils.py   # Utilidades blockchain
└── models/             # Modelos de datos
```

### Archivos Principales
- `WoldVirtual_Crypto_3D.py`: Punto de entrada de la aplicación
- `state.py`: Gestión del estado global
- `styles.py`: Estilos globales
- `rxconfig.py`: Configuración de Reflex

## 🛠️ Tecnologías Principales

### Frontend
- **Reflex**: Framework Python Full-Stack
- **Three.js**: Motor 3D
- **React Three Fiber**: Integración React con Three.js
- **React Three Drei**: Componentes útiles para Three.js

### Backend
- **Reflex**: Manejo de estado y lógica de negocio
- **SQLite**: Base de datos (desarrollo)
- **Web3.py**: Integración con blockchain

### Blockchain
- **Ethereum/Polygon**: Redes soportadas
- **Web3.js**: Interacción con smart contracts
- **IPFS**: Almacenamiento descentralizado

## 📋 Requisitos del Sistema

### Desarrollo
- Python 3.8+
- Node.js 16+
- WebGL 2.0 compatible
- Git

### Producción
- Servidor con soporte WebGL
- Base de datos PostgreSQL
- Nodo blockchain
- Servidor IPFS

## 🚀 Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/WoldVirtual_Crypto_3D.git
cd WoldVirtual_Crypto_3D
```

### 2. Configurar Entorno Virtual
```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows
.venv\Scripts\activate
# Unix/Mac
source .venv/bin/activate
```

### 3. Instalar Dependencias
```bash
# Instalar dependencias Python
pip install -r requirements.txt

# Instalar dependencias Node.js
npm install
```

### 4. Configurar Variables de Entorno
```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tus configuraciones
```

## 💻 Desarrollo

### Iniciar Servidor de Desarrollo
```bash
reflex run
```
La aplicación estará disponible en `http://localhost:3000`

### Estructura de Desarrollo
- `components/`: Componentes reutilizables
- `assets/`: Recursos estáticos
- `utils/`: Utilidades y helpers
- `models/`: Modelos de datos

## 🎮 Características Principales

### Renderizado 3D
- Escenas inmersivas
- Física realista
- Iluminación dinámica
- Optimización de rendimiento

### Integración Blockchain
- Conexión de wallets
- NFTs para activos
- Marketplace descentralizado
- Gobernanza DAO

### Creación de Contenido
- Editor de escenas
- Importación de modelos
- Sistema de terrenos
- Creación de avatares

## 📚 Documentación

### Guías
- [Guía de Desarrollo](docs/development.md)
- [Guía de Contribución](docs/contributing.md)
- [Guía de Despliegue](docs/deployment.md)

### API
- [API Reference](docs/api.md)
- [Componentes](docs/components.md)
- [Estado](docs/state.md)

## 🤝 Contribuir

### Proceso de Contribución
1. Fork el repositorio
2. Crear rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

### Convenciones de Código
- PEP 8 para Python
- TypeScript para componentes
- Documentación con docstrings
- Tests unitarios

## 📝 Licencia
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📞 Contacto
- Website: [woldvirtual.com](https://woldvirtual.com)
- Discord: [Discord Server](https://discord.gg/woldvirtual)
- Twitter: [@WoldVirtual](https://twitter.com/WoldVirtual)

## 🙏 Agradecimientos
- Reflex por el framework
- Three.js por el motor 3D
- La comunidad de código abierto
