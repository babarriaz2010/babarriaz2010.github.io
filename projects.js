(() => {
  const projects = [
    {
      title: 'Insurance RAG Assistant', category: 'APPLIED AI / DOCUMENT INTELLIGENCE',
      description: 'Making insurance information accessible through retrieval-augmented conversations.',
      workflow: [['SOURCE','Insurance documents','Domain knowledge'],['RETRIEVE','Relevant context','Document retrieval'],['RESPOND','AI assistant','Contextual answers']],
      flowLabel: 'KNOWLEDGE → CONTEXT → ANSWER',
      overview: [['The challenge','Help users navigate insurance information through natural-language questions.'],['The approach','Combine document retrieval with conversational responses to surface relevant insurance knowledge.']],
      engineering: [['Retrieval layer','Retrieve insurance information relevant to the user’s question as context for the assistant.'],['Conversation layer','Use the retrieved context to support domain-focused conversational responses.']],
      stack: ['Retrieval-augmented generation','Document retrieval','Conversational AI'],
      stackNote: 'Core techniques used in this project.'
    },
    {
      title: 'Enterprise CRM Platform', category: 'ENTERPRISE SOFTWARE / BUSINESS OPERATIONS',
      description: 'More than six years of engineering across customer management, sales, purchasing, and inventory.',
      workflow: [['OPERATE','Sales & inventory','Business workflows'],['CONNECT','APIs & services','Third-party integrations'],['MANAGE','Customer data','PostgreSQL & reporting']],
      flowLabel: 'OPERATIONS ↔ SERVICES ↔ DATA',
      overview: [['The challenge','Support connected business operations across customer management, sales, purchasing, inventory, and reporting.'],['My contribution','Worked across backend and frontend development, database design, API integrations, performance optimization, and production support.']],
      engineering: [['Application & integrations','Developed business workflows and REST API integrations linking the platform with external services.'],['Data & performance','Worked on PostgreSQL queries, indexing, and reducing unnecessary database calls as reporting and data-heavy workflows grew.']],
      stack: ['PHP','JavaScript','PostgreSQL','REST APIs'],
      stackNote: 'The application and integration stack behind the enterprise platform.'
    },
    {
      title: 'AI Workflow Automation', category: 'AGENTIC SYSTEMS / LOUCOM',
      description: 'Connecting agent reasoning with external tools, APIs, and real business workflows.',
      workflow: [['ORCHESTRATE','Agent workflows','LangGraph & CrewAI'],['EXECUTE','Tool calling','APIs & databases'],['SERVE','Async services','Python & FastAPI']],
      flowLabel: 'REASON → USE TOOLS → ACT',
      overview: [['The challenge','Automate complex business processes that need both LLM reasoning and interactions with external systems.'],['My contribution','Built Generative AI applications and multi-agent workflows at Loucom, with custom function-calling architectures and backend services.']],
      engineering: [['Agent orchestration','Used LangChain, LangGraph, and CrewAI to coordinate multi-agent workflows and connect agents with external APIs and databases.'],['Backend execution','Built asynchronous Python and FastAPI services to support LLM responses and streaming agent execution loops.']],
      stack: ['Python','FastAPI','LangChain','LangGraph','CrewAI','Function calling'],
      stackNote: 'Orchestration frameworks and backend tools used across these workflows.'
    },
    {
      title: 'Component Data Intelligence', category: 'DATA ENGINEERING / CHIP ONE EXCHANGE',
      description: 'Turning unstructured electronics data into usable specifications and market-pricing insights.',
      workflow: [['COLLECT','Web sources','Component data'],['TRANSFORM','Clean & normalize','Specification extraction'],['ANALYZE','Pricing insights','Market analysis']],
      flowLabel: 'COLLECT → STRUCTURE → ANALYZE',
      overview: [['The challenge','Extract useful chip specifications and pricing information from diverse, unstructured web sources.'],['My contribution','Engineered automated extraction, cleansing, normalization, and transformation pipelines, alongside pricing and market-analysis engines.']],
      engineering: [['Data pipelines','Processed multi-source web data into normalized component specifications for downstream search and analysis.'],['Pricing intelligence','Built analytics and automated algorithms to help determine competitive minimum market pricing for electronic components.']],
      stack: ['Python','Automated extraction','Data normalization','Pricing analytics'],
      stackNote: 'Core engineering techniques and language used for the data pipeline.'
    }
  ];
  const selectors = [...document.querySelectorAll('.project-select')];
  const tabs = [...document.querySelectorAll('.case-tabs [role="tab"]')];
  const study = document.querySelector('#case-study');
  const panel = document.querySelector('#case-panel');
  const status = document.querySelector('#filter-status');
  let selected = 0;
  let view = 'overview';
  const visibleProjects = () => selectors.filter(button => !button.hidden);
  const element = (tag, text, className) => {
    const node = document.createElement(tag);
    node.textContent = text;
    if (className) node.className = className;
    return node;
  };
  function renderPanel() {
    const project = projects[selected];
    tabs.forEach(tab => {
      const active = tab.dataset.view === view;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
    });
    panel.setAttribute('aria-labelledby', `tab-${view}`);
    panel.replaceChildren();
    if (view === 'stack') {
      const chips = document.createElement('div');
      chips.className = 'case-stack';
      chips.append(...project.stack.map(skill => element('span', skill)));
      panel.append(chips, element('p', project.stackNote, 'stack-context'));
    } else {
      project[view].forEach(([heading, body]) => {
        const detail = document.createElement('div');
        detail.className = 'case-detail';
        detail.append(element('h4', heading), element('p', body));
        panel.append(detail);
      });
    }
  }
  function renderProject(index, announce = true) {
    selected = index;
    const project = projects[index];
    selectors.forEach(button => button.setAttribute('aria-pressed', String(Number(button.dataset.project) === index)));
    document.querySelector('#case-title').textContent = project.title;
    document.querySelector('#case-category').textContent = project.category;
    document.querySelector('#case-description').textContent = project.description;
    document.querySelector('#case-counter').textContent = `${String(index + 1).padStart(2,'0')} / 04`;
    document.querySelector('#blueprint-label').textContent = project.flowLabel;
    const blueprint = document.querySelector('#case-blueprint');
    blueprint.replaceChildren();
    project.workflow.forEach(([stage,title,detail], i) => {
      if (i) { const arrow = element('span','→','blueprint-arrow'); arrow.setAttribute('aria-hidden','true'); blueprint.append(arrow); }
      const node = document.createElement('div');
      node.className = 'blueprint-node';
      node.append(element('small',`0${i + 1} / ${stage}`),element('strong',title),element('span',detail));
      blueprint.append(node);
    });
    const single = visibleProjects().length < 2;
    document.querySelectorAll('.case-pagination button').forEach(button => button.disabled = single);
    renderPanel();
    study.classList.remove('changing');
    void study.offsetWidth;
    study.classList.add('changing');
    if (announce) status.textContent = `${project.title} selected. ${view === 'stack' ? 'Tech stack' : view} details displayed.`;
  }
  selectors.forEach(button => button.addEventListener('click', () => renderProject(Number(button.dataset.project))));
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => { view = tab.dataset.view; renderPanel(); });
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) { event.preventDefault(); tabs[next].focus(); tabs[next].click(); }
    });
  });
  document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => {
    document.querySelectorAll('.filter').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    selectors.forEach(item => item.hidden = button.dataset.filter !== 'all' && item.dataset.category !== button.dataset.filter);
    if (selectors[selected].hidden) selected = Number(visibleProjects()[0].dataset.project);
    renderProject(selected, false);
    status.textContent = `${visibleProjects().length} projects available. ${projects[selected].title} selected.`;
  }));
  function navigate(direction) {
    const list = visibleProjects();
    const position = list.findIndex(button => Number(button.dataset.project) === selected);
    renderProject(Number(list[(position + direction + list.length) % list.length].dataset.project));
  }
  document.querySelector('#previous-project').addEventListener('click', () => navigate(-1));
  document.querySelector('#next-project').addEventListener('click', () => navigate(1));
  renderProject(0, false);
})();
