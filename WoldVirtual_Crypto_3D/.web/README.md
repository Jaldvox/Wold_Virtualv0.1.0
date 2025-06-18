# WoldVirtual Web

Este directorio contiene la implementación web del metaverso WoldVirtual, construido con Next.js, TypeScript y tecnologías modernas de desarrollo web.

## 🚀 Características Principales

- **Desarrollo Moderno**
  - TypeScript para tipado estático
  - Next.js 14 para renderizado híbrido
  - Chakra UI para componentes y temas
  - Web3 y ethers.js para integración blockchain
  - Three.js para gráficos 3D
  - Zustand para gestión de estado
  - SWR y React Query para manejo de datos

- **Herramientas de Desarrollo**
  - ESLint y Prettier para calidad de código
  - Jest para pruebas unitarias
  - Cypress para pruebas E2E
  - Storybook para documentación de componentes
  - Husky para git hooks
  - TypeScript para tipado estático

## 📁 Estructura del Proyecto

```
src/
  ├── components/     # Componentes reutilizables
  ├── hooks/         # Custom hooks
  ├── utils/         # Utilidades y helpers
  ├── styles/        # Estilos globales y temas
  ├── types/         # Definiciones de TypeScript
  ├── context/       # Contextos de React
  ├── services/      # Servicios y APIs
  ├── store/         # Estado global con Zustand
  ├── pages/         # Páginas de Next.js
  └── assets/        # Recursos estáticos
```

## 🛠️ Configuración

### Requisitos Previos

- Node.js 18.x o superior
- npm 9.x o superior
- Git

### Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/woldvirtual.git
cd woldvirtual/.web
```

2. Instalar dependencias:
```bash
npm install
```

3. Configurar variables de entorno:
```bash
cp .env.example .env.local
```

### Scripts Disponibles

- `npm run dev` - Inicia el servidor de desarrollo
- `npm run build` - Construye la aplicación para producción
- `npm run start` - Inicia el servidor de producción
- `npm run lint` - Ejecuta el linter
- `npm run test` - Ejecuta las pruebas unitarias
- `npm run test:watch` - Ejecuta las pruebas en modo watch
- `npm run test:coverage` - Genera reporte de cobertura de pruebas
- `npm run storybook` - Inicia Storybook
- `npm run cypress` - Abre Cypress para pruebas E2E
- `npm run cypress:headless` - Ejecuta pruebas E2E en modo headless

## 🧪 Testing

### Pruebas Unitarias (Jest)
```bash
npm run test
```

### Pruebas E2E (Cypress)
```bash
npm run cypress
```

### Documentación de Componentes (Storybook)
```bash
npm run storybook
```

## 📦 Dependencias Principales

### Producción
- `@chakra-ui/react` - UI Components
- `ethers` - Web3 Integration
- `framer-motion` - Animaciones
- `next` - Framework
- `react-query` - Data Fetching
- `three` - 3D Graphics
- `web3` - Blockchain Integration
- `zustand` - State Management

### Desarrollo
- `@testing-library` - Testing
- `cypress` - E2E Testing
- `eslint` - Linting
- `jest` - Unit Testing
- `prettier` - Code Formatting
- `storybook` - Component Documentation
- `typescript` - Type Checking

## 🔧 Configuraciones

### TypeScript (tsconfig.json)
- Configuración estricta
- Path aliases para imports limpios
- Soporte para JSX/TSX
- Configuración de módulos ES

### ESLint (.eslintrc.json)
- Reglas para React y TypeScript
- Integración con Prettier
- Reglas personalizadas para el proyecto

### Prettier (.prettierrc)
- Configuración de formato de código
- Integración con ESLint
- Reglas de estilo consistentes

### Jest (jest.config.js)
- Configuración para pruebas unitarias
- Integración con Next.js
- Path aliases
- Configuración de cobertura

### Cypress (cypress.config.ts)
- Configuración para pruebas E2E
- Integración con Next.js
- Configuración de viewport y video

### Storybook (.storybook/main.ts)
- Configuración para documentación de componentes
- Addons para accesibilidad y pruebas
- Integración con Next.js y TypeScript

## 🤝 Contribución

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 👥 Equipo

- Desarrolladores Frontend
- Diseñadores UI/UX
- Ingenieros Blockchain
- QA Engineers

## 📞 Soporte

Para soporte, email support@woldvirtual.com o únete a nuestro servidor de Discord. 