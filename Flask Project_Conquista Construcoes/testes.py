import secrets
import urllib
import urllib.parse

# print(secrets.token_hex(16))
# print("**TESTE** TESTE")

# print(urllib.parse.quote("asdasdÇ"))
lista_servicos=[("Elétrica", "Instalações e reparos elétricos com segurança e eficiência.", "fas fa-bolt fa-3x"), 
                    ("Hidráulica", "Soluções completas para sua rede de água e esgoto.", "fas fa-water fa-3x"), 
                    ("Gesso", "Trabalhos em gesso com acabamentos perfeitos.", "fas fa-hard-hat fa-3x"), 
                    ("Pintura", "Pintura residencial e comercial com acabamento profissional.", "fas fa-paint-roller fa-3x"), 
                    ("Azulejo", "Colocação e reparo de azulejos para cozinhas, banheiros e mais.", "fas fa-th fa-3x"), 
                    ("Cerâmica", "Revestimentos cerâmicos com precisão e qualidade.", "fas fa-th-large fa-3x"), 
                    ("Porcelanato", "Instalação de porcelanato com acabamentos sofisticados.", "fas fa-th fa-3x"), 
                    ("Tubulação de Gás", "Execução e reparos em tubulações de gás com segurança garantida.", "fas fa-gas-pump fa-3x"), 
                    ("Vidro Temperado", "Fornecimento e instalação de vidros temperados de alta resistência.", "fas fa-window-maximize fa-3x"),
                    ("Emissão de Laudo Técnico", "Fornecemos laudos técnicos detalhados, com garantia de precisão e confiabilidade, para assegurar a conformidade de suas obras com as normas vigentes.", "fas fa-file-alt fa-3x"),
                    ("Emissão de Laudo Técnico", "Fornecemos laudos técnicos detalhados, com garantia de precisão e confiabilidade, para assegurar a conformidade de suas obras com as normas vigentes.", "fas fa-file-alt fa-3x"),
                    ]
print(len(lista_servicos)%3)