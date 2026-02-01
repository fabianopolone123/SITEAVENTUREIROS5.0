import Image from 'next/image';

export default function HomePage() {
  return (
    <main className="login-screen">
      <div className="card-content">
        <div className="logo-badge">
          <Image src="/logo.png" alt="Logo Clube de Aventureiros" width={110} height={110} />
        </div>
        <p className="tagline">Espaço do Clube</p>
        <h1 className="club-title">Clube de Aventureiros Pinhal Junior</h1>

        <div className="form-group">
          <label htmlFor="username">Nome de usuário</label>
          <input id="username" name="username" type="text" placeholder="Digite o seu nome" />
        </div>

        <div className="form-group">
          <label htmlFor="password">Senha secreta</label>
          <input id="password" name="password" type="password" placeholder="Digite sua senha" />
        </div>

        <button className="primary-action" type="button">
          Entrar
        </button>

        <div className="footer-links">
          <span>novo por aqui?</span>
          <a className="secondary-pill" href="#">Cadastre-se</a>
          <a className="muted-link" href="#">Esqueci meu usuário ou senha</a>
        </div>
      </div>
    </main>
  );
}
