import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pyodbc

# Função para conectar ao banco de dados SQL Server
def conectar_banco():
    try:
        conexao = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=DESKTOP-6DBKSFC;'  # Nome do servidor
            'DATABASE=lojatech;'       # Nome do banco de dados
            'UID=sa;'                  # Nome de usuário
            'PWD=herik1996'            # Senha
        )
        return conexao
    except Exception as e:
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao banco de dados: {e}")
        return None

# Função para cadastrar cliente no banco de dados
def cadastrar_cliente(nome, cpf, endereco, email, telefone, data_cadastro):
    conexao = conectar_banco()
    if conexao:
        with conexao.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Clientes (Nome, CPFCNPJ, Endereco, Email, Telefone, DataCadastro) VALUES (?, ?, ?, ?, ?, ?)",
                               (nome, cpf, endereco, email, telefone, data_cadastro))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o cliente: {e}")
            finally:
                conexao.close()
# Função para cadastrar funcionário no banco de dados
def cadastrar_funcionario(nome, cpf, endereco, cargo, salario, data_admissao):
    conexao = conectar_banco()
    if conexao:
        with conexao.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Funcionarios (Nome, CPF, Endereco, Cargo, Salario, DataAdmissao) VALUES (?, ?, ?, ?, ?, ?)",
                               (nome, cpf, endereco, cargo, salario, data_admissao))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o funcionário: {e}")
            finally:
                conexao.close()
# Função para cadastrar produto no banco de dados
def cadastrar_produto(nome, numero_serie, preco, quantidade_estoque, categoria):
    conexao = conectar_banco()
    if conexao:
        with conexao.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Produtos (NomeProduto, Descricao, NumeroSerie, Preco, QuantidadeEstoque, Categoria) VALUES (?, ?, ?, ?, ?, ?)",
                               (nome, "Descrição", numero_serie, preco, quantidade_estoque, categoria))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o produto: {e}")
            finally:
                conexao.close()
# Função para registrar venda no banco de dados
def registrar_venda(cliente_id, funcionario_id, total_venda, data_venda):
    conexao = conectar_banco()
    if conexao:
        with conexao.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Vendas (ClienteID, FuncionarioID, TotalVenda, DataVenda) VALUES (?, ?, ?, ?)",
                               (cliente_id, funcionario_id, total_venda, data_venda))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao registrar a venda: {e}")
            finally:
                conexao.close()

def cadastrar_item_venda(venda_id, produto_id, quantidade, preco):
    conexao = conectar_banco()
    if conexao:
        with conexao.cursor() as cursor:
            try:
                cursor.execute("""
                INSERT INTO ItensVenda (VendaID, ProdutoID, Quantidade, PrecoUnitario)
                VALUES (?, ?, ?, ?)""",
                (venda_id, produto_id, quantidade, preco))
                conexao.commit()
                messagebox.showinfo("Sucesso", "Item de venda cadastrado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o item da venda: {e}")
            finally:
                conexao.close()

