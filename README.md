# Revisão Quality Assurance - UniFECAF

## Conceitos de QA

A qualidade em software refere-se ao conjunto de características que tornam um produto de software adequado ao seu propósito, atendendo às necessidades dos usuários e stakeholders. Já a cultura de qualidade é um ambiente organizacional em que todos os colaboradores priorizam a excelência, buscando prevenir defeitos e melhorar continuamente os processos.

- A qualidade de software pode ser avaliada com base em critérios como:

- Funcionalidade: O software atende aos requisitos especificados?

- Confiabilidade: O sistema opera sem falhas em diferentes condições?

- Usabilidade: É fácil de usar e intuitivo?

- Eficiência: Tem bom desempenho e consumo de recursos?

- Manutenibilidade: Pode ser facilmente modificado e atualizado?

- Portabilidade: Pode ser executado em diferentes ambientes?

## Tipos de teste

### 1. Teste Unitário
O que testa? Componentes individuais (funções, classes, métodos).

Objetivo: Verificar lógica interna e comportamentos isolados.

Ferramentas: JUnit (Java), pytest (Python), Jest (JavaScript).

[Exemplo de código](./tipos-de-teste/tests/teste-unitario.py)

### 2. Teste de Integração
O que testa? Interação entre módulos/serviços (ex.: API + banco de dados).

Objetivo: Garantir que partes do sistema funcionem juntas corretamente.

Exemplo: Testar comunicação entre um microsserviço e um banco de dados.

[Exemplo de código](./tipos-de-teste/tests/teste-de-integracao.py)

### 3. Teste de Sistema
O que testa? O sistema completo, em um ambiente próximo ao real.

Objetivo: Validar se o software atende aos requisitos funcionais e não funcionais.

Abrange: Performance, segurança, usabilidade.

[Exemplo de código](./tipos-de-teste/tests/teste-de-sistema.py)

### 4. Teste de Aceitação
O que testa? Fluxos de negócio, conforme expectativa do usuário/cliente.

Objetivo: Confirmar se o sistema está pronto para entrega.

Quem executa? Cliente ou Product Owner (PO), em ambiente simulado.

[Exemplo de código](./tipos-de-teste/tests/teste-de-aceitacao.py)

### 5. Teste de Regressão
O que testa? Funcionalidades existentes após novas alterações.

Objetivo: Evitar que mudanças quebrem features já validadas.

Quando? Após correções, atualizações ou releases.

[Exemplo de código](./tipos-de-teste/tests/teste-de-regressao.py)

### 6. Teste Exploratório
O que testa? Comportamentos não previstos, sem roteiro fixo.

Objetivo: Descobrir bugs através da experiência e criatividade do tester.

Diferencial: Focado em investigação livre, sem scripts pré-definidos.

**Exemplo de teste exploratório com o site da Amazon**

