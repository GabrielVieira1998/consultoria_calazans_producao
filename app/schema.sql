DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS testimonials;
DROP TABLE IF EXISTS contacts;

CREATE TABLE courses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  image TEXT NOT NULL,
  link TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE testimonials (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  text TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL,
  issue TEXT NOT NULL,
  message TEXT NOT NULL,
  source TEXT,
  utm_source TEXT,
  utm_medium TEXT,
  utm_campaign TEXT,
  utm_term TEXT,
  utm_content TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Dados iniciais para cursos
INSERT INTO courses (title, description, image, link)
VALUES 
  ('Recuperação Lombar para Mães', 'Programa completo para mães com dor lombar pós-parto, foco em recuperação segura e progressiva.', 'https://images.unsplash.com/photo-1518495973542-4542c06a5843', 'https://opersonaldigital.com/curso-exemplo-1'),
  ('Treinamento para Mulheres com Hérnia de Disco', 'Treinos especializados para mulheres com hérnia de disco, focando na estabilização e fortalecimento seguro.', 'https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07', 'https://opersonaldigital.com/curso-exemplo-2'),
  ('Retorno Seguro ao Exercício', 'Para mulheres que desejam retornar à atividade física após lesões ou longo período de inatividade.', 'https://images.unsplash.com/photo-1506744038136-46273834b3fb', 'https://opersonaldigital.com/curso-exemplo-3');

-- Dados iniciais para depoimentos
INSERT INTO testimonials (name, text)
VALUES 
  ('Maria Silva', 'Depois de dois anos sofrendo com dor lombar, finalmente encontrei um treinamento que me ajudou a voltar a ter qualidade de vida. Muito obrigada!'),
  ('Juliana Mendes', 'A metodologia da Consultoria Calazans é incrível! Consegui recuperar meu corpo após a gravidez de uma forma segura e eficiente.'),
  ('Fernanda Oliveira', 'Tinha desistido de me exercitar por causa da minha hérnia de disco, mas os treinos personalizados mudaram minha vida. Recomendo demais!'); 