# Interface gráfica para o cadastro de clientes
def interface_cadastro_clientes():
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Clientes")
    janela_cadastro.geometry("400x300")  # Ajusta o tamanho da janela

    ttk.Label(janela_cadastro, text="Nome:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
    entry_nome = ttk.Entry(janela_cadastro)
    entry_nome.grid(row=0, column=1, sticky='e', padx=10, pady=10)

    ttk.Label(janela_cadastro, text="CPF/CNPJ:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
    entry_cpf = ttk.Entry(janela_cadastro)
    entry_cpf.grid(row=1, column=1, sticky='e', padx=10, pady=10)

    ttk.Label(janela_cadastro, text="Endereço:").grid(row=2, column=0, sticky='w', padx=10, pady=10)
    entry_endereco = ttk.Entry(janela_cadastro)
    entry_endereco.grid(row=2, column=1, sticky='e', padx=10, pady=10)

    ttk.Label(janela_cadastro, text="Email:").grid(row=3, column=0, sticky='w', padx=10, pady=10)
    entry_email = ttk.Entry(janela_cadastro)
    entry_email.grid(row=3, column=1, sticky='e', padx=10, pady=10)

    ttk.Label(janela_cadastro, text="Telefone:").grid(row=4, column=0, sticky='w', padx=10, pady=10)
    entry_telefone = ttk.Entry(janela_cadastro)
    entry_telefone.grid(row=4, column=1, sticky='e', padx=10, pady=10)

    ttk.Label(janela_cadastro, text="Data de Cadastro:").grid(row=5, column=0, sticky='w', padx=10, pady=10)
    entry_data_cadastro = ttk.Entry(janela_cadastro)
    entry_data_cadastro.grid(row=5, column=1, sticky='e', padx=10, pady=10)

    ttk.Button(janela_cadastro, text="Salvar", command=lambda: cadastrar_cliente(
        entry_nome.get(),
        entry_cpf.get(),
        entry_endereco.get(),
        entry_email.get(),
        entry_telefone.get(),
        entry_data_cadastro.get())).grid(row=6, column=1, padx=10, pady=10)

    janela_cadastro.mainloop()


def interface_cadastro_funcionarios():
    janela_funcionarios = tk.Toplevel()
    janela_funcionarios.title("Cadastro de Funcionários")
    janela_funcionarios.geometry("400x400")

    ttk.Label(janela_funcionarios, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome_func = ttk.Entry(janela_funcionarios)
    entry_nome_func.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(janela_funcionarios, text="CPF:").grid(row=1, column=0, padx=10, pady=5)
    entry_cpf_func = ttk.Entry(janela_funcionarios)
    entry_cpf_func.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(janela_funcionarios, text="Endereço:").grid(row=2, column=0, padx=10, pady=5)
    entry_endereco_func = ttk.Entry(janela_funcionarios)
    entry_endereco_func.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(janela_funcionarios, text="Cargo:").grid(row=3, column=0, padx=10, pady=5)
    entry_cargo = ttk.Entry(janela_funcionarios)
    entry_cargo.grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(janela_funcionarios, text="Email:").grid(row=4, column=0, padx=10, pady=5)
    entry_email_func = ttk.Entry(janela_funcionarios)
    entry_email_func.grid(row=4, column=1, padx=10, pady=5)

    ttk.Label(janela_funcionarios, text="Telefone:").grid(row=5, column=0, padx=10, pady=5)
    entry_telefone_func = ttk.Entry(janela_funcionarios)
    entry_telefone_func.grid(row=5, column=1, padx=10, pady=5)

    ttk.Label(janela_funcionarios, text="Data de Admissão:").grid(row=6, column=0, padx=10, pady=5)
    entry_data_admissao = ttk.Entry(janela_funcionarios)
    entry_data_admissao.grid(row=6, column=1, padx=10, pady=5)

    ttk.Label(janela_funcionarios, text="Salário:").grid(row=7, column=0, padx=10, pady=5)
    entry_salario = ttk.Entry(janela_funcionarios)
    entry_salario.grid(row=7, column=1, padx=10, pady=5)

    ttk.Button(janela_funcionarios, text="Salvar", command=lambda: cadastrar_funcionario(
        entry_nome_func.get(),
        entry_cpf_func.get(),
        entry_endereco_func.get(),
        entry_cargo.get(),
        entry_email_func.get(),
        entry_telefone_func.get(),
        entry_data_admissao.get(),
        entry_salario.get())).grid(row=8, column=1, padx=10, pady=10)

    janela_funcionarios.mainloop()


def interface_cadastro_produtos():
    janela_produtos = tk.Toplevel()
    janela_produtos.title("Cadastro de Produtos")
    janela_produtos.geometry("400x400")

    ttk.Label(janela_produtos, text="Nome do Produto:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome_produto = ttk.Entry(janela_produtos)
    entry_nome_produto.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(janela_produtos, text="Descrição:").grid(row=1, column=0, padx=10, pady=5)
    entry_descricao = ttk.Entry(janela_produtos)
    entry_descricao.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(janela_produtos, text="Número de Série:").grid(row=2, column=0, padx=10, pady=5)
    entry_numero_serie = ttk.Entry(janela_produtos)
    entry_numero_serie.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(janela_produtos, text="Preço:").grid(row=3, column=0, padx=10, pady=5)
    entry_preco = ttk.Entry(janela_produtos)
    entry_preco.grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(janela_produtos, text="Quantidade em Estoque:").grid(row=4, column=0, padx=10, pady=5)
    entry_quantidade_estoque = ttk.Entry(janela_produtos)
    entry_quantidade_estoque.grid(row=4, column=1, padx=10, pady=5)

    ttk.Label(janela_produtos, text="Categoria:").grid(row=5, column=0, padx=10, pady=5)
    entry_categoria = ttk.Entry(janela_produtos)
    entry_categoria.grid(row=5, column=1, padx=10, pady=5)

    ttk.Button(janela_produtos, text="Salvar", command=lambda: cadastrar_produto(
        entry_nome_produto.get(),
        entry_descricao.get(),
        entry_numero_serie.get(),
        entry_preco.get(),
        entry_quantidade_estoque.get(),
        entry_categoria.get())).grid(row=6, column=1, padx=10, pady=10)

    janela_produtos.mainloop()


def interface_registro_vendas():
    janela_vendas = tk.Toplevel()
    janela_vendas.title("Registro de Vendas")
    janela_vendas.geometry("400x300")

    ttk.Label(janela_vendas, text="ID do Cliente:").grid(row=0, column=0, padx=10, pady=5)
    entry_cliente_id = ttk.Entry(janela_vendas)
    entry_cliente_id.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(janela_vendas, text="ID do Funcionário:").grid(row=1, column=0, padx=10, pady=5)
    entry_funcionario_id = ttk.Entry(janela_vendas)
    entry_funcionario_id.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(janela_vendas, text="Data da Venda:").grid(row=2, column=0, padx=10, pady=5)
    entry_data_venda = ttk.Entry(janela_vendas)
    entry_data_venda.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(janela_vendas, text="Total da Venda:").grid(row=3, column=0, padx=10, pady=5)
    entry_total_venda = ttk.Entry(janela_vendas)
    entry_total_venda.grid(row=3, column=1, padx=10, pady=5)

    ttk.Button(janela_vendas, text="Registrar", command=lambda: registrar_venda(
        entry_cliente_id.get(),
        entry_funcionario_id.get(),
        entry_total_venda.get(),
        entry_data_venda.get())).grid(row=4, column=1, padx=10, pady=10)

    janela_vendas.mainloop()


def interface_cadastro_itens_venda():
    janela_itens_venda = tk.Toplevel()
    janela_itens_venda.title("Cadastro de Itens de Venda")
    janela_itens_venda.geometry("400x300")

    ttk.Label(janela_itens_venda, text="ID da Venda:").grid(row=0, column=0, padx=10, pady=5)
    entry_venda_id = ttk.Entry(janela_itens_venda)
    entry_venda_id.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(janela_itens_venda, text="ID do Produto:").grid(row=1, column=0, padx=10, pady=5)
    entry_produto_id = ttk.Entry(janela_itens_venda)
    entry_produto_id.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(janela_itens_venda, text="Quantidade:").grid(row=2, column=0, padx=10, pady=5)
    entry_quantidade = ttk.Entry(janela_itens_venda)
    entry_quantidade.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(janela_itens_venda, text="Preço Unitário:").grid(row=3, column=0, padx=10, pady=5)
    entry_preco = ttk.Entry(janela_itens_venda)
    entry_preco.grid(row=3, column=1, padx=10, pady=5)

    ttk.Button(janela_itens_venda, text="Salvar", command=lambda: cadastrar_item_venda(
        entry_venda_id.get(),
        entry_produto_id.get(),
        entry_quantidade.get(),
        entry_preco.get())).grid(row=4, column=1, padx=10, pady=10)

    janela_itens_venda.mainloop()


    
    

def abrir_janela_cadastro():
    janela_cadastro = tk.Toplevel(root)
    janela_cadastro.title("Opções de Cadastro")
    janela_cadastro.geometry("300x250")  # Ajusta o tamanho conforme necessário

    tk.Button(janela_cadastro, text="Cadastro de Clientes", command=interface_cadastro_clientes).pack(fill='x', padx=10, pady=5)
    tk.Button(janela_cadastro, text="Cadastro de Funcionários", command=interface_cadastro_funcionarios).pack(fill='x', padx=10, pady=5)
    tk.Button(janela_cadastro, text="Cadastro de Produtos", command=interface_cadastro_produtos).pack(fill='x', padx=10, pady=5)
    tk.Button(janela_cadastro, text="Registro de Vendas", command=interface_registro_vendas).pack(fill='x', padx=10, pady=5)
    tk.Button(janela_cadastro, text="Registro de Itens da Venda", command=interface_cadastro_itens_venda).pack(fill='x', padx=10, pady=5)

def abrir_janela_consulta_clientes():
    tabela = 'Clientes'
    colunas = ('Nome', 'CPFCNPJ', 'Endereco', 'Email', 'Telefone', 'DataCadastro')
    abrir_janela_consulta(tabela, colunas)

def abrir_janela_consulta_funcionarios():
    tabela = 'Funcionarios'
    colunas = ('Nome', 'CPF', 'Endereco', 'Cargo', 'Email', 'Telefone', 'DataAdmissao', 'Salario')
    abrir_janela_consulta(tabela, colunas)

def abrir_janela_consulta_produtos():
    tabela = 'Produtos'
    colunas = ('NomeProduto', 'Descricao', 'NumeroSerie', 'Preco', 'QuantidadeEstoque', 'Categoria')
    abrir_janela_consulta(tabela, colunas)

def abrir_janela_consulta_vendas():
    tabela = 'Vendas'
    colunas = ('VendaID', 'ClienteID', 'FuncionarioID', 'DataVenda', 'TotalVenda')
    abrir_janela_consulta(tabela, colunas)
    

def abrir_menu_consultas():
    janela_consultas = tk.Toplevel(root)
    janela_consultas.title("Consultas")
    janela_consultas.geometry("300x250")

    tk.Button(janela_consultas, text="Clientes", command=abrir_janela_consulta_clientes).pack(fill='x', padx=10, pady=5)
    tk.Button(janela_consultas, text="Funcionários", command=abrir_janela_consulta_funcionarios).pack(fill='x', padx=10, pady=5)
    tk.Button(janela_consultas, text="Produtos", command=abrir_janela_consulta_produtos).pack(fill='x', padx=10, pady=5)
    tk.Button(janela_consultas, text="Vendas", command=abrir_janela_consulta_vendas).pack(fill='x', padx=10, pady=5)

def sair_do_programa():
    if messagebox.askyesno("Confirmação", "Você realmente deseja sair?"):
        root.destroy()

def main():
    global root
    root = tk.Tk()
    root.title("Sistema de Cadastro - Loja Tech")
    root.geometry("800x600")

    try:
        # Carregar a imagem original
        original_image = Image.open("C:/Users/Estudos/Pictures/Logo.png")

        # Redimensionar a imagem
        resized_image = original_image.resize((500, 300))
        logo_image = ImageTk.PhotoImage(resized_image)

        # Adicionar a imagem redimensionada ao Label
        logo_label = tk.Label(root, image=logo_image)
        logo_label.pack(pady=20)

        # Frame para os botões
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(fill='x', padx=20, pady=20)

        tk.Button(frame_botoes, text="Cadastro", command=abrir_janela_cadastro).pack(fill='x', padx=10, pady=5)
        tk.Button(frame_botoes, text="Consulta", command=abrir_menu_consultas).pack(fill='x', padx=10, pady=5)
        tk.Button(frame_botoes, text="Sair", command=sair_do_programa).pack(fill='x', padx=10, pady=5)

    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível carregar a imagem: {e}")

    root.mainloop()

if __name__ == "__main__":
    main()