![Captura de tela 2025-05-22 094644](https://github.com/user-attachments/assets/11e203dd-f484-41f3-8744-db573308b25c)

## Critérios de Aceitação em Metodologias Ágeis (User Stories e BDD)
Os critérios de aceitação (AC) são condições que uma User Story deve satisfazer para ser considerada "pronta" (Done). Eles definem o limite de funcionalidade e ajudam a alinhar expectativas entre desenvolvedores, QA e stakeholders.

 Formato em User Stories (Exemplo)

**User Story:**
 “Como cliente, quero adicionar produtos ao meu carrinho e salvá-los para comprar mais tarde”


**Critérios de Aceitação:**
- O usuário deve poder adicionar e excluir um ou mais itens no carrinho.
- O sistema deve exibir uma confirmação visual de que o produto foi adicionado ao carrinho.
- O usuário deve ter a opção de mover o produto para a lista de “Salvar para mais tarde”
- Os itens salvos em “Salvo para mais tarde” devem ser acessíveis na mesma página do carrinho.

## Automação de testes
A automação de testes é essencial para garantir qualidade, velocidade e confiabilidade no desenvolvimento de software. Abaixo, uma visão geral das principais ferramentas e suas aplicações:

### Ferramentas de Automação por Camada
**Front-end (Web e Mobile)**
- Selenium WebDriver

  - Linguagens: Java, Python, C#, JavaScript.

  - Vantagens: Multi-navegador, ampla comunidade.
 
  - [Exemplo de código](./automacao-de-testes/selenium.py)


 - Fake Filler

![Captura de tela 2025-04-25 084300](https://github.com/user-attachments/assets/d015b9ba-a9a4-4c94-93e7-b0cac6abc4e1)

- Ghost Inspector

![Captura de tela 2025-04-25 085646](https://github.com/user-attachments/assets/1b1fedc0-ce9e-4c2f-8717-2458be191dbb)

- WAVE

![Captura de tela 2025-04-25 090805](https://github.com/user-attachments/assets/db4eeae2-2c56-4a29-98e3-9ec1fccfbb84)


**Back-end e APIs**
- Postman (Automation + Newman)

  - Vantagens: Interface gráfica, testes via coleções, integração com CI/CD.

- RestAssured (Java)

  - Vantagens: Sintaxe fluente, ideal para testes de API em Java.

- Supertest (Node.js)

  - Vantagens: Simplicidade para testes de APIs em JavaScript.

**Testes de Desempenho e Carga**
- JMeter

  - O que faz? Simula usuários virtuais para testar performance.

  - Vantagens: Open-source, suporta HTTP, SOAP, bancos de dados.
 
## Controle e Monitoramento da Qualidade de Software
A garantia da qualidade (QA) não termina após os testes – ela exige monitoramento contínuo, auditorias e gestão eficiente de problemas. Abaixo, um guia estruturado sobre práticas e ferramentas para manter a qualidade sob controle.

### 1. Auditorias de Qualidade de Software
Auditorias avaliam processos, código e conformidade com padrões para identificar riscos e melhorias.

**Tipos de Auditoria**

- Código: Verificação de boas práticas (ex.: SonarQube).

- Processos: Alinhamento com metodologias (ex.: CMMI, ISO 9001).

- Segurança: Vulnerabilidades (ex.: OWASP ZAP, Nessus).

### 2. Monitoramento Contínuo

**Análise Estática de Código**

O que é? Verificação do código sem executá-lo.

**Ferramentas:**

- SonarQube (bugs, code smells, cobertura).

- ESLint (JavaScript), Pylint (Python).

**Métricas em Tempo Real**

- Cobertura de Testes (ex.: JaCoCo, Istanbul).

- Dívida Técnica (SonarQube).

- Tempo de Resposta (New Relic, Datadog).

### 3. Gestão de Bugs e Problemas

**Priorização**

Critérios: Severidade (Crítico, Alto, Médio, Baixo) + Impacto no negócio.

**Modelos:**

- MoSCoW (Must have, Should have, Could have, Won’t have).

- Matriz GUT (Gravidade, Urgência, Tendência).

**Rastreamento e Resolução**

**Ferramentas:**

- Jira (+ plugins como Xray para testes).

- Bugzilla, Azure DevOps.

### 4. Observabilidade (Observability)
Vai além do monitoramento, permitindo investigar problemas complexos através de:

**Os 3 Pilares da Observabilidade**

1. Logs (registros de eventos) → ELK Stack (Elasticsearch, Logstash, Kibana).

2. Métricas (dados quantitativos) → Prometheus + Grafana.

3. Tracing (rastreamento de fluxos) → Jaeger, Zipkin.

**Ferramentas Modernas**

- Datadog (unifica logs, métricas e traces).

- New Relic (APM + monitoramento de desempenho).

- Sentry (erros em tempo real).

### 5. Monitoramento Proativo
**Práticas Recomendadas**

- Alertas Inteligentes (ex.: Slack/Teams integrado ao Prometheus).

- Synthetic Monitoring (simula usuários reais) → Selenium Grid, Cypress Cloud.

- Chaos Engineering (teste de resiliência) → Gremlin, Chaos Monkey.
