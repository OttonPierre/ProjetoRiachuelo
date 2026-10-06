import icon from './icone.png';

function App() {
  return (
    <div className="app-container">
      <header className="navbar">
        <div className="logo">
          <img src={icon} alt="Projeto Riachuelo Logo" className="logo-img" />
          Projeto Riachuelo
        </div>
        <nav className="nav-links">
          <a href="#">Início</a>
          <a href="#">Adotar</a>
          <a href="#">Desaparecidos</a>
          <a href="#">Contato</a>
        </nav>
        <button className="btn-primary">Entrar</button>
      </header>

      <main>
        <section className="hero">
          <div className="hero-content">
            <h1>Todo animal merece um <span>lar amoroso.</span></h1>
            <p>
              Junte-se à nossa comunidade para adotar um novo melhor amigo ou ajudar a reunir animais perdidos com suas famílias.
            </p>
            <div className="hero-actions">
              <button className="btn-primary">Encontrar um Pet</button>
              <button className="btn-secondary">Cadastrar Pet Desaparecido</button>
            </div>
          </div>
        </section>

        <section className="features">
          <div className="feature-card">
            <h3>Adotar</h3>
            <p>Navegue pela nossa lista de animais adoráveis à espera de uma segunda chance. Encontre seu par perfeito hoje.</p>
          </div>
          <div className="feature-card">
            <h3>Reencontrar</h3>
            <p>Cadastre animais desaparecidos para alertar a comunidade e trazê-los para casa em segurança.</p>
          </div>
          <div className="feature-card">
            <h3>Voluntariado</h3>
            <p>Faça parte da nossa equipe de resgate e faça uma diferença real na vida dos animais.</p>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
