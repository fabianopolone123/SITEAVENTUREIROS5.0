import type { ReactNode } from 'react';
import './globals.css';

export const metadata = {
  title: 'Espaço do Clube - Login',
  description: 'Login do Clube de Aventureiros Pinhal Junior'
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
