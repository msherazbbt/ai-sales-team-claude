/**
 * Brand Configuration — Labstar Diagnostic Lab
 */

import type { Theme } from '../../../../lib/theme';

export const brandName = 'labstar';

export const brand = {
  name: 'Labstar',
  colors: {
    primary: '#0077CC',
    primaryLight: '#29A8FF',
    accent: '#00C9A7',
    textDark: '#ffffff',
    textMedium: '#a0bcd0',
    textLight: '#5a7a8a',
    bgLight: '#071828',
    bgDark: '#030d18',
    bgOverlay: 'rgba(0, 119, 204, 0.08)',
    divider: '#0e2d45',
    shadow: 'rgba(0, 0, 0, 0.6)',
  },
  fonts: {
    primary: 'Inter, system-ui, -apple-system, sans-serif',
    mono: 'JetBrains Mono, ui-monospace, SFMono-Regular, monospace',
  },
  spacing: {
    xs: 8,
    sm: 16,
    md: 24,
    lg: 48,
    xl: 80,
    xxl: 120,
  },
  borderRadius: {
    sm: 8,
    md: 16,
    lg: 24,
  },
  typography: {
    h1: { size: 80, weight: 800 },
    h2: { size: 60, weight: 700 },
    h3: { size: 42, weight: 600 },
    body: { size: 26, weight: 400 },
    label: { size: 18, weight: 600, letterSpacing: 2 },
  },
  assets: {
    logo: undefined as string | undefined,
    logoLight: undefined as string | undefined,
  },
};

export const brandTheme: Theme = {
  colors: brand.colors,
  fonts: brand.fonts,
  spacing: brand.spacing,
  borderRadius: brand.borderRadius,
  typography: brand.typography,
};
