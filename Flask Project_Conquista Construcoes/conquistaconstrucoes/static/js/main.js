document.addEventListener('DOMContentLoaded', function () {
    var navbarToggler = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.querySelector('#navbarSupportedContent');
  
    navbarToggler.addEventListener('click', function () {
      var isExpanded = navbarToggler.getAttribute('aria-expanded') === 'true';
      navbarToggler.setAttribute('aria-expanded', !isExpanded);
      if (isExpanded) {
        navbarCollapse.style.height = navbarCollapse.scrollHeight + 'px';
        setTimeout(function () {
          navbarCollapse.style.height = '0';
        }, 10);
      } else {
        navbarCollapse.style.height = '0';
        setTimeout(function () {
          navbarCollapse.style.height = navbarCollapse.scrollHeight + 'px';
        }, 10);
      }
      navbarCollapse.classList.toggle('show');
    });
  
    // Fechar o menu ao clicar fora dele
    document.addEventListener('click', function (event) {
      var isClickInside = navbarToggler.contains(event.target) || navbarCollapse.contains(event.target);
      if (!isClickInside && navbarCollapse.classList.contains('show')) {
        navbarCollapse.style.height = navbarCollapse.scrollHeight + 'px';
        setTimeout(function () {
          navbarCollapse.style.height = '0';
        }, 10);
        navbarCollapse.classList.remove('show');
        navbarToggler.setAttribute('aria-expanded', 'false');
      }
    });
  });

  
  document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('#navbar .nav-link');
    const currentUrl = window.location.href;
  
    // Verifica se a URL atual corresponde a algum dos links de navegação
    navLinks.forEach(link => {
      if (link.href === currentUrl) {
        link.classList.add('fw-bold');
      } else {
        link.classList.remove('fw-bold');
      }
    });
  
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        // Remove a classe 'fw-bold' de todos os links
        navLinks.forEach(nav => nav.classList.remove('fw-bold'));
        
        // Adiciona a classe 'fw-bold' ao link clicado
        this.classList.add('fw-bold');
  
        // Armazena o link ativo no localStorage
        localStorage.setItem('activeLink', this.href);
      });
    });
  });
  
  