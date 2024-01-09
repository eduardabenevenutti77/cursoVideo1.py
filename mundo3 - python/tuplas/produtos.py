#tenha uma tupla com os nomes de produtos e seus repectivos preços na sequência.
#no final, mostre uma listagem de preços, organizando em forma tabular

produtos = (
  ('Azeite', 15.99),
  ('Limão', 6.50),
  ('Sabão em pó', 8.50),
  ('Sal', 10.00),
  ('Uva', 5.99),
  ('Ovo', 10.00),
  ("Carne moída", 25.50),
  ("Batata", 10.99),
  ("Chocolate", 5.75),
  ("Bolo", 15.30),
  ("Amaciante", 8.50)
)

print("{:<15} {:<10}".format("Produto", "Preço"))
for produto, preco in produtos:
    print("{:<15} R${:<10.2f}".format(produto, preco))
