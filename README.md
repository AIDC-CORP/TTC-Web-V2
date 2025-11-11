

# Tân Thành Công JSC - Corporate Website

[![React](https://img.shields.io/badge/React-19.2.0-blue.svg)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8.2-blue.svg)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-6.2.0-646CFF.svg)](https://vitejs.dev/)
[![Jest](https://img.shields.io/badge/Jest-30.2.0-C21325.svg)](https://jestjs.io/)
[![Testing Library](https://img.shields.io/badge/Testing_Library-16.3.0-E33332.svg)](https://testing-library.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC.svg)](https://tailwindcss.com/)
[![Yarn](https://img.shields.io/badge/Yarn-1.22+-blue.svg)](https://yarnpkg.com/)

A modern, responsive corporate website for Tân Thành Công JSC, showcasing construction projects, consulting services, and company information. Built with React, TypeScript, and Tailwind CSS.

## 🌟 Features

### 🏢 **Company Showcase**
- **Hero Section** - Compelling introduction with call-to-action
- **About Page** - Company history, mission, and values
- **Services** - Comprehensive service offerings (Design Consulting, Project Management, Construction Supervision, Project Appraisal)


### 📱 **Modern UI/UX**
- **Responsive Design** - Mobile-first approach, works on all devices
- **Vietnamese Language** - Localized content and navigation
- **SEO-Friendly URLs** - Vietnamese path segments for better SEO
- **Smooth Animations** - CSS transitions and hover effects
- **Accessibility** - Semantic HTML and keyboard navigation support

### 🔧 **Technical Features**
- **TypeScript** - Type-safe development
- **React Router** - Client-side routing with HashRouter
- **Component Architecture** - Feature-based folder structure
- **Mock Data System** - Static data for development and demo purposes
- **Testing Suite** - Jest and React Testing Library for component testing

## 🚀 Quick Start

### Prerequisites
- **Node.js** (v16 or higher)
- **Yarn** package manager

### Installing Yarn

If you don't have Yarn installed, choose the installation method that matches your operating system:

## 🍎 **macOS**

### Method 1: Using Homebrew (Recommended)
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Yarn
brew install yarn
```

### Method 2: Using npm
```bash
# Install Yarn globally via npm
npm install -g yarn
```

### Method 3: Using Corepack (Node.js 16.10+)
```bash
# Enable Corepack
corepack enable

# Prepare Yarn
corepack prepare yarn@stable --activate
```

## 🪟 **Windows**

### Method 1: Using Chocolatey (Recommended)
```powershell
# Install Chocolatey if you don't have it
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install Yarn
choco install yarn
```

### Method 2: Using npm
```bash
# Install Yarn globally via npm
npm install -g yarn
```

### Method 3: Using Corepack (Node.js 16.10+)
```bash
# Enable Corepack
corepack enable

# Prepare Yarn
corepack prepare yarn@stable --activate
```

### Method 4: Using Scoop
```powershell
# Install Scoop if you don't have it
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')

# Install Yarn
scoop install yarn
```

## 🐧 **Linux**

### Method 1: Using npm (Universal)
```bash
# Install Yarn globally via npm
npm install -g yarn
```

### Method 2: Using Corepack (Node.js 16.10+)
```bash
# Enable Corepack
corepack enable

# Prepare Yarn
corepack prepare yarn@stable --activate
```

### Method 3: Using Package Manager

#### Ubuntu/Debian
```bash
# Update package list
sudo apt update

# Install Yarn
sudo apt install yarn
```

#### CentOS/RHEL/Fedora
```bash
# For CentOS/RHEL
sudo yum install yarn

# For Fedora
sudo dnf install yarn
```

#### Arch Linux
```bash
# Install Yarn
sudo pacman -S yarn
```

### Method 4: Using Installation Script
```bash
# Download and install Yarn
curl -o- -L https://yarnpkg.com/install.sh | bash

# Add Yarn to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.yarn/bin:$PATH"
```

## ✅ **Verify Installation**

After installation, verify that Yarn is working correctly:

```bash
# Check Yarn version
yarn --version

# You should see output like: 1.22.x
```

## 🔧 **Troubleshooting**

### Permission Issues (macOS/Linux)
If you encounter permission errors, try:
```bash
# Install without sudo (if using npm)
npm install -g yarn --prefix ~/.npm-global

# Or use a Node version manager like nvm
```

### PATH Issues
If Yarn commands are not found, ensure Yarn is in your PATH:
```bash
# Check where Yarn is installed
which yarn

# Add to PATH if needed (add to ~/.bashrc, ~/.zshrc, or ~/.profile)
export PATH="$(yarn global bin):$PATH"
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AIDC-CORP/TTC-Web-V2.git
   cd TTC-Web-V2
   ```

2. **Install dependencies**
   ```bash
   yarn install
   ```



4. **Start development server**
   ```bash
   yarn dev
   ```

5. **Open your browser**
   - Navigate to `http://localhost:3000`
   - The app will automatically reload when you make changes

## 📜 Available Scripts

| Command | Description |
|---------|-------------|
| `yarn dev` | Start development server on port 3000 |
| `yarn build` | Build the app for production |
| `yarn preview` | Preview the production build locally |
| `yarn test` | Run Jest tests once |
| `yarn test:watch` | Run Jest tests in watch mode |
| `yarn test:coverage` | Run Jest tests with coverage report |

## 🏛️ Project Structure

```
TTC-Web-V2/
├── public/                 # Static assets
├── src/
│   ├── features/          # Feature-based modules
│   │   ├── home/         # Homepage feature
│   │   ├── about/        # About page feature
│   │   ├── projects/     # Projects showcase
│   │   ├── consulting/   # Consulting services
│   │   ├── blog/         # Blog/articles system
│   │   ├── contact/      # Contact page
│   │   ├── search/       # Search functionality
│   │   └── common/       # Shared components
│   ├── data/             # Mock data and content
│   ├── types.ts          # TypeScript interfaces
│   ├── App.tsx           # Main application component
│   └── index.tsx         # Application entry point
├── __tests__/             # Jest test files
├── package.json           # Dependencies and scripts
├── vite.config.ts         # Vite configuration
├── tsconfig.json          # TypeScript configuration
├── jest.config.ts         # Jest configuration
├── jest.setup.ts          # Jest setup file
└── README.md             # This file
```

## 🛠️ Technology Stack

### Frontend Framework
- **React 19.2.0** - Modern React with concurrent features
- **TypeScript 5.8.2** - Type-safe JavaScript development
- **React Router DOM 7.9.5** - Declarative routing for React

### Build & Development Tools
- **Vite 6.2.0** - Fast build tool and development server
- **@vitejs/plugin-react** - React plugin for Vite
- **@types/node** - Node.js type definitions

### Testing Framework
- **Jest 30.2.0** - JavaScript testing framework
- **React Testing Library 16.3.0** - Testing utilities for React components
- **@testing-library/jest-dom 6.9.1** - Custom Jest matchers for DOM testing
- **@testing-library/user-event 14.6.1** - User interaction testing utilities
- **ts-jest 29.4.5** - TypeScript preprocessor for Jest

### Styling & UI
- **Tailwind CSS** - Utility-first CSS framework
- **Responsive Design** - Mobile-first approach
- **Custom Animations** - CSS transitions and transforms

## 🧪 Testing

This project includes a comprehensive testing setup using Jest and React Testing Library to ensure code quality and prevent regressions.

### Running Tests

```bash
# Run tests once
yarn test

# Run tests in watch mode (recommended during development)
yarn test:watch

# Run tests with coverage report
yarn test:coverage
```

### Test Structure

Tests are organized in the `__tests__/` directory at the root level:

```
__tests__/
├── ServiceCard.test.tsx    # Tests for ServiceCard component
├── ProjectCard.test.tsx    # Tests for ProjectCard component
└── ...                     # Additional test files
```

### Test Configuration

- **jest.config.ts** - Main Jest configuration with TypeScript support
- **jest.setup.ts** - Global test setup (imports jest-dom matchers)
- **tsconfig.json** - Updated to include Jest types

### Writing Tests

Tests use React Testing Library for component testing:

```typescript
import React from 'react';
import { render, screen } from '@testing-library/react';
import MyComponent from './MyComponent';

describe('MyComponent', () => {
  it('should render correctly', () => {
    render(<MyComponent />);
    expect(screen.getByText('Expected Text')).toBeInTheDocument();
  });
});
```

## 📊 Data Models

### Project
```typescript
interface Project {
  id: string;
  name: string;
  image: string;
  summary: string;
  description: string;
  investor?: string;
  executionTime?: string;
  gallery: string[];
  category: string;
}
```

### Article
```typescript
interface Article {
  id: string;
  title: string;
  image: string;
  excerpt: string;
  content: string;
  publishDate: string;
  category: 'Blog' | 'Tư vấn';
}
```

### Service
```typescript
interface Service {
  id: string;
  name: string;
  image: string;
  summary: string;
}
```

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is proprietary software owned by Tân Thành Công JSC.

## 📞 Contact

**Tân Thành Công JSC**
- Website: [www.tanthanhcong.com](https://www.tanthanhcong.com)
- Email: info@tanthanhcong.com
- Phone: +84 xxx xxx xxxx

---

<div align="center">
Built with ❤️ by AIDC-CORP Team
</div>